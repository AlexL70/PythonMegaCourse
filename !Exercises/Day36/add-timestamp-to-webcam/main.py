import cv2
import datetime
import streamlit as st

CAMERA_STARTED = "__camera_started__"
if CAMERA_STARTED not in st.session_state:
    st.session_state[CAMERA_STARTED] = False
    started = False
else:
    started = st.session_state[CAMERA_STARTED]

st.title("Motion Detector")
if started:
    start = st.button("Stop camera")
else:
    start = st.button("Start camera")

if start:
    started = not started
    st.session_state[CAMERA_STARTED] = started
    st.rerun()
else:
    streamlit_image = st.image([])
    camera = None
    if started:
        camera = cv2.VideoCapture(4)

        while True:
            if not started:
                break
            try:
                check, frame = camera.read()
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                now = datetime.datetime.now()
                day_of_week = now.strftime("%A")
                time = now.strftime("%H:%M:%S")
                cv2.putText(img=frame, text=day_of_week, org=(50, 50), fontFace=cv2.FONT_HERSHEY_PLAIN,
                            fontScale=2, color=(200, 200, 255), thickness=2, lineType=cv2.LINE_AA)
                cv2.putText(img=frame, text=time, org=(50, 80), fontFace=cv2.FONT_HERSHEY_PLAIN,
                            fontScale=2, color=(255, 50, 50), thickness=2, lineType=cv2.LINE_AA)
                streamlit_image.image(frame)
            except Exception:
                pass
    else:
        if camera is not None:
            camera.release()
            camera = None
            cv2.destroyAllWindows()
