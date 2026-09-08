# 🌱 Smart Agriculture Platform

## 🚀 Tech Stack (Languages & Frameworks Used)
Ye project ek modern microservices architecture par based hai, jisme 3 alag-alag technologies ka use kiya gaya hai:

### 1. Frontend (User Interface)
*   **Languages:** JavaScript, HTML, CSS
*   **Framework:** React.js (Vite)
*   **Kaam:** Kisaano ke liye dashboard, form aur graphs dikhana.

### 2. Main Backend (API & Database)
*   **Languages:** JavaScript (Node.js)
*   **Framework:** Express.js
*   **Database:** MongoDB
*   **Kaam:** IoT sensors ka data receive karna, database me save karna aur frontend ko data bhejna.

### 3. AI / ML Service (Machine Learning)
*   **Languages:** Python
*   **Framework:** FastAPI
*   **Libraries:** Scikit-learn, Uvicorn, Pydantic
*   **Kaam:** Crop (Fasal) ki recommendation dena aur image processing ke through paudho ki bimari (Disease) detect karna.

---

## 📁 Project Folder Structure

```text
smart-agriculture/
│
├── frontend/               # React.js UI Project
│   ├── src/
│   │   ├── components/     # Dashboard, CropPredictor, DiseaseDetector, MarketPrices
│   │   ├── App.jsx         # Main React Component
│   │   ├── App.css         # Styling and UI Colors
│   │   └── main.jsx        # React Entry Point
│   ├── package.json        # Frontend Dependencies
│   └── vite.config.js      # Vite Configuration
│
├── backend/                # Node.js & Express API
│   ├── models/             # MongoDB Schemas (User.js, SensorData.js, Crop.js)
│   ├── routes/             # API Endpoints (userRoutes.js, iotRoutes.js)
│   ├── server.js           # Main Express Server File
│   └── package.json        # Backend Dependencies
│
├── ml-service/             # Python FastAPI Machine Learning
│   ├── app.py              # Main Python API Server (Endpoints for ML)
│   └── requirements.txt    # Python Dependencies
│
├── task.md                 # Project Task Tracker
├── implementation_plan.md  # Original Project Architecture Plan
└── PROJECT_STRUCTURE.md    # This file
```
