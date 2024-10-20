from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("facial-recognition.ico")
        
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="blue")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        top_img = Image.open(r"college_images\face_detector1.jpg")
        top_img = top_img.resize((650, 700), Image.LANCZOS)
        self.photo_top_img = ImageTk.PhotoImage(top_img)
        
        first_lbl = Label(self.root, image=self.photo_top_img)
        first_lbl.place(x=0, y=55, width=650, height=700)
        
        bottom_img = Image.open(r"college_images\facial_recognition_system_identification_digital_id_security_scanning_think.jpg")
        bottom_img = bottom_img.resize((950, 700), Image.LANCZOS)
        self.photo_bottom_img = ImageTk.PhotoImage(bottom_img)
        
        second_lbl = Label(self.root, image=self.photo_bottom_img)
        second_lbl.place(x=650, y=55, width=950, height=700)
        
        b1_1 = Button(second_lbl, text="Face Recognition", command=self.face_recognition, cursor="hand2", font=("times new roman", 18, "bold"), bg="blue", fg="white")
        b1_1.place(x=365, y=620, width=200, height=40)
        
    # =================================Attendance===========================================   
    def  mark_attendance(self,i,r,n,c):
        with open("attendance_report/attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (c not in name_list) ):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{c},{dtString},{d1},Preset")
                
            
            
        
    def face_recognition(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
        
            coord = []
        
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100 * (1 - predict / 300))
            
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="9648",
                    database="face_reconiger"
                )
                my_cursor = conn.cursor()
            
                my_cursor.execute("select Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n) if n else "Unknown"
            
                my_cursor.execute("select Roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "Unknown"
                
                my_cursor.execute("select Course from student where Student_id=" + str(id))
                c = my_cursor.fetchone()
                c = "+".join(c) if c else "Unknown"
                
                my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i) if i else "Unknown"
            
                if confidence > 60:
                    cv2.putText(img, f"ID: {i}", (x+2, y-95), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Roll: {r}", (x+2, y-70), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {n}", (x+2, y-43), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Course: {c}", (x+2, y-15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.mark_attendance(i,r,n,c)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                
                coord = [x, y, w, h]
                
            return coord
    
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_capture = cv2.VideoCapture(0)
        window_name = "Welcome To Face Recognition"
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

        while True:
            ret, img = video_capture.read()
            img = recognize(img, clf, faceCascade)
            
            # Get the size of the window
            cv2.imshow(window_name, img)
            
            # Resize image to fit window
            # Resize image to fit window
            window_width = int(cv2.getWindowImageRect(window_name)[2])
            window_height = int(cv2.getWindowImageRect(window_name)[3])
            img_resized = cv2.resize(img, (window_width, window_height))
            cv2.imshow(window_name, img_resized)
            
            
        
            if cv2.waitKey(1)==13:  # Press 'Enter' to break the loop
                break
            
            if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
                break

        video_capture.release()
        cv2.destroyAllWindows()
        
        

if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition(root)
    root.mainloop()
