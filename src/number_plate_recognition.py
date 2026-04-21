import cv2

def recognize_plates(frame, reader):
    if reader is None:
        return []

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect text
    results = reader.readtext(gray)

    plates = []
    for (bbox, text, confidence) in results:
        if confidence > 0.5 and len(text) > 3:  # Filter likely plates
            plates.append(text)
            # Draw bbox
            (tl, tr, br, bl) = bbox
            tl = (int(tl[0]), int(tl[1]))
            br = (int(br[0]), int(br[1]))
            cv2.rectangle(frame, tl, br, (0, 255, 255), 2)
            cv2.putText(frame, text, tl, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
    return plates
