# 🚗 AI Drowsiness Detection System using Computer Vision 😴

A real-time **AI-powered drowsiness detection system** that monitors eye movements using a webcam and alerts the user when signs of fatigue are detected.

This project helps in **preventing accidents** by detecting driver drowsiness using **facial landmark detection and Eye Aspect Ratio (EAR)**.

---

## 📌 Features

* 👁️ Real-time eye tracking using webcam
* 🧠 Drowsiness detection using Eye Aspect Ratio (EAR)
* 🚨 Instant alert system (beep sound)
* ⚡ Lightweight and fast processing
* 🎯 Works in real-time with high accuracy

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries Used:**

  * OpenCV
  * Dlib
  * Imutils
  * Scipy
  * NumPy

---

## 🧠 How It Works

1. Detects face using **Dlib face detector**
2. Extracts **facial landmarks (68 points)**
3. Focuses on **eye region**
4. Calculates **Eye Aspect Ratio (EAR)**
5. If EAR falls below threshold for a certain time → **Drowsiness Detected**
6. Triggers **alert sound**

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/selvan-01/drowsiness-detection-system.git
cd drowsiness-detection-system
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Download Model File

Download:
👉 shape_predictor_68_face_landmarks.dat

Place it inside:

```
models/
```

---

## ▶️ Run the Project

```bash
python src/main.py
```

Press **Q** to exit the application.

---

## ⚠️ Requirements

* Python 3.x
* Webcam
* Windows OS (for alarm sound using winsound)

---

## 📸 Output

* Detects face and eyes
* Displays alert: **"DROWSINESS DETECTED!"**
* Plays alarm sound

(Add your project screenshot in `assets/demo.png`)

---

## 🚀 Future Improvements

* 🔊 Voice alert instead of beep
* 📱 Mobile app integration
* 🌙 Night vision support
* 🚗 Integration with vehicle systems
* 📊 Drowsiness analytics dashboard

---

## 🤝 Contribution

Contributions are welcome! Feel free to fork this repo and improve the project.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**S. Senthamil Selvan**
AI & Tech Enthusiast | ML ENGINEERt | Developer

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
