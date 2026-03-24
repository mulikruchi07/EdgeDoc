import cv2

def capture_image():
    cap = cv2.VideoCapture(1)

    if not cap.isOpened():
        print("Camera not working")
        return None

    print("Align document... Capturing in 3 seconds")
    
    for i in range(3):
        ret, frame = cap.read()

    cv2.imwrite("captured.jpg", frame)
    cap.release()

    return "captured.jpg"