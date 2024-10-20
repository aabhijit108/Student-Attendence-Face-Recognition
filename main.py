from tkinter import *
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime





class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("facial-recognition.ico")
        
        #First Image
        img=Image.open(r"college_images\BestFacialRecognition.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        
        first_lbl=Label(self.root,image=self.photoimg)
        first_lbl.place(x=0,y=0,width=500,height=130)
        
        #Second Image
        img1=Image.open(r"college_images\facialrecognition.png")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        
        first_lbl=Label(self.root,image=self.photoimg1)
        first_lbl.place(x=500,y=0,width=500,height=130)
        
        #Third Image
        img2=Image.open(r"college_images\facialrecognition.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        
        first_lbl=Label(self.root,image=self.photoimg2)
        first_lbl.place(x=1000,y=0,width=550,height=130)
        
        # Background Image
        imgb=Image.open(r"college_images\bgimg.jpg")
        imgb=imgb.resize((1530,710),Image.LANCZOS)
        self.photoimgb=ImageTk.PhotoImage(imgb)
        
        
        bg_img=Label(self.root,image=self.photoimgb)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        # =========================================Time=============================================
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
            
        lbl=Label(title_lbl,font=("times new roman",14,"bold"),background="white",foreground="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        
        # Student Button
        imgsbtn=Image.open(r"college_images\student.jpg")
        imgsbtn=imgsbtn.resize((220,220),Image.LANCZOS)
        self.photoimgsbtn=ImageTk.PhotoImage(imgsbtn)
        
        b1=Button(bg_img,image=self.photoimgsbtn,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)
        
        #Face Detect Button
        imgfbtn=Image.open(r"college_images\face_detector1.jpg")
        imgfbtn=imgfbtn.resize((220,220),Image.LANCZOS)
        self.photoimgfbtn=ImageTk.PhotoImage(imgfbtn)
        
        b1=Button(bg_img,image=self.photoimgfbtn,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)
        
        
        
        #Face Attendance Button
        imgabtn=Image.open(r"college_images\attendance.jpg")
        imgabtn=imgabtn.resize((220,220),Image.LANCZOS)
        self.photoimgabtn=ImageTk.PhotoImage(imgabtn)
        
        b1=Button(bg_img,image=self.photoimgabtn,cursor="hand2",command=self.attendence_data)
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendence_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)
        
        
        
        #Help  Attendance Button
        imghbtn=Image.open(r"college_images\help.jpg")
        imghbtn=imghbtn.resize((220,220),Image.LANCZOS)
        self.photoimghbtn=ImageTk.PhotoImage(imghbtn)
        
        b1=Button(bg_img,image=self.photoimghbtn,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Help DESK",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        
        #Face Train Button
        imgtbtn=Image.open(r"college_images\Train.jpg")
        imgtbtn=imgtbtn.resize((220,220),Image.LANCZOS)
        self.photoimgtbtn=ImageTk.PhotoImage(imgtbtn)
        
        b1=Button(bg_img,image=self.photoimgtbtn,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)
        
        
        #Face Photos Button
        imgpbtn=Image.open(r"college_images\opencv_face_reco_more_data.jpg")
        imgpbtn=imgpbtn.resize((220,220),Image.LANCZOS)
        self.photoimgpbtn=ImageTk.PhotoImage(imgpbtn)
        
        b1=Button(bg_img,image=self.photoimgpbtn,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)
        
        
        
        #Developer Face Button
        imgdevbtn=Image.open(r"college_images\Team-Management-Software-Development.jpg")
        imgdevbtn=imgdevbtn.resize((220,220),Image.LANCZOS)
        self.photoimgdevbtn=ImageTk.PhotoImage(imgdevbtn)
        
        b1=Button(bg_img,image=self.photoimgdevbtn,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)
        
        
        
        #Exit Face Button
        imgebtn=Image.open(r"college_images\exit.jpg")
        imgebtn=imgebtn.resize((220,220),Image.LANCZOS)
        self.photoimgebtn=ImageTk.PhotoImage(imgebtn)
        
        b1=Button(bg_img,image=self.photoimgebtn,cursor="hand2",command=self.exit_button)
        b1.place(x=1100,y=380,width=220,height=220)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.exit_button,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)
        
    # ------------------------------------open image----------------------------------------    
    def open_img(self):
        os.startfile("data")
        
    def exit_button(self):
        self.exit_button=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this Applicaton",parent=self.root)
        if self.exit_button >0:
            self.root.destroy()
        else:
            return
        
        
    # -----------------------------------Function Buttons---------------------------------
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
    
        
        
        
        
        
        

if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition_System(root)
    root.mainloop()