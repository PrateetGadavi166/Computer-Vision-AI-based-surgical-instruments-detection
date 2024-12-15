from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import json
import os
import traceback

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_path = r"C:\Users\Asus\Desktop\FY\n_best.pt"
json_file_path = r"yolo-detection-ui\public\objectsData.json"  # Replace with the correct path to your JSON file

try:
    from ultralytics import YOLO
    model = YOLO(model_path)  # Load the YOLO model
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    raise HTTPException(status_code=500, detail="Failed to load YOLO model.")

# Function to load JSON data for object metadata
def load_object_metadata():
    if not os.path.exists(json_file_path):
        raise HTTPException(status_code=404, detail="JSON file not found.")
    
    with open(json_file_path, "r") as file:
        return json.load(file)

@app.post("/detect")
async def detect_objects(file: UploadFile = File(...)):
    try:
        # Log the uploaded file name
        print(f"File uploaded: {file.filename}")

        # Read and open the uploaded file as an image
        image = Image.open(file.file)
        print("Image successfully opened.")

        # Perform object detection
        results = model.predict(image)
        print("Detection results:", results)

        # Load object metadata from the JSON file
        metadata = load_object_metadata()

        # Parse detection results
        detected_objects = []
        for result in results:  # Iterate over results (usually a single image)
            if hasattr(result, "boxes"):  # Check if boxes are available
                for box in result.boxes:
                    if hasattr(box, "data"):  # Ensure data exists
                        for detection in box.data.tolist():
                            # Extract detected class names and confidence scores
                            class_id = int(detection[5])  # Class ID is at index 5
                            confidence = detection[4]  # Confidence score is at index 4
                            class_name = model.names[class_id]  # Map class ID to name
                            
                            # Get additional metadata from the JSON file if available
                            object_metadata = {}
                            for item in metadata:
                                if class_name in item:
                                    object_metadata = item[class_name]
                                    break

                            # Append the detected object with additional metadata (description and uses)
                            detected_objects.append({
                                "class_name": class_name,
                                "confidence": confidence,
                                "description": object_metadata.get("description", "No description available."),
                                "uses": object_metadata.get("uses", "No uses information available.")
                            })

        print("Parsed Detected Objects:", detected_objects)

        return {"objects": detected_objects}

    except Exception as e:
        print("Error during detection:", traceback.format_exc())
        raise HTTPException(status_code=500, detail="Error detecting objects.")
