import cv2
import numpy as np

def detect_potholes(frame):
    # Simple pothole detection: look for dark patches (mock)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)  # Dark areas
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    potholes = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if 100 < area < 10000:  # Size filter
            x, y, w, h = cv2.boundingRect(cnt)
            potholes.append((x, y, w, h))
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, 'Pothole', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    return potholes