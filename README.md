# 🩺 Computer Vision AI-based Surgical Instruments Detection  

📁 **Project Overview**  
This project focuses on detecting **surgical instruments in medical images and videos** using **Computer Vision and AI**.  
The aim is to assist in medical workflow automation by accurately identifying instruments used during surgeries, enabling better analysis, documentation, and safety.  

---

🛠️ **Tech Stack**  
- **Backend:** FastAPI  
- **Frontend:** React + Tailwind CSS  
- **Authentication:** Firebase  
- **Model:** YOLO (Ultralytics) for object detection  
- **Image Processing:** OpenCV  

---

📊 **Dataset**  
- Custom dataset of **surgical tools** curated and preprocessed.  
- Dataset includes multiple classes of instruments used in surgical procedures.  

---

🚀 **Features**  
- 🔍 Detects and classifies surgical instruments in real-time.  
- 🌐 Web-based interface for interactive usage.  
- 🖼️ Supports both image and video input.  
- 📂 Stores and retrieves detection results.  
- 🔒 Secure login and access control with Firebase.  

---

⚙️ **How It Works**  
1. Upload an image or video containing surgical instruments.  
2. YOLO model processes the input and detects instruments.  
3. Detected objects are highlighted with bounding boxes and labels.  
4. Results are displayed on the frontend dashboard.  

---

📌 **Project Structure, Installation & Setup, and Acknowledgements**  

```bash
Computer-Vision-AI-based-surgical-instruments-detection
│── backend/ # FastAPI server
│── frontend/ # React + Tailwind frontend
│── models/ # YOLO model weights and configs
│── dataset/ # Surgical tools dataset
│── requirements.txt # Dependencies
│── README.md # Project documentation
```

**Clone the repo**  
```bash
git clone https://github.com/<your-username>/Computer-Vision-AI-based-surgical-instruments-detection.git
cd Computer-Vision-AI-based-surgical-instruments-detection
```

**Backend Setup (FastAPI)**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

**Frontend Setup (React + Tailwind)**
```bash
cd frontend
npm install
npm start
```

## Acknowledgements 🙏

- 🟢 **Ultralytics YOLO** – for object detection  
- 🎥 **OpenCV** – for image processing  
- 🔐 **Firebase** – for authentication  
- 🌐 **FastAPI + React** – for web application


