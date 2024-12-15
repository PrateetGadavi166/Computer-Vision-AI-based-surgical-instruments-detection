from ultralytics import YOLO
import torch

def main():
    # Load YOLOv8 model
    model = YOLO('yolov8n.pt')  # Use a smaller model if needed

    # Clear CUDA cache before training
    torch.cuda.empty_cache()

    # Train the model with a smaller batch size and possibly smaller image size
    model.train(data='data.yaml', epochs=100, imgsz=640, batch=22, workers = 10, lr0 = 0.02)

    # After training, you can save the best weights
    model.export(format='onnx')  # Optional: Export to other formats like ONNX

if __name__ == '_main_':
    main()