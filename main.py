import pyttsx3 #to speak
import speech_recognition as sr #takecommand from user
import datetime
import time
import os
import wikipedia
import webbrowser
import smtplib
import sys
import requests
from bs4 import BeautifulSoup
from requests import get
import random
import pyautogui

# **************************Gui start************************
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import pymysql
# *************************GUI packages***********************



# import pywhatkit as kit
# import cv2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# to convert voice into text (useer input)
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        r.energy_threshold = 2500
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        print(e)
        speak("Say that again please")
        return "None"
    return query



# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour < 12:
        speak(f"Good Morning, its {tt}")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon, its {tt}")
    else:
        speak(f"Good Evening, its {tt}")
    speak("I am Infono Sir, please tell me how may i help you")



# to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jkl2gmail.com', 'NV@123456')
    server.sendmail('jkl@gmail.com', to, content)
    server.close()


# *******************GUI CODE START*******************************
class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")


        # *****************Background Image*********************
        self.bg=ImageTk.PhotoImage(file="images/asdf.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)


        # *****************Left Image*********************
        self.left=ImageTk.PhotoImage(file="images/a1.png")
        left=Label(self.root,image=self.left).place(x=75,y=130,width=400,height=400)
     
        # *****************Right Image*********************
        self.right=ImageTk.PhotoImage(file="images/b1.jpg")
        right=Label(self.root,image=self.right).place(x=875,y=130,width=400,height=400)

        # *****************Login Frame*********************
        Frame1=Frame(self.root,bg="gray")
        Frame1.place(x=475,y=130,width=400,height=400)

        title=Label(Frame1,text="LOGIN FORM",font=("times new roman",20,"bold"),bg="gray",fg="firebrick").place(x=100,y=30)
        
        username=Label(Frame1,text="Username",font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=100,y=100)
        self.txt_username=Entry(Frame1,font=("times new roman",15),bg="lightgray")
        self.txt_username.place(x=100,y=130,width=250)

        password=Label(Frame1,text="Password",font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=100,y=170)
        self.txt_password=Entry(Frame1,font=("times new roman",15),show="*",bg="lightgray")
        self.txt_password.place(x=100,y=200,width=250)

        btn=Button(Frame1,text="Login Here",command=self.login,font=("times new roman",15,"bold"),bg="sandybrown",bd=0,cursor="hand2").place(x=100,y=250,width="250")

        right_btn=Button(self.root,text="Create new account",command=self.Register_window,font=("times new roman",15,"bold"),bg="sandybrown",bd=0,cursor="hand2").place(x=980,y=380,width="225")




    # ******************Working with database****************
    def Register_window(self):
        self.root.destroy()
        import signup
    
    def clear(self):
        self.txt_username.delete(0,END)
        self.txt_password.delete(0,END)
        



    def login(self):
        if self.txt_username.get()=="" or self.txt_password.get()=="": 
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="himanshu")
                cur=con.cursor()
                cur.execute("select * from details where username=%s and password=%s",(self.txt_username.get(),self.txt_password.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid username & password",parent=self.root)    
                    self.clear()
                else:
                    messagebox.showinfo("Success","Login Successful, Welcome",parent=self.root)
                    self.root.destroy()
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)


root=Tk()
obj=login_window(root)
root.mainloop()
# *******************GUI CODE END*******************************

def taskExecution():
    wish()
    while True:

        query = takecommand().lower()

        # logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)


        elif "where is" in query:
            data = data.split("")
            location = data[2]
            speak("Hold on Frank, I will show you where " + location + " is.")
            os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
        
        elif "open ms word" in query:
            wpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013"
            os.startfile(wpath)

        elif "open excel" in query:
            gpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel 2013"
            os.startfile(gpath)

        elif "open powerpoint" in query:
            bpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint 2013"
            os.startfile(bpath)

        elif "open typing master" in query:
            tpath = "C:\\Program Files (x86)\\TypingMaster10\\tmaster.exe"
            os.startfile(tpath)

        elif "open paint" in query:
            ppath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\paint"
            os.startfile(ppath)

        elif "open firefox" in query:
            wpath = "C:\\Program Files\\Mozilla Firefox\\firefox"
            os.startfile(wpath)

        elif "open microsoft edge" in query:
            zpath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft edge"
            os.startfile(zpath)

        elif "open chrome" in query:
            zpath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome"
            os.startfile(zpath)

        elif "open sublime text" in query:
            spath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\sublime text 3"
            os.startfile(spath)

        elif "open cmd" in query:
            os.system("start cmd")

        elif "hello infono" in query:
            speak("Hello Sir, please tell me how may i help you?")

        elif "how are you" in query:
            speak("I am Fine Sir, what about you?")

        elif "i am also fine" in query or "i am good" in query:
            speak("great Sir, please tell me how may i help you?")

        elif "who are you" in query:
            speak("My Name is Infono Sir, I am your personal Virtual Assistant")

        elif "who developed you" in query:
            speak("I am Infono Sir, and i am developed by Aryan Singh, Gautam paswan and Himanshu Arora by using python technology")

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP Address is : {ip}")

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        
        elif"open youtube and play any punjabi song" in query:
            webbrowser.open("https://www.youtube.com/watch?v=zsmcSN7sW0s")

        elif "open erp" in query:
            webbrowser.open("https://student.gehu.ac.in/")

        elif "open Graphic Era  University site" in query:
            webbrowser.open("https://www.gehu.ac.in/")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "temperature" in query:
            # speak("sir, which city temperature you want to know ?")
            temperature = "temperature in Dehradun"
            url = f"https://www.google.com/search?q={temperature}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"Current {temperature} is {temp}")

        # elif "wait" in query:
        #     speak("okay sir, i am waiting, you can call me anytime")

        # to play music
        elif "play music" in query:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            # print(songs)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        # to send email
        elif "send email to aryan" in query:
            try:
                speak("Sir, what should I say to aryan?")
                content = takecommand().lower()
                to = "arrusingh731@gmail.com"
                sendEmail(to, content)
                speak("email has been sent to aryan!")

            except Exception as e:
                print(e)
                speak("sorry sir, i not able to sent this email to aryan")

        elif "email to suraj" in query:
            try:
                speak("Sir, what should I say to suraj?")
                content = takecommand().lower()
                to = "surajdobhal25@gmail.com"
                sendEmail(to, content)
                speak("email has been sent to suraj!")

            except Exception as e:
                print(e)
                speak("sorry sir, i not able to sent this email to suraj")

        elif "send email to gautam" in query:
            try:
                speak("Sir, what should I say to gautam?")
                content = takecommand().lower()
                to = "paswaangkp506@gmail.com"
                sendEmail(to, content)
                speak("email has been sent to gautam!")

            except Exception as e:
                print(e)
                speak("sorry sir, i not able to sent this email to nitin")

        elif "email to abhishek" in query:
            try:
                speak("Sir, what should I say to abhishek?")
                content = takecommand().lower()
                to = "abhisheksemwal10@gmail.com"
                sendEmail(to, content)
                speak("email has been sent to abhishek!")

            except Exception as e:
                print(e)
                speak("sorry sir, i not able to sent this email to abhishek")

        elif "email to shubham" in query:
            try:
                speak("Sir, what should I say to shubham?")
                content = takecommand().lower()
                to = "dhananjaydhiman809@gmail.com"
                sendEmail(to, content)
                speak("email has been sent to shubham!")

            except Exception as e:
                print(e)
                speak("sorry sir, i not able to sent this email to abhishek")

        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

        elif "you can sleep now" in query or "sleep now" in query:
            speak("okay sir, i am going to sleep you can call me anytime.")
            break

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        #  to close some application-->
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close sublime text" in query:
            speak("okay sir, closing sublime text")
            os.system("taskkill /f /im sublime_text.exe")

        elif "close ms word" in query:
            speak("okay sir, closing ms word")
            os.system("taskkill /f /im WINWORD.exe")

        elif "close chrome" in query:
            speak("okay sir, closing chrome")
            os.system("taskkill /f /im chrome.exe")

        elif "close microsoft edge" in query:
            speak("okay sir, closing microsoft edge")
            os.system("taskkill /f /im msedge.exe")

        elif "close firefox" in query:
            speak("okay sir, closing firefox")
            os.system("taskkill /f /im firefox.exe")

        elif "close paint" in query:
            speak("okay sir, closing paint")
            os.system("taskkill /f /im mspaint.exe")

        elif "close typing master" in query:
            speak("okay sir, closing typing master")
            os.system("taskkill /f /im tmaster.exe")

        elif "close powerpoint" in query:
            speak("okay sir, closing powerpoint")
            os.system("taskkill /f /im POWERPNT.exe")

        elif "close excel" in query:
            speak("okay sir, closing excel")
            os.system("taskkill /f /im EXCEL.exe")
 
        elif "close code" in query:
            speak("okay sir, closing vs code")
            os.system("taskkill /f /im Code.exe")

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("taskkill /r /t 5")

        speak("sir, do you have any other work ?")

    # takecommand()
    # speak("hello sir, my name is infono  how may i help you sir ")



if __name__ == "__main__":
    while True:
        permession = takecommand()
        if "activate now" in permession:
            taskExecution()
        elif "goodbye" in permession:
            speak("thanks for using me sir, have a good day.")
            sys.exit()
    
    
