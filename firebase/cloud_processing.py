import firebase_admin
from firebase_admin import credentials, db, storage
from ultralytics import YOLO
import base64
import cv2
import numpy as np

# Initialize Firebase
cred = credentials.Certificate("firebase_credentials.json")  # Path ke file credentials.json
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project.firebaseio.com/',
    'storageBucket': 'your-project.appspot.com'
})

# Load YOLO model
model = YOLO('best_model.pt')  # Model YOLO yang sudah dilatih

# Firebase references
db_ref = db.reference('/images')
response_ref = db.reference('/response')
bucket = storage.bucket()

def decode_image(base64_string):
    """Mengubah string base64 menjadi gambar OpenCV."""
    img_data = base64.b64decode(base64_string)
    np_arr = np.frombuffer(img_data, np.uint8)
    return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

def process_images():
    """Proses gambar yang diunggah dari ESP32."""
    images = db_ref.get()
    if images:
        for key, base64_image in images.items():
            # Decode gambar
            img = decode_image(base64_image)

            # Deteksi objek menggunakan YOLO
            results = model(img)

            # Analisis hasil deteksi
            largest_box = None
            largest_area = 0
            for box in results.boxes:
                if box.conf > 0.5:  # Confidence threshold
                    area = (box.xyxy[2] - box.xyxy[0]) * (box.xyxy[3] - box.xyxy[1])
                    if area > largest_area:
                        largest_area = area
                        largest_box = box

            # Tentukan respons berdasarkan kategori objek
            if largest_box:
                category = largest_box.name
                if category == 'kendaraan':
                    response_ref.set("Ada kendaraan tepat di depan anda")
                elif category == 'manusia':
                    response_ref.set("Ada manusia dekat dengan anda")
                elif category == 'jalan':
                    response_ref.set("Anda berada di jalan")
            else:
                response_ref.set("Tidak ada objek terdeteksi")

            # Hapus gambar dari Firebase setelah diproses
            db_ref.child(key).delete()

if __name__ == "__main__":
    while True:
        process_images()
