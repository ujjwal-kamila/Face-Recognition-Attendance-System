# data_collection.py
# Handles capturing and saving photo samples for a given student.

import cv2
import os
from tkinter import messagebox
from config import FACES_DIR, HAAR_CASCADE_PATH

def collect_samples(student_id):
    """
    Captures 100 face samples for a given student ID using the webcam.
    """
    if not os.path.exists(HAAR_CASCADE_PATH):
        messagebox.showerror("Error", "Haar Cascade file not found!")
        return

    face_classifier = cv2.CascadeClassifier(HAAR_CASCADE_PATH)
    
    def face_cropped(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        
        if len(faces) == 0:
            return None
        
        # Assume only one face for sample collection
        (x, y, w, h) = faces
        cropped_face = img[y:y+h, x:x+w]
        return cropped_face

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not open webcam.")
        return

    img_id = 0
    student_dir = os.path.join(FACES_DIR, student_id)
    os.makedirs(student_dir, exist_ok=True)

    messagebox.showinfo("Info", "Starting photo sample collection. Look at the camera and press 'Enter' to start. Press 'q' to quit.", parent=None)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if face_cropped(frame) is not None:
            img_id += 1
            face = cv2.resize(face_cropped(frame), (450, 450))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            
            file_path = os.path.join(student_dir, f"{student_id}.{img_id}.jpg")
            cv2.imwrite(file_path, face)
            
            cv2.putText(frame, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("Collecting Samples", frame)

        if cv2.waitKey(1) == 13 or img_id == 100: # 13 is Enter key
            break

    cap.release()
    cv2.destroyAllWindows()
    messagebox.showinfo("Result", "Photo sample collection completed!", parent=None)