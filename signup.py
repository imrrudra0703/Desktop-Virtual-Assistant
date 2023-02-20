from tkinter import*  
from tkinter import messagebox
from PIL import Image,ImageTk 
import pymysql     

class Register_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Signup Window")
        self.root.geometry("1350x700+0+0")

    # *********Background Image*********
        self.bg=ImageTk.PhotoImage(file="images/bgg.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

    # *****************Left Image********
        self.left=ImageTk.PhotoImage(file="images/left_image.png")
        left=Label(self.root,image=self.left).place(x=350,y=0,width=350,height=300)

    # *****************Right Image********
        self.right=ImageTk.PhotoImage(file="images/right_image.png")
        right=Label(self.root,image=self.right).place(x=700,y=0,width=350,height=300)

    # **********Register Frame********
        Frame1=Frame(self.root,bg="gray")
        Frame1.place(x=350,y=300,width=700,height=400)

        title=Label(Frame1,text="REGISTRATION FORM",font=("dancing script",20,"bold"),bg="gray",fg="firebrick").place(x=100,y=15)

        f_name=Label(Frame1,text="First Name",font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=100,y=70)
        self.txt_f_name=Entry(Frame1,font=("times new roman",15),bg="lightgray")
        self.txt_f_name.place(x=100,y=100,width=250)

        l_name=Label(Frame1,text="Last Name",font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=370,y=70)
        self.txt_l_name=Entry(Frame1,font=("times new roman",15),bg="lightgray")
        self.txt_l_name.place(x=370,y=100,width=250)
        
        username=Label(Frame1,text="Username",font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=100,y=150)
        self.txt_username=Entry(Frame1,font=("times new roman",15),bg="lightgray")
        self.txt_username.place(x=100,y=180,width=250)

        email=Label(Frame1,text="Email",font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=370,y=150)
        self.txt_email=Entry(Frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=180,width=250)

        password=Label(Frame1,text="Password",font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=100,y=230)
        self.txt_password=Entry(Frame1,font=("times new roman",15),show="*",bg="lightgray")
        self.txt_password.place(x=100,y=260,width=250)

        con_password=Label(Frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=370,y=230)
        self.txt_con_password=Entry(Frame1,font=("times new roman",15),show="*",bg="lightgray")
        self.txt_con_password.place(x=370,y=260,width=250)

        self.var_check=IntVar()
        check=Checkbutton(Frame1,text="I Agree the terms & Conditions",variable=self.var_check,onvalue=1,offvalue=0,bg="gray", font=("times new roman",12)).place(x=100,y=300)

        self.btn=Button(Frame1,text="Register Here",font=("times new roman",15,"bold"),bg="sandybrown",bd=0,cursor="hand2",command=self.register).place(x=200,y=350,width="250")
       
        left_btn=Button(self.root,text="Sign in",command=self.login_window, font=("times new roman",15,"bold"),bg="gold",bd=0,cursor="hand2").place(x=750,y=200,width="200")


    

    # *********working with database*******
    
    def login_window(self):
        self.root.destroy()
        import main
    
    def clear(self):
        self.txt_f_name.delete(0,END)
        self.txt_l_name.delete(0,END)
        self.txt_username.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_con_password.delete(0,END)
        
    
    
    def register(self):
        if self.txt_f_name.get()=="" or self.txt_l_name.get()=="" or self.txt_username.get()=="" or self.txt_email.get()=="" or self.txt_password.get()=="" or self.txt_con_password.get()=="": 
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_con_password.get():
            messagebox.showerror("Error","Password and Confirm Password should be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our terms and condition",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="himanshu")
                cur=con.cursor()
                cur.execute("select * from details where emails=%s", self.txt_email.get())
                row=cur.fetchone()
                # print(row)
                if row!=None:
                    messagebox.showinfo("Success","User Already Exist, please try with another email",parent=self.root)
                else:
                    cur.execute("insert into details (f_name, l_name, username, emails, password) values(%s,%s,%s,%s,%s)",
                            (self.txt_f_name.get(),
                             self.txt_l_name.get(),
                             self.txt_username.get(),
                             self.txt_email.get(),
                             self.txt_password.get()
                             ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registration Successful",parent=self.root)
                    self.root.destroy()
                    import main
                    self.clear()


            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)



root=Tk()
obj=Register_window(root)
root.mainloop()
from tkinter import*  
from tkinter import messagebox
from PIL import Image,ImageTk 
import pymysql     

class Register_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Signup Window")
        self.root.geometry("1350x700+0+0")

    # *********Background Image*********
        self.bg=ImageTk.PhotoImage(file="images/bgg.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

    # *****************Left Image********
        self.left=ImageTk.PhotoImage(file="images/left_image.png")
        left=Label(self.root,image=self.left).place(x=350,y=0,width=350,height=300)

    # *****************Right Image********
        self.right=ImageTk.PhotoImage(file="images/right_image.png")
        right=Label(self.root,image=self.right).place(x=700,y=0,width=350,height=300)

    # **********Register Frame********
        Frame1=Frame(self.root,bg="gray")
        Frame1.place(x=350,y=300,width=700,height=400)

        title=Label(Frame1,text="REGISTRATION FORM",font=("dancing script",20,"bold"),bg="gray",fg="firebrick").place(x=100,y=15)

        f_name=Label(Frame1,text="First Name",font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=100,y=70)
        self.txt_f_name=Entry(Frame1,font=("times new roman",15),bg="lightgray")
        self.txt_f_name.place(x=100,y=100,width=250)

        l_name=Label(Frame1,text="Last Name",font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=370,y=70)
        self.txt_l_name=Entry(Frame1,font=("times new roman",15),bg="lightgray")
        self.txt_l_name.place(x=370,y=100,width=250)
        
        username=Label(Frame1,text="Username",font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=100,y=150)
        self.txt_username=Entry(Frame1,font=("times new roman",15),bg="lightgray")
        self.txt_username.place(x=100,y=180,width=250)

        email=Label(Frame1,text="Email",font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=370,y=150)
        self.txt_email=Entry(Frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=180,width=250)

        password=Label(Frame1,text="Password",font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=100,y=230)
        self.txt_password=Entry(Frame1,font=("times new roman",15),show="*",bg="lightgray")
        self.txt_password.place(x=100,y=260,width=250)

        con_password=Label(Frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="gray",fg="black").place(x=370,y=230)
        self.txt_con_password=Entry(Frame1,font=("times new roman",15),show="*",bg="lightgray")
        self.txt_con_password.place(x=370,y=260,width=250)

        self.var_check=IntVar()
        check=Checkbutton(Frame1,text="I Agree the terms & Conditions",variable=self.var_check,onvalue=1,offvalue=0,bg="gray", font=("times new roman",12)).place(x=100,y=300)

        self.btn=Button(Frame1,text="Register Here",font=("times new roman",15,"bold"),bg="sandybrown",bd=0,cursor="hand2",command=self.register).place(x=200,y=350,width="250")
       
        left_btn=Button(self.root,text="Sign in",command=self.login_window, font=("times new roman",15,"bold"),bg="gold",bd=0,cursor="hand2").place(x=750,y=200,width="200")


    

    # *********working with database*******
    
    def login_window(self):
        self.root.destroy()
        import main
    
    def clear(self):
        self.txt_f_name.delete(0,END)
        self.txt_l_name.delete(0,END)
        self.txt_username.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_con_password.delete(0,END)
        
    
    
    def register(self):
        if self.txt_f_name.get()=="" or self.txt_l_name.get()=="" or self.txt_username.get()=="" or self.txt_email.get()=="" or self.txt_password.get()=="" or self.txt_con_password.get()=="": 
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_con_password.get():
            messagebox.showerror("Error","Password and Confirm Password should be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our terms and condition",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="himanshu")
                cur=con.cursor()
                cur.execute("select * from details where emails=%s", self.txt_email.get())
                row=cur.fetchone()
                # print(row)
                if row!=None:
                    messagebox.showinfo("Success","User Already Exist, please try with another email",parent=self.root)
                else:
                    cur.execute("insert into details (f_name, l_name, username, emails, password) values(%s,%s,%s,%s,%s)",
                            (self.txt_f_name.get(),
                             self.txt_l_name.get(),
                             self.txt_username.get(),
                             self.txt_email.get(),
                             self.txt_password.get()
                             ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Registration Successful",parent=self.root)
                    self.root.destroy()
                    import main
                    self.clear()


            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)



root=Tk()
obj=Register_window(root)
root.mainloop()
