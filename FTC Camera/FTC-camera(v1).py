"""FTC-Camera: live camera feed + AprilTag tracking, ChatGPT-style UI (dark/light)."""
import json
import math
import os
import subprocess
import tempfile
import wave
import sys
import threading
import time
import tkinter as tk
from concurrent.futures import ThreadPoolExecutor
from tkinter import font as tkfont

import cv2
import numpy as np
from PIL import Image, ImageTk
from pupil_apriltags import Detector

try:
    import AVFoundation as AVF  # optional (pyobjc): real camera names
except Exception:
    AVF = None

CONFIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "FTC-Camera.json")
ROTATIONS = {0: None, 90: cv2.ROTATE_90_CLOCKWISE, 180: cv2.ROTATE_180,
             270: cv2.ROTATE_90_COUNTERCLOCKWISE}
MAX_PROBE = 6
BACKEND = cv2.CAP_AVFOUNDATION if sys.platform == "darwin" else cv2.CAP_ANY
DETECT_W = 960          # detect on frames at most this wide
TAG_PRED = 5.0          # keep a tag (optical flow, else last position) this long without a detection
BOX_SCALE = 2.0         # box height as a multiple of the tag size
GUIDE_MAX_AGE = 1.0     # guide only from tags positively detected this recently
DARKEN = (255 * (np.arange(256) / 255.0) ** 4).astype(np.uint8)   # gamma LUT for glare

THEMES = {
    "dark": dict(BG="#212121", SIDE="#171717", PANEL="#2F2F2F", HOVER="#3A3A3A",
                 LINE="#383838", TEXT="#ECECEC", MUTED="#9B9B9B", OFF="#555555"),
    "light": dict(BG="#FFFFFF", SIDE="#F9F9F9", PANEL="#ECECEC", HOVER="#E0E0E0",
                  LINE="#E5E5E5", TEXT="#0D0D0D", MUTED="#6B6B6B", OFF="#C4C4C4"),
}
GREEN, RED = "#10A37F", "#EF4444"

# Official AprilTag C library (UMich), via pupil-apriltags: pip install pupil-apriltags
DETECTOR = Detector(families="tag36h11", nthreads=4, quad_decimate=1.5, refine_edges=True,
                    decode_sharpening=0.25)


class Sound:
    """Pre-rendered voice prompts + beep, played with afplay (macOS) for low latency."""
    PHRASES = {1: "Left", 2: "Right", 3: "Front", 4: "Back", 5: "Rotate clockwise",
               6: "Rotate counter clockwise", 7: "Stop", 8: "Aligned"}

    def __init__(self):
        self.dir = tempfile.mkdtemp(prefix="ftc_snd_")
        self.files = {}
        self.proc = {"voice": None, "beep": None}
        self.enabled = sys.platform == "darwin"
        if self.enabled:
            threading.Thread(target=self._render, daemon=True).start()

    def _render(self):
        path = os.path.join(self.dir, "beep.wav")
        sr = 44100
        t = np.arange(int(sr * 0.16)) / sr
        tone = np.concatenate([np.sin(2 * np.pi * 880 * t[:len(t) // 2]),
                               np.sin(2 * np.pi * 1320 * t[len(t) // 2:])])
        tone *= np.minimum(1, np.minimum(t, t[::-1]) * 200) * 0.5
        with wave.open(path, "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(sr)
            w.writeframes((tone * 32767).astype(np.int16).tobytes())
        self.files["beep"] = path
        for code, text in self.PHRASES.items():
            threading.Thread(target=self._say_to_file, args=(code, text), daemon=True).start()

    def _say_to_file(self, code, text):
        f = os.path.join(self.dir, f"c{code}.aiff")
        try:
            subprocess.run(["say", "-r", "230", "-o", f, text], check=True,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            self.files[code] = f
        except Exception:
            pass

    def play(self, key, slot):
        if not self.enabled:
            return
        f = self.files.get(key)
        if f:
            cmd = ["afplay", f]
        elif key in self.PHRASES:           # file not rendered yet: speak live
            cmd = ["say", "-r", "230", self.PHRASES[key]]
        else:
            return
        old = self.proc[slot]
        if old is not None and old.poll() is None:
            old.terminate()
        try:
            self.proc[slot] = subprocess.Popen(cmd, stdout=subprocess.DEVNULL,
                                               stderr=subprocess.DEVNULL)
        except Exception:
            pass


def device_names():
    if AVF is None:
        return []
    try:
        devs = AVF.AVCaptureDevice.devicesWithMediaType_(AVF.AVMediaTypeVideo)
        return [str(d.localizedName()) for d in devs]
    except Exception:
        return []


def probe(i):
    cap = cv2.VideoCapture(i, BACKEND)
    ok = cap.isOpened() and cap.read()[0]
    cap.release()
    return i if ok else None


def round_rect(c, x1, y1, x2, y2, r, **kw):
    r = min(r, (x2 - x1) / 2, (y2 - y1) / 2)
    pts = [x1 + r, y1, x2 - r, y1, x2, y1, x2, y1 + r, x2, y2 - r, x2, y2,
           x2 - r, y2, x1 + r, y2, x1, y2, x1, y2 - r, x1, y1 + r, x1, y1]
    return c.create_polygon(pts, smooth=True, **kw)


class Pill(tk.Canvas):
    """Fully rounded clickable button / list row."""

    def __init__(self, parent, text, cmd, font, bg, fg, hover, parent_bg,
                 height=38, radius=None, anchor="center"):
        super().__init__(parent, height=height, bg=parent_bg, highlightthickness=0,
                         cursor="hand2")
        self.text, self.cmd, self.f = text, cmd, font
        self.bg, self.fg, self.hover, self.h = bg, fg, hover, height
        self.radius = radius if radius is not None else height / 2
        self.anchor, self.cur = anchor, bg
        self.bind("<Configure>", lambda e: self.draw())
        self.bind("<Enter>", lambda e: self.set(self.hover))
        self.bind("<Leave>", lambda e: self.set(self.bg))
        self.bind("<Button-1>", lambda e: self.cmd())

    def set(self, col):
        self.cur = col
        self.draw()

    def draw(self):
        self.delete("all")
        w = self.winfo_width()
        round_rect(self, 1, 1, w - 1, self.h - 1, self.radius, fill=self.cur, outline=self.cur)
        if self.anchor == "w":
            self.create_text(16, self.h / 2, text=self.text, fill=self.fg, font=self.f, anchor="w")
        else:
            self.create_text(w / 2, self.h / 2, text=self.text, fill=self.fg, font=self.f)


class CameraApp:
    def __init__(self, root):
        self.root = root
        root.title("FTC Camera")
        root.geometry("1180x720")
        root.minsize(760, 480)
        fam = "SF Pro Text" if sys.platform == "darwin" else "Segoe UI"
        self.f = tkfont.Font(family=fam, size=13)
        self.fb = tkfont.Font(family=fam, size=13, weight="bold")
        self.fs = tkfont.Font(family=fam, size=11)
        self.ft = tkfont.Font(family=fam, size=20, weight="bold")

        self.theme = "dark"
        self.cap = None
        self.photo = None
        self.cams = []          # [(index, name)]
        self.current = None
        self.mirror = tk.BooleanVar(value=False)
        self.orient = 0         # camera orientation, degrees clockwise (remembered)
        try:
            with open(CONFIG) as fh:
                o = int(json.load(fh).get("orientation", 0))
            self.orient = o if o in ROTATIONS else 0
        except Exception:
            pass
        self.tags_on = tk.BooleanVar(value=True)
        self.light = tk.BooleanVar(value=False)
        self.guide_on = tk.BooleanVar(value=True)
        self.prev_gray = None
        self.last_tag_time = time.time()
        self.sound_on = tk.BooleanVar(value=True)
        self.sound = Sound()
        self.cur_cmd = 7        # command currently "running" (7 = stopped)
        self.pending, self.pending_n = 7, 0
        self.aligned = False
        self.announced = False
        self.box_side = None    # smoothed tag side length, frame px
        self.cmd_log = []
        self.guide_info = None  # (code, label) shown on the feed
        self.scanning = False
        self.frames, self.t0 = 0, time.time()
        self.last_frame = None
        self.tracked = {}       # id -> dict(center, angle, corners, seen)
        self.status_text, self.status_col = "", None
        self.title_text, self.fps_text = "No camera", ""
        self.view_text = "Looking for cameras…"

        root.bind("<Command-s>", lambda e: self.snapshot())
        root.bind("<Control-s>", lambda e: self.snapshot())
        root.protocol("WM_DELETE_WINDOW", self.close)
        self.build_ui()
        self.refresh()
        self.tick()

    # ---------- UI
    def c(self, k):
        return THEMES[self.theme][k]

    def build_ui(self):
        for w in self.root.winfo_children():
            w.destroy()
        c = self.c
        self.root.configure(bg=c("BG"))
        side = tk.Frame(self.root, bg=c("SIDE"), width=280)
        side.pack(side="left", fill="y")
        side.pack_propagate(False)
        tk.Label(side, text="FTC Camera", bg=c("SIDE"), fg=c("TEXT"), font=self.ft,
                 anchor="w").pack(fill="x", padx=20, pady=(24, 2))
        tk.Label(side, text="Live feed · AprilTag tracking", bg=c("SIDE"), fg=c("MUTED"),
                 font=self.fs, anchor="w").pack(fill="x", padx=20, pady=(0, 18))

        row = tk.Frame(side, bg=c("SIDE"))
        row.pack(fill="x", padx=20, pady=(0, 8))
        tk.Label(row, text="CAMERAS", bg=c("SIDE"), fg=c("MUTED"), font=self.fs).pack(side="left")
        Pill(row, "⟳ Refresh", self.refresh, self.fs, c("SIDE"), c("MUTED"), c("HOVER"),
             c("SIDE"), height=26).pack(side="right")
        row.winfo_children()[-1].config(width=84)

        self.list_frame = tk.Frame(side, bg=c("SIDE"))
        self.list_frame.pack(fill="x", padx=14)

        tk.Frame(side, bg=c("LINE"), height=1).pack(fill="x", padx=20, pady=16)
        for text, var in (("Detect AprilTags", self.tags_on), ("Guide to centre box", self.guide_on),
                          ("Sound & voice", self.sound_on),
                          ("Mirror view", self.mirror),
                          ("Light mode", self.light)):
            self.toggle(side, text, var).pack(fill="x", padx=20, pady=5)
        self.orient_btn = Pill(side, f"⟳  Orientation: {self.orient}°", self.rotate_orientation,
                               self.f, c("PANEL"), c("TEXT"), c("HOVER"), c("SIDE"), height=42)
        self.orient_btn.pack(fill="x", padx=20, pady=(16, 0))
        Pill(side, "📷  Save snapshot", self.snapshot, self.f, c("PANEL"), c("TEXT"),
             c("HOVER"), c("SIDE"), height=42).pack(fill="x", padx=20, pady=(16, 0))

        self.log_lbl = tk.Label(side, text="\n".join(self.cmd_log[-5:]), bg=c("SIDE"),
                                fg=c("MUTED"), font=self.fs, anchor="w", justify="left")
        self.log_lbl.pack(side="bottom", fill="x", padx=20)
        self.status = tk.Label(side, text=self.status_text, bg=c("SIDE"),
                               fg=self.status_col or c("MUTED"), font=self.fs, anchor="w",
                               justify="left", wraplength=240)
        self.status.pack(side="bottom", fill="x", padx=20, pady=16)

        main = tk.Frame(self.root, bg=c("BG"))
        main.pack(side="left", fill="both", expand=True)
        head = tk.Frame(main, bg=c("BG"))
        head.pack(fill="x", padx=24, pady=(18, 8))
        self.title = tk.Label(head, text=self.title_text, bg=c("BG"), fg=c("TEXT"), font=self.fb)
        self.title.pack(side="left")
        self.fps_lbl = tk.Label(head, text=self.fps_text, bg=c("BG"), fg=c("MUTED"), font=self.fs)
        self.fps_lbl.pack(side="right")
        self.view = tk.Label(main, bg=c("BG"), fg=c("MUTED"), font=self.f, text=self.view_text)
        self.view.pack(fill="both", expand=True, padx=24, pady=(0, 24))
        self.render_list()

    def toggle(self, parent, text, var):
        c = self.c
        fr = tk.Frame(parent, bg=c("SIDE"))
        lab = tk.Label(fr, text=text, bg=c("SIDE"), fg=c("TEXT"), font=self.f)
        lab.pack(side="left")
        cv = tk.Canvas(fr, width=44, height=24, bg=c("SIDE"), highlightthickness=0,
                       cursor="hand2")
        cv.pack(side="right")

        def draw():
            cv.delete("all")
            col = GREEN if var.get() else c("OFF")
            round_rect(cv, 1, 1, 43, 23, 12, fill=col, outline=col)
            x = 23 if var.get() else 4
            cv.create_oval(x, 4, x + 16, 20, fill="white", outline="white")

        def flip(_=None):
            var.set(not var.get())
            draw()
            if var is self.light:
                self.theme = "light" if var.get() else "dark"
                self.root.after(10, self.build_ui)
        for w in (cv, lab):
            w.bind("<Button-1>", flip)
        draw()
        return fr

    def render_list(self):
        c = self.c
        for w in self.list_frame.winfo_children():
            w.destroy()
        if not self.cams:
            tk.Label(self.list_frame, text="No cameras found", bg=c("SIDE"), fg=c("MUTED"),
                     font=self.f, anchor="w").pack(fill="x", padx=8, pady=6)
        for idx, name in self.cams:
            sel = idx == self.current
            Pill(self.list_frame, ("●  " if sel else "○  ") + name,
                 lambda i=idx: self.open_cam(i), self.f,
                 c("PANEL") if sel else c("SIDE"), c("TEXT") if sel else c("MUTED"),
                 c("PANEL") if sel else c("HOVER"), c("SIDE"), height=40, anchor="w"
                 ).pack(fill="x", pady=2)

    def set_status(self, text, color=None):
        self.status_text, self.status_col = text, color
        self.status.config(text=text, fg=color or self.c("MUTED"))

    # ---------- cameras
    def refresh(self):
        if self.scanning:
            return
        self.scanning = True
        self.set_status("Scanning…")
        threading.Thread(target=self._scan, daemon=True).start()

    def _scan(self):
        names = device_names()
        with ThreadPoolExecutor(MAX_PROBE) as ex:
            found = [i for i in ex.map(probe, range(MAX_PROBE)) if i is not None]
        cams = [(i, names[i] if i < len(names) else f"Camera {i}") for i in found]
        self.root.after(0, self._scan_done, cams)

    def _scan_done(self, cams):
        self.scanning = False
        self.cams = cams
        if self.current is not None and not any(i == self.current for i, _ in cams):
            self.release()
        if cams and self.current is None:
            self.open_cam(cams[0][0])
        elif not cams:
            self.release()
            self.title_text, self.view_text = "No camera", "No camera available"
            self.title.config(text=self.title_text)
            self.view.config(image="", text=self.view_text)
            self.set_status("No cameras found")
        self.render_list()
        if cams:
            self.set_status(f"{len(cams)} camera(s) found", GREEN)

    def release(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None
        self.current = None

    def open_cam(self, idx):
        if idx == self.current and self.cap is not None:
            return
        if self.cap is not None:
            self.cap.release()
            self.cap = None
        cap = cv2.VideoCapture(idx, BACKEND)
        if not cap.isOpened():
            self.set_status(f"Could not open camera {idx}", RED)
            return
        self.cap, self.current = cap, idx
        name = dict(self.cams).get(idx, f"Camera {idx}")
        self.title_text = name
        self.title.config(text=name)
        self.set_status(f"Streaming {name}", GREEN)
        self.frames, self.t0 = 0, time.time()
        self.tracked.clear()
        self.prev_gray = None
        self.render_list()

    def rotate_orientation(self):
        """Turn the camera's reference frame 90 deg; front/back/rotate follow it."""
        self.orient = (self.orient + 90) % 360
        self.orient_btn.text = f"⟳  Orientation: {self.orient}°"
        self.orient_btn.draw()
        if self.cur_cmd != 7:
            self.send_command(7)
        self.tracked.clear()
        self.prev_gray = None
        self.box_side, self.aligned = None, False
        self.pending, self.pending_n = 7, 0
        try:
            with open(CONFIG, "w") as fh:
                json.dump({"orientation": self.orient}, fh)
        except Exception:
            pass

    def snapshot(self):
        if self.last_frame is None:
            return
        path = time.strftime("ftc_snapshot_%Y%m%d_%H%M%S.jpg")
        cv2.imwrite(path, self.last_frame)
        self.set_status(f"Saved {path}", GREEN)

    # ---------- AprilTags
    def _find(self, gray):
        """Detect on gray and on its mirror image -> [(tag, flipped)]."""
        hits = [(t, False) for t in DETECTOR.detect(gray)]
        have = {t.tag_id for t, _ in hits}
        hits += [(t, True) for t in DETECTOR.detect(cv2.flip(gray, 1)) if t.tag_id not in have]
        return [(t, f) for t, f in hits if t.hamming <= 1 and t.decision_margin >= 15]

    def _find_multi(self, gray):
        """Raw pass, then a darkened pass (rescues over-exposed / washed-out frames)."""
        return self._find(gray) or self._find(cv2.LUT(gray, DARKEN))

    def _set(self, tid, q, flipped, now, detected, **keep):
        """q: 4x2 corners TL,TR,BR,BL in frame px. Updates the tracked entry."""
        top = q[1] - q[0]
        screen_angle = math.degrees(math.atan2(top[1], top[0]))   # clockwise from +x
        angle = (180 - screen_angle + 180) % 360 - 180 if flipped else screen_angle
        side = float(np.mean([np.linalg.norm(q[i] - q[(i + 1) % 4]) for i in range(4)]))
        mid = (q[0] + q[1]) / 2 - q.mean(axis=0)         # centre -> red (top) edge
        up_err = (math.degrees(math.atan2(mid[1], mid[0])) + 90 + 180) % 360 - 180
        old = self.tracked.get(tid)
        if old is None and self.sound_on.get():
            self.sound.play("beep", "beep")              # tag newly detected
        self.tracked[tid] = dict(corners=q, center=q.mean(axis=0), angle=angle,
                                 screen_angle=screen_angle, up_err=up_err, side=side, mirrored=flipped,
                                 seen=now, det=now if detected else (old or keep)["det"],
                                 predicted=not detected)

    def detect(self, frame):
        """Keep track of AprilTags at all times: official detector (normal + mirrored,
        raw + darkened), a zoomed search around lost tags, then optical-flow prediction."""
        h, w = frame.shape[:2]
        k = min(1.0, DETECT_W / w)
        full = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        small = cv2.resize(full, None, fx=k, fy=k, interpolation=cv2.INTER_AREA) if k < 1 else full
        sw = small.shape[1]
        now = time.time()
        got = set()
        for t, flipped in self._find_multi(small):
            q = t.corners[[3, 2, 1, 0]].astype(np.float64)       # -> TL, TR, BR, BL
            if flipped:
                q[:, 0] = sw - 1 - q[:, 0]
            self._set(int(t.tag_id), q / k, flipped, now, True)
            got.add(int(t.tag_id))
        # zoomed search around tags we have but did not see this frame
        for tid, d in list(self.tracked.items()):
            if tid in got:
                continue
            cx, cy = d["center"]
            r = int(d["side"] * 1.8) + 20
            x0, y0 = max(0, int(cx) - r), max(0, int(cy) - r)
            x1, y1 = min(w, int(cx) + r), min(h, int(cy) + r)
            roi = full[y0:y1, x0:x1]
            if roi.size == 0:
                continue
            zoom = max(1.0, 240.0 / max(roi.shape))
            if zoom > 1:
                roi = cv2.resize(roi, None, fx=zoom, fy=zoom, interpolation=cv2.INTER_CUBIC)
            rw = roi.shape[1]
            for t, flipped in self._find_multi(roi):
                if int(t.tag_id) != tid:
                    continue
                q = t.corners[[3, 2, 1, 0]].astype(np.float64)
                if flipped:
                    q[:, 0] = rw - 1 - q[:, 0]
                q = q / zoom + (x0, y0)
                self._set(tid, q, flipped, now, True)
                got.add(tid)
                break
        # optical-flow prediction for the rest
        if self.prev_gray is not None and self.prev_gray.shape == small.shape:
            for tid, d in list(self.tracked.items()):
                if tid in got:
                    continue
                p0 = (d["corners"] * k).astype(np.float32).reshape(-1, 1, 2)
                p1, st, err = cv2.calcOpticalFlowPyrLK(
                    self.prev_gray, small, p0, None, winSize=(31, 31), maxLevel=3,
                    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 20, 0.01))
                if p1 is not None and st.all() and float(err.max()) < 25:
                    self._set(tid, p1.reshape(4, 2).astype(np.float64) / k, d["mirrored"],
                              now, False)
        self.prev_gray = small
        for tid in [t for t, d in self.tracked.items()
                    if now - d["det"] > TAG_PRED]:
            del self.tracked[tid]
        if self.tracked:
            self.last_tag_time = now

    def draw_tags(self, img, s):
        """Draw tag outlines (quad borders, not bounding boxes) + readout panel."""
        tags = sorted(self.tracked.items())
        for tid, d in tags:
            q = (d["corners"] * s).astype(np.int32)
            cv2.polylines(img, [q.reshape(-1, 1, 2)], True, (166, 163, 16), 3, cv2.LINE_AA)
            cv2.line(img, tuple(q[0]), tuple(q[1]), (68, 68, 239), 4, cv2.LINE_AA)  # top edge
            ctr = (d["center"] * s)
            tip = (q[0] + q[1]) / 2
            cv2.arrowedLine(img, tuple(ctr.astype(int)), tuple(tip.astype(int)),
                            (255, 255, 255), 2, cv2.LINE_AA, tipLength=0.3)
            cv2.putText(img, f"ID {tid}", (q[:, 0].min(), q[:, 1].min() - 8),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (166, 163, 16), 2, cv2.LINE_AA)
        # readout, bottom-left
        lines = [f"AprilTags: {len(tags)}"] + [
            f"ID {t:<3} x {d['center'][0]:6.0f}  y {d['center'][1]:6.0f}  rot {d['angle']:7.1f} deg"
            + (" (mirrored)" if d.get("mirrored") else "")
            + (" (tracking)" if d.get("predicted") else "")
            for t, d in tags[:8]]
        lh, pad = 24, 12
        bw = max(cv2.getTextSize(l, cv2.FONT_HERSHEY_SIMPLEX, 0.55, 1)[0][0] for l in lines)
        bh = lh * len(lines) + pad
        H = img.shape[0]
        x0, y0 = 12, H - 12 - bh
        if y0 < 0 or x0 + bw + 2 * pad > img.shape[1]:
            return
        roi = img[y0:y0 + bh, x0:x0 + bw + 2 * pad]
        roi[:] = (roi * 0.35).astype(np.uint8)
        for i, l in enumerate(lines):
            cv2.putText(img, l, (x0 + pad, y0 + pad + lh * i + 8), cv2.FONT_HERSHEY_SIMPLEX,
                        0.55, (255, 255, 255) if i else (166, 220, 16), 1, cv2.LINE_AA)

    # ---------- guidance to the centre box
    COMMANDS = {1: "LEFT", 2: "RIGHT", 3: "FRONT", 4: "BACK", 5: "ROTATE CW",
                6: "ROTATE CCW", 7: "STOP"}

    def send_command(self, code, aligned=False):
        """Hook for the robot: 1-6 run until a 7 (Stop) is sent."""
        self.cur_cmd = code
        if self.sound_on.get():
            self.sound.play(8 if aligned else code, "voice")
        line = f"{code}) {self.COMMANDS[code]}" + (" (aligned)" if aligned else "")
        self.cmd_log.append(time.strftime("%H:%M:%S  ") + line)
        self.cmd_log = self.cmd_log[-20:]
        self.log_lbl.config(text="\n".join(self.cmd_log[-5:]))
        print(line, flush=True)

    def centre_box(self, fw, fh):
        """Full-width band centred vertically, BOX_SCALE x the tag size tall."""
        if self.box_side is None:
            return None
        half = BOX_SCALE * self.box_side / 2
        return 0, fh / 2 - half, fw - 1, fh / 2 + half

    def target_tag(self, fw, fh):
        now = time.time()
        tags = [d for d in self.tracked.values() if now - d["det"] <= GUIDE_MAX_AGE]
        if not tags:
            return None
        ctr = np.array([fw / 2, fh / 2])
        return min(tags, key=lambda d: np.linalg.norm(d["center"] - ctr))

    def update_guidance(self, fw, fh):
        tag = self.target_tag(fw, fh)
        if tag is None:
            want = 7
            self.guide_info = None
        else:
            self.box_side = tag["side"] if self.box_side is None else \
                0.8 * self.box_side + 0.2 * tag["side"]
            # tag counts as inside once its whole outline fits anywhere in the box
            ext = (tag["corners"][:, 1].max() - tag["corners"][:, 1].min()) / 2
            tin = max(BOX_SCALE * self.box_side / 2 - ext, 2.0)
            tout = tin + 0.05 * self.box_side
            rin, rout = 15.0, 20.0
            dx = tag["center"][0] - fw / 2
            dy = tag["center"][1] - fh / 2
            err = tag["up_err"]       # 0 = red (top) edge straight up, on the top side
            cur = self.cur_cmd

            def thr(active, lo, hi):
                return lo if (active or not self.aligned) else hi
            by = abs(dy) > thr(cur in (3, 4), tin, tout)
            br = abs(err) > thr(cur in (5, 6), rin, rout)
            if by:                                     # step 1: tag into the box (front/back only)
                want = 3 if dy > 0 else 4              # tag below centre -> move front (up)
            elif br:                                   # step 2: red edge to the top
                want = 5 if err > 0 else 6             # (CW/CCW as the user wants them)
            else:
                want = 7
            self.guide_info = (want, dx, dy, err)
        self.aligned = want == 7 and tag is not None
        # debounce, then Stop between different commands
        if want == self.pending:
            self.pending_n += 1
        else:
            self.pending, self.pending_n = want, 1
        if self.pending_n >= 3 and want != self.cur_cmd:
            if self.cur_cmd != 7 and want != 7:
                self.send_command(7)
            if want == 7:
                self.send_command(7, aligned=tag is not None)
                self.announced = tag is not None
            elif want != 7:
                self.send_command(want)
        if want != 7:
            if self.pending_n >= 3:
                self.announced = False
        elif self.pending_n >= 3 and tag is not None and not self.announced:
            self.announced = True              # aligned without ever having moved
            self.send_command(7, aligned=True)

    def draw_guide(self, img, s, fw, fh):
        box = self.centre_box(fw, fh)
        if box is None:
            return
        done = self.cur_cmd == 7 and self.aligned
        col = (166, 163, 16) if done else (0, 180, 255)
        x1, y1, x2, y2 = (int(v * s) for v in box)
        cv2.rectangle(img, (x1, y1), (x2, y2), col, 2, cv2.LINE_AA)
        if self.guide_info is None:
            return
        code = self.cur_cmd if self.cur_cmd != 7 else self.guide_info[0]
        text = f"{code}) {self.COMMANDS[code]}" + ("  -  aligned" if done else "")
        (tw, th), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1.0, 2)
        x0, y0 = (img.shape[1] - tw) // 2, 24
        if tw + 40 > img.shape[1]:
            return
        roi = img[y0:y0 + th + 28, x0 - 20:x0 + tw + 20]
        roi[:] = (roi * 0.3).astype(np.uint8)
        cv2.putText(img, text, (x0, y0 + th + 10), cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                    col if done else (255, 255, 255), 2, cv2.LINE_AA)

    # ---------- loop
    def tick(self):
        if self.cap is not None:
            ok, frame = self.cap.read()
            if ok:
                if ROTATIONS[self.orient] is not None:
                    frame = cv2.rotate(frame, ROTATIONS[self.orient])
                if self.mirror.get():
                    frame = cv2.flip(frame, 1)
                self.last_frame = frame
                if self.tags_on.get():
                    self.detect(frame)
                    if not self.tracked and time.time() - self.last_tag_time > 2:
                        self.set_status("No tag found - reduce glare / phone brightness, "
                                        "keep a white margin around the tag")
                else:
                    self.tracked.clear()
                w, h = max(self.view.winfo_width(), 2), max(self.view.winfo_height(), 2)
                fh, fw = frame.shape[:2]
                s = min(w / fw, h / fh)
                img = cv2.resize(frame, (max(1, int(fw * s)), max(1, int(fh * s))),
                                 interpolation=cv2.INTER_AREA)
                if self.tags_on.get():
                    if self.guide_on.get():
                        self.update_guidance(fw, fh)
                        self.draw_guide(img, s, fw, fh)
                    self.draw_tags(img, s)
                self.photo = ImageTk.PhotoImage(
                    Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)))
                self.view.config(image=self.photo, text="")
                self.frames += 1
                dt = time.time() - self.t0
                if dt >= 1:
                    self.fps_text = f"{self.frames / dt:.0f} fps  ·  {fw}×{fh}"
                    self.fps_lbl.config(text=self.fps_text)
                    self.frames, self.t0 = 0, time.time()
        self.root.after(8, self.tick)

    def close(self):
        if self.cap is not None:
            self.cap.release()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    CameraApp(root)
    root.mainloop()
