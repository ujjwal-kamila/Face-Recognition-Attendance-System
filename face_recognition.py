# face_recognition.py
# The core real-time face recognition engine.

import cv2
import sqlite3
import os
import pickle
from datetime import datetime
from config import DB_PATH, HAAR_CASCADE_PATH, MODEL_PATH, RECOGNITION_CONFIDENCE_THRESHOLD, MODELS_DIR

class FaceRecognitionSystem:
    def __init__(self, update_callback):
        self.is_running = False
        self.update_callback = update_callback

    def start_recognition(self):
        self.is_running = True
        
        face_cascade = cv2.CascadeClassifier(HAAR_CASCADE_PATH)
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(MODEL_PATH)
        
        # Load the student ID to numerical label mapping
        id_map_path = os.path.join(MODELS_DIR, 'id_map.pkl')
        with open(id_map_path, 'rb') as f:
            id_map = pickle.load(f)
        # Create a reverse map from numerical label to student ID
        rev_id_map = {v: k for k, v in id_map.items()}

        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not open video stream.")
            self.is_running = False
            return

        while self.is_running:
            ret, frame = cap.read()
            if not ret:
                break
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(50, 50))

            for (x, y, w, h) in faces:
                roi_gray = gray[y:y+h, x:x+w]
                
                numeric_id, confidence = recognizer.predict(roi_gray)
                
                student_id = "Unknown"
                student_name = "Unknown"
                
                if confidence < RECOGNITION_CONFIDENCE_THRESHOLD:
                    student_id = rev_id_map.get(numeric_id, "Unknown")
                    student_name = self.get_student_name(student_id)
                    
                    if student_name!= "Unknown":
                        self.mark_attendance(student_id, student_name)
                
                # Draw rectangle and text
                color = (0, 255, 0) if student_id!= "Unknown" else (0, 0, 255)
                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
                display_text = f"{student_id} ({student_name})"
                cv2.putText(frame, display_text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

            cv2.imshow("Face Recognition - Press 'q' to stop", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
        self.is_running = False

    def stop_recognition(self):
        self.is_running = False

    def get_student_name(self, student_id):
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM students WHERE student_id=?", (student_id,))
            result = cursor.fetchone()
            conn.close()
            return result if result else "Unknown"
        except Exception:
            return "Unknown"

    def mark_attendance(self, student_id, student_name):
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            
            now = datetime.now()
            date_str = now.strftime("%Y-%m-%d")
            time_str = now.strftime("%H:%M:%S")
            
            # Use INSERT OR IGNORE to prevent duplicate entries for the same student on the same day
            cursor.execute("""
                INSERT OR IGNORE INTO attendance (student_id, name, date, time, status)
                VALUES (?,?,?,?,?)
            """, (student_id, student_name, date_str, time_str, "Present"))
            
            conn.commit()
            if cursor.rowcount > 0: # If a row was inserted
                print(f"Attendance marked for {student_name} ({student_id})")
                # Use a thread-safe way to update GUI if needed, e.g., via a queue
                # For simplicity, directly calling the callback here
                self.update_callback()
            conn.close()
        except Exception as e:
            print(f"Database error while marking attendance: {e}")