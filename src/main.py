import cv2
import numpy as np
from vehicle_detection import detect_vehicles
from accident_detection import detect_accidents
from pothole_detection import detect_potholes
from number_plate_recognition import recognize_plates

try:
    import easyocr
except ImportError:
    easyocr = None

def main():
    # Initialize OCR reader
    reader = easyocr.Reader(['en']) if easyocr else None
    if reader is None:
        print("EasyOCR is not installed; number plate recognition is disabled.")

    # Choose input: 0 for webcam, or path to video file
    cap = cv2.VideoCapture(0)  # Change to 'video.mp4' for file

    vehicle_count = 0
    accident_alerts = 0
    pothole_alerts = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect vehicles
        vehicles, frame = detect_vehicles(frame)
        vehicle_count += len(vehicles)

        # Detect accidents (basic: stopped vehicles)
        accidents = detect_accidents(frame, vehicles)
        if accidents:
            accident_alerts += 1
            print("Accident detected!")

        # Detect potholes (simple threshold)
        potholes = detect_potholes(frame)
        if potholes:
            pothole_alerts += 1
            print("Pothole detected!")

        # Recognize number plates
        plates = recognize_plates(frame, reader)
        for plate in plates:
            print(f"Plate: {plate}")

        # Display results
        cv2.putText(frame, f'Vehicles: {vehicle_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f'Accidents: {accident_alerts}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame, f'Potholes: {pothole_alerts}', (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.imshow('Road Monitoring', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
