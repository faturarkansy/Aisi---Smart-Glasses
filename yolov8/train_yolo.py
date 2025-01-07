from ultralytics import YOLO

# Load model
model = YOLO('yolov8s.pt')

# Train model
model.train(data='dataset.yaml', epochs=50, imgsz=640)

# Save model
model.save('best_model.pt')
