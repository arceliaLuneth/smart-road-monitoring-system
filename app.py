import streamlit as st
from ultralytics import YOLO
import cv2
import tempfile
import pandas as pd
import os
from datetime import datetime



# PAGE CONFIG
st.set_page_config(
    page_title="Smart Road Monitoring System",
    layout="wide"
)

# LOAD CSS
def load_css():
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()


# TITLE
st.title("Smart Road Monitoring System")


# SIDEBAR
st.sidebar.title("Control Panel")

conf = st.sidebar.slider(
    "Confidence Threshold",
    0.1,
    1.0,
    0.5
)

frame_skip = st.sidebar.slider(
    "Frame Skip",
    1,
    30,
    10
)

uploaded_file = st.sidebar.file_uploader(
    "Upload Video",
    type=["mp4", "avi"]
)


# LOAD MODEL
model = YOLO("best.pt")


# METRIC CARDS
col1, col2, col3 = st.columns(3)

metric_total = col1.empty()
metric_status = col2.empty()
metric_conf = col3.empty()

metric_total.metric("Total Pothole", 0)
metric_status.metric("Status", "Waiting")
metric_conf.metric("Confidence", conf)


# PROCESS VIDEO
if uploaded_file is not None:

    metric_status.metric("Status", "Processing")

    # Save uploaded video temporarily
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    # Open video
    cap = cv2.VideoCapture(tfile.name)

    # Display frame
    stframe = st.empty()

    # Statistics
    total_detected = 0
    frame_count = 0

    # Progress bar
    progress_bar = st.progress(0)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    fps = cap.get(cv2.CAP_PROP_FPS)

    st.info(f"Video FPS: {fps:.2f}")

    # VIDEO LOOP
    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1

        # Skip frame for speed
        if frame_count % frame_skip != 0:
            continue

        # Resize frame
        frame = cv2.resize(frame, (640, 360))

        # YOLO Detection
        results = model(
            frame,
            conf=conf,
            verbose=False
        )

        pothole_count = len(results[0].boxes)

        total_detected += pothole_count

        # Draw result
        annotated = results[0].plot()

        # TOTAL TEXT
        cv2.putText(
            annotated,
            f"Total: {pothole_count}",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        # Convert color
        annotated = cv2.cvtColor(
            annotated,
            cv2.COLOR_BGR2RGB
        )

        # Show frame
        stframe.image(
            annotated,
            channels="RGB",
            use_container_width=True
        )

        # Update metric
        metric_total.metric(
            "Total Pothole",
            total_detected
        )

        # Update progress
        progress = int(
            (frame_count / total_frames) * 100
        )

        progress_bar.progress(progress)

     # FINISHED
    cap.release()

    metric_status.metric(
        "Status",
        "Finished"
    )

    st.success("Detection Finished")

    # SAVE HISTORY
    history = {
        "Tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Video": uploaded_file.name,
        "Total Pothole": total_detected
    }

    df = pd.DataFrame([history])

    df.to_csv(
        "history.csv",
        mode="a",
        header=not os.path.exists("history.csv"),
        index=False
    )

    st.divider()

st.subheader("Detection History")

if os.path.exists("history.csv"):

    history_df = pd.read_csv("history.csv")

    st.dataframe(
        history_df,
        use_container_width=True
    )