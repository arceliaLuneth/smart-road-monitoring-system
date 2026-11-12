<div align="center">

# Smart Road Monitoring System (SRMS)
### AI-powered pothole detection and road condition analysis dashboard built with YOLO, OpenCV, and Streamlit.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Detection-YOLO%20(Ultralytics)-1D4ED8?style=flat-square" alt="YOLO">
  <img src="https://img.shields.io/badge/Vision-OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/Dashboard-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/License-MIT-10B981?style=flat-square&logo=open-source-initiative&logoColor=white" alt="License">
</p>

</div>

---

## About The Project

**Smart Road Monitoring System (SRMS)** is a computer vision application designed to automate road surface inspection by detecting potholes from video footage. Trained on custom datasets curated via **Roboflow** and powered by **YOLO (Ultralytics)**, the system processes road inspection videos frame by frame and presents real-time visual detections alongside analytical summaries through a custom dark-themed **Streamlit** dashboard.

---

## Key Features

* **Automated Pothole Detection:** Identifies road potholes across video frames using custom-trained YOLO weights (`best.pt` and iterative checkpoints `SRMS_V1.1` – `SRMS_V1.3`).
* **Video Upload & Frame Processing:** Supports direct road inspection video uploads with automated frame extraction via OpenCV.
* **Adjustable Confidence Threshold:** Allows dynamic tuning of detection sensitivity directly from the dashboard interface.
* **Detection Statistics Dashboard:** Aggregates and visualizes detection counts and key metrics for road condition assessment.
* **Detection History Logging:** Records detection events and session outputs using Pandas for structured monitoring.
* **Custom Dark-Themed UI:** Styled with custom CSS (`style.css`) for a clean, low-glare monitoring interface.

---

## Tech Stack

| Component | Technology |
| :--- | :--- |
| **Core Language** | Python (69%) |
| **UI Styling** | Custom CSS (31%) |
| **Object Detection** | YOLO (Ultralytics) |
| **Dataset Management** | Roboflow |
| **Video & Frame Processing** | OpenCV |
| **Web Dashboard** | Streamlit |
| **Data & History Logging** | Pandas |

---

## System Workflow

1. **Video Input:** Upload a recorded road inspection video through the Streamlit interface.
2. **Frame Extraction:** OpenCV decodes the video stream into sequential frames.
3. **Model Inference:** The YOLO model evaluates each frame against the configured confidence threshold to localize potholes.
4. **Visual Rendering:** Bounding boxes and confidence scores are overlaid onto the processed frames in real time.
5. **Metrics & Logging:** Detection statistics are compiled and logged for road maintenance monitoring.

---

## Repository Structure

```text
smart-road-monitoring-system/
├── app.py              # Main Streamlit dashboard and YOLO inference pipeline
├── style.css           # Custom dark-theme UI styling
├── best.pt             # Primary production YOLO model weights
├── SRMS_V1.1.pt        # Iterative model checkpoint v1.1
├── SRMS_V1.2.pt        # Iterative model checkpoint v1.2
├── SRMS_V1.3.pt        # Iterative model checkpoint v1.3
├── .gitignore          # Git ignore configuration
├── LICENSE             # MIT License
└── README.md           # Project documentation
```

---

## Getting Started

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/arceliaLuneth/smart-road-monitoring-system.git](https://github.com/arceliaLuneth/smart-road-monitoring-system.git)
   cd smart-road-monitoring-system
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux / macOS
   source venv/bin/activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install ultralytics streamlit opencv-python pandas
   ```

### Running the Application

Start the Streamlit monitoring dashboard:

```bash
streamlit run app.py
```

---

## Future Roadmap

Planned upgrades to expand SRMS from offline video analysis into a comprehensive road infrastructure monitoring platform:

* [ ] **Real-Time Live Camera Monitoring:** Support direct webcam, dashcam, or RTSP video streams for live on-vehicle road inspection.
* [ ] **GPS-Based Road Damage Mapping:** Synchronize video timestamps with GPS telemetry to pin detected potholes onto an interactive geographic map.
* [ ] **Road Damage Severity Classification:** Classify defects by bounding-box dimensions and confidence metrics into low, moderate, and severe maintenance priorities.
* [ ] **Multi-Class Defect Expansion:** Expand dataset training on Roboflow to detect longitudinal cracks, alligator cracking, and faded road markings alongside potholes.
* [ ] **Cloud Database Integration:** Persist inspection logs, frame snapshots, and geolocation records in a centralized cloud database (e.g., PostgreSQL or Firebase).
* [ ] **Automated Maintenance Reporting:** Generate downloadable PDF/CSV inspection reports complete with timestamped visual evidence and summary statistics.

---

## License

Distributed under the **MIT License**. See `LICENSE` for more information.
