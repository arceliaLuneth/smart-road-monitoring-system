# Road Damage Detection System

An AI-powered road damage detection application that uses YOLO object detection to identify potholes from road inspection videos. The system provides an interactive monitoring dashboard built with Streamlit and supports video-based road condition analysis.

## Features

- Pothole detection using YOLO
- Video upload and processing
- Adjustable confidence threshold
- Detection statistics dashboard
- Detection history logging
- Custom dark-themed user interface
- Built with Streamlit and OpenCV

## Technologies Used

- Python
- YOLO (Ultralytics)
- Roboflow
- OpenCV
- Streamlit
- Pandas

## Project Structure

```text
road-damage-detection-system/
│
├── app.py
├── style.css
├── best.pt
├── README.md
│
├── SRMS_V1.1.pt
├── SRMS_V1.2.pt
└── SRMS_V1.3.pt
```

## How It Works

1. Upload a road inspection video.
2. The system extracts video frames.
3. YOLO detects potholes on each frame.
4. Detection results are visualized on the dashboard.
5. Detection statistics are recorded for monitoring purposes.

## Installation

```bash
git clone https://github.com/arceliaLuneth/road-damage-detection-system.git

cd road-damage-detection-system

pip install -r requirements.txt
```

## Run Application

```bash
streamlit run app.py
```

## Future Improvements

- Real-time camera monitoring
- GPS-based road damage mapping
- Road damage severity classification
- Cloud database integration
- Automated reporting system
