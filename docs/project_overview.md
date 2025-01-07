Project Overview: Smart Glasses for the Visually Impaired

Objective

The project aims to develop smart glasses that assist visually impaired individuals by detecting objects (vehicles, people, and roads) using YOLOv8 and providing audio feedback to help them navigate safely.

Features

Object Detection: Detects vehicles, people, and roads.

Audio Feedback: Provides audio alerts based on detected objects.

Real-Time Processing: Utilizes Firebase for cloud processing to reduce the computational load on the ESP32 microcontroller.

Bluetooth Integration: Sends audio information to Bluetooth earphones.

Battery-Powered: Rechargeable battery for portable use.

Workflow

Image Capture: ESP32-CAM captures images.

Cloud Processing: Images are sent to Firebase for object detection using a pre-trained YOLOv8 model.

Audio Feedback: Firebase processes the detection results and sends the appropriate audio response back to the ESP32.

User Notification: ESP32 streams audio alerts to Bluetooth earphones.

Technologies Used

Hardware: ESP32-CAM, rechargeable battery, Bluetooth module.

Software: YOLOv8, Firebase, Python (for model training and cloud processing).

Programming Languages: C++ (ESP32 firmware), Python (cloud processing).