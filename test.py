from ultralytics import YOLO
import cv2
import time

# Load the trained model
model = YOLO(r'C:\Users\Asus\Desktop\FY\m_best.pt')  # Path to the best model weights

# Open the webcam (use 0 for the default webcam, or change if you have multiple cameras)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the webcam.")
    exit()

while True:
    # Capture frame-by-frame from the webcam
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to capture frame from webcam.")
        break
    
    # Perform detection on the current frame
    results = model(frame)

    # Iterate over the results and plot each result
    for result in results:
        # Get the plotted image with detections
        plotted_frame = result.plot()

        # Show the detection result in a window
        cv2.imshow("YOLO Detection", plotted_frame)

        # Print the number of detected objects
        print(f"Detected {len(result)} objects in this frame.")

    # Introduce a 1-second delay between each frame
    # time.sleep(1)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()