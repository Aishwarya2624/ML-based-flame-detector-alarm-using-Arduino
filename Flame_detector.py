import tkinter as tk
import serial
import threading
import time

COM_PORT   = "COM7"     
BAUD_RATE  = 9600
REFRESH_MS = 200        

class FlameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ML Flame Detector Monitor")
        self.geometry("300x150")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.raw_var  = tk.StringVar(value="Raw: —")
        self.prob_var = tk.StringVar(value="Prob: —")
        self.status_var = tk.StringVar(value="Status: —")

        tk.Label(self, textvariable=self.raw_var,  font=("Helvetica", 14)).pack(pady=5)
        tk.Label(self, textvariable=self.prob_var, font=("Helvetica", 14)).pack(pady=5)
        tk.Label(self, textvariable=self.status_var, font=("Helvetica", 16, "bold")).pack(pady=5)

        self.serial_run = True
        self.ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
        threading.Thread(target=self.read_serial, daemon=True).start()

    def read_serial(self):
        while self.serial_run:
            line = self.ser.readline().decode(errors="ignore").strip()
            if line.startswith("Raw"):
                try:
                    parts = line.split("|")
                    raw   = parts[0].split("=")[1].strip()
                    self.raw_var.set(f"Raw: {raw}")
                    prob_raw = float(parts[1].split("=")[1].strip())
                    prob = 1.0 - prob_raw
                    self.prob_var.set(f"Prob: {prob:.4f}")

                    if prob > 0.5:
                        self.status_var.set("🔥 FLAME DETECTED")
                        self.status_var_label_fg("red")
                    else:
                        self.status_var.set("✅ No Flame")
                        self.status_var_label_fg("green")

                except Exception:
                    pass
            time.sleep(0.01)

    def status_var_label_fg(self, color):
        self.children[list(self.children)[-1]].config(fg=color)

    def on_close(self):
        self.serial_run = False
        self.ser.close()
        self.destroy()

if __name__ == "__main__":
    app = FlameApp()
    app.mainloop()
