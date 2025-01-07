YOLOv8 Training Guide

Step 1: Install YOLOv8

Install Python (version 3.8 or higher).

Install YOLOv8 using the following command:

pip install ultralytics

Step 2: Prepare Dataset

Collect Images: Gather images for the categories (vehicles, people, roads).

Label Images: Use labeling tools like LabelImg or Roboflow.

Organize Dataset:

dataset/
├── images/
│   ├── train/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   ├── ...
│   └── val/
│       ├── image1.jpg
│       ├── image2.jpg
│       ├── ...
├── labels/
    ├── train/
    │   ├── image1.txt
    ├── val/
        ├── image1.txt

Create dataset.yaml:

train: dataset/images/train
val: dataset/images/val
nc: 3
names:
  0: kendaraan
  1: manusia
  2: jalan

Step 3: Train Model

Run the following command to start training:

yolo train data=dataset.yaml model=yolov8n.pt epochs=50 imgsz=640

Monitor training logs for accuracy and loss metrics.

Step 4: Save the Best Model

After training, the best model will be saved as:

runs/detect/train/weights/best.pt

Step 5: Test the Model

Test the model on an image:

yolo predict model=runs/detect/train/weights/best.pt source=path_to_image.jpg

Test the model on a video:

yolo predict model=runs/detect/train/weights/best.pt source=path_to_video.mp4

Step 6: Deploy the Model

Move best.pt to the project folder and integrate it into your processing pipeline.