from ultralytics import YOLO

# Load the YOLO model
model = YOLO('m_best.pt')

# Perform validation on the dataset
metrics = model.val(data='data.yaml', imgsz=640, batch=16)

# Print mAP and other evaluation metrics
print(f"mAP@0.5: {metrics.box.map50:.4f}")
print(f"mAP@0.5:0.95: {metrics.box.map:.4f}")
print(f"Precision: {metrics.box.mp:.4f}")
print(f"Recall: {metrics.box.mr:.4f}")