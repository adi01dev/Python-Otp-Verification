import smtplib
import random
import os
import math
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import font

def generate_otp():
    digit = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digit[math.floor(random.random() * 10)]   
    return OTP
    
def send_email(emailID, OTP):
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("adi01dev01@gmail.com","lpyk sphx smqf avpe")
    msg = OTP + " is your OTP. This is valid for 5 minutes."
    s.sendmail("&&&&&&&&&&&",emailID,msg)
    return True

class OTPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OTP Verification")
        self.root.geometry("800x500")
        self.root.resizable(False, False)
        # self.root.configure(bg="#181818")
        
        self.bg_image = ImageTk.PhotoImage(Image.open("D:/PROGRAMS/dabotics india/OTP Verification/Images/root_bg.jpg"))
        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_label.image = self.bg_image 
 
        self.panel = tk.Frame(root, width=320, height=420, bg="#1e1e1e", highlightthickness=1, highlightbackground="black")
        self.panel.place(x=240, y=40)

        self.panel_bg_image = ImageTk.PhotoImage(Image.open("D:/PROGRAMS/dabotics india/OTP Verification/Images/panel_bg.jpg"))
        self.panel_bg_label = tk.Label(self.panel, image=self.panel_bg_image)
        self.panel_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.panel_bg_label.image = self.panel_bg_image

        self.email_label = tk.Label(self.panel, text="Enter Your Email Here :", font=("Arial", 14, "bold"), bg="white", fg="black")
        self.email_label.place(x=50, y=110)
        
        self.email_entry = tk.Entry(self.panel, width=29, font=("times new roman", 12), bg="white", borderwidth=0, highlightthickness=1, highlightbackground="#000000")
        self.email_entry.place(x=45, y=145)
        
        self.send_otp_button = tk.Button(self.panel, text="Send OTP", width=10, height=1, bg="#400564", fg="white", font=("Arial", 11, "bold"), borderwidth=0, highlightthickness=1, command=self.send_otp)
        self.send_otp_button.place(x=115, y=190)
        
        self.otp_label = tk.Label(self.panel, text="Enter Your OTP Here :", font=("Arial", 14, "bold"), bg="white", fg="black")
        self.otp_label.place(x=55, y=250)
        
        self.otp_entry = tk.Entry(self.panel, width=29, font=("times new roman", 12), borderwidth=0, highlightthickness=1, highlightbackground="#000000")
        self.otp_entry.place(x=45, y=285)
        
        self.verify_button = tk.Button(self.panel, text="Verify OTP", width=10, height=1, bg="#400564", fg="white", font=("Arial", 11, "bold"), borderwidth=0, highlightthickness=0, command=self.verify_otp)
        self.verify_button.place(x=115, y=330)
        
        self.otp = None


    def send_otp(self):
        email = self.email_entry.get()
        if not email:
            messagebox.showwarning("Input Error", "Please enter your email.")
            return
        
        self.otp = generate_otp()
        success = send_email(email, self.otp)
        if success:
            messagebox.showinfo("Success", "OTP sent to your email.")
        else:
            messagebox.showerror("Error", "Failed to send OTP. Please try again.")

    def verify_otp(self):
        user_otp = self.otp_entry.get()
        if not user_otp:
            messagebox.showwarning("Input Error", "Please enter the OTP.")
            return
        
        if user_otp == self.otp:
            messagebox.showinfo("Success", "OTP verified successfully!")
        else:
            messagebox.showerror("Error", "Invalid OTP. Please try again.")


def main():
    
    root = tk.Tk()
    app = OTPApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()