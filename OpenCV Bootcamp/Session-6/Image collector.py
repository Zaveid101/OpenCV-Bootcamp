import os
import cv2
import time
import uuid

IMAGE_PATH = 'CollectedImages'

labels = ['Hello', ' Yes', ' No', 'Thanks', 'IloveYou', 'Please']

num_of_images = 10

for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path, exist_ok=True)
    cap = cv2.VideoCapture(0)
    print(f"Collecting images for {label}")
    time.sleep(10)

    for img_num in range(num_of_images):
        success, frame = cap.read()
        image_name = os.path.join(f"{label}_{str(uuid.uuid1())}.jpg")
        cv2.imwrite(os.path.join(img_path, image_name), frame)
        cv2.imshow('frame' , frame)
        time.sleep(2)
        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()