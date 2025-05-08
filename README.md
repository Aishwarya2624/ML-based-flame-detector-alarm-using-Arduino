# 🔥 ML-Based Flame Detector Alarm using Arduino and Logistic Regression

## 🔧 Project Description

This project integrates a flame sensor with an Arduino to detect the presence of flame in real-time. The sensor readings are analyzed using a logistic regression model trained in Python, which predicts the probability of a flame being present. A buzzer is triggered if flame is detected, and the live data is also visualized in a desktop GUI application built with Tkinter.

---

## 🎯 Objective

To develop a reliable flame detection system using machine learning (logistic regression) and Arduino that can:
- Accurately detect flame presence.
- Raise an alert using a buzzer.
- Display live data and prediction probability on a desktop GUI.

---

## 🧰 Components Used

- Arduino Uno
- Flame Sensor (Analog Output)
- Buzzer
- Jumper Wires
- USB Cable (for Arduino connection)
- PC with Python (for GUI and model)
- 10k Ohm Resistor (optional, for stable sensor connection)

---

## 🧠 Machine Learning Model

- **Model Used**: Logistic Regression
- **Why Logistic Regression?**
  - It's simple, efficient, and perfect for binary classification (flame vs. no flame).
- **Inputs**: Raw sensor analog value.
- **Output**: Probability (0 to 1) of flame presence.
- **Threshold**: If probability > 0.5 → flame detected.

---

## 🛠️ Arduino Circuit Connections

| Component     | Arduino Pin |
|---------------|-------------|
| Flame Sensor  | A0          |
| Buzzer        | D8          |
| GND           | GND         |
| VCC           | 5V          |

---

## 🖥️ GUI Features (Python Tkinter)

- Shows **raw sensor value**
- Displays **flame probability**
- Indicates **flame status**
- Refreshes in real-time
- Uses **pySerial** to communicate with Arduino

#How to run??
-  ✅ Prerequisites
Make sure you have the following installed:

Python (3.7 or later) → https://python.org

Arduino IDE → https://www.arduino.cc/en/software

🔌 Step-by-Step Setup
🔹 Step 1: Open VS Code
            Open VS Code and use File > Open Folder to open your FlameDetectorProject folder.
🔹 Step 2: Upload Arduino Code
            Connect your Arduino board via USB.
            Open sketch_flame.ino in the Arduino IDE.
            Make sure the correct board and COM port are selected.
            Click Upload.
    Step 3: Train the ML Model
    Step 4: Run the GUI
            python flame_detector.py




