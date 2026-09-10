# 🌱 Smart Agriculture Platform

## 🌐 Live Deployment Links
*   **Frontend (Python Website):** [https://smart-agri-ui.onrender.com/](https://smart-agri-ui.onrender.com/)
*   **Backend (API):** [https://smart-agriculture-tdbe.onrender.com](https://smart-agriculture-tdbe.onrender.com)
*   **Database:** MongoDB Atlas

---

## 🚀 Tech Stack (Languages & Frameworks Used)
Ye project ek modern architecture par based hai:

### 1. Frontend (User Interface)
*   **Languages:** Python
*   **Framework:** Streamlit
*   **Kaam:** Kisaano ke liye live dashboard, forms aur interactive AI predictions dikhana.

### 2. Main Backend (API & Database)
*   **Languages:** JavaScript (Node.js)
*   **Framework:** Express.js
*   **Database:** MongoDB
*   **Kaam:** IoT sensors (ESP32/Arduino) ka data receive karna, database me save karna aur frontend ko live data bhejna.

### 3. AI / ML Integration
*   **Languages:** Python (Integrated within Streamlit Frontend)
*   **Kaam:** Crop (Fasal) ki recommendation dena aur paudho ki photo dekh kar bimari (Disease) detect karna.

---

## 📁 Project Folder Structure

```text
smart-agriculture/
│
├── python-frontend/        # Python Streamlit UI Project
│   ├── app.py              # Main UI, Dashboard & ML logic
│   ├── requirements.txt    # Python Dependencies
│   └── .python-version     # Render deployment version setting
│
├── backend/                # Node.js & Express API
│   ├── models/             # MongoDB Schemas
│   ├── routes/             # API Endpoints
│   ├── server.js           # Main Express Server File
│   └── package.json        # Backend Dependencies
│
├── task.md                 # Project Task Tracker
├── implementation_plan.md  # Architecture Plan
└── PROJECT_STRUCTURE.md    # This file
```
