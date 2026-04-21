import cv2
import numpy as np

def detect_accidents(frame, vehicles):
    # Simple accident detection: if vehicles are very close or stopped
    accidents = []
    for i, veh1 in enumerate(vehicles):
        for j, veh2 in enumerate(vehicles):
            if i != j:
                x1, y1, w1, h1 = veh1
                x2, y2, w2, h2 = veh2
                # Check overlap or proximity
                if abs(x1 - x2) < 50 and abs(y1 - y2) < 50:  # Arbitrary threshold
                    accidents.append((veh1, veh2))
                    cv2.putText(frame, 'Accident!', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    return accidents