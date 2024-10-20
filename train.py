from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("facial-recognition.ico")
        
        
        title_lbl=Label(self.root, text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        top_img=Image.open(r"college_images\facialrecognition.png")
        top_img=top_img.resize((1530,325),Image.LANCZOS)
        self.photo_top_img=ImageTk.PhotoImage(top_img)
        
        first_lbl=Label(self.root,image=self.photo_top_img)
        first_lbl.place(x=0,y=55,width=1530,height=325)
        
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)
        
        bottom_img=Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        bottom_img=bottom_img.resize((1530,325),Image.LANCZOS)
        self.photo_bottom_img=ImageTk.PhotoImage(bottom_img)
        
        first_lbl=Label(self.root,image=self.photo_bottom_img)
        first_lbl.place(x=0,y=440,width=1530,height=325)
        
        
    def train_classifier(self):
        data_dir="data"
        path= [os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') #Gray Scale Image
            imageNP=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Traning",imageNP)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        
        # --------------------------Train Classifier And Save----------------------------------------
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets compeleted!!")
        
        
        
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()