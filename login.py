
from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fields are requred')
    elif usernameEntry.get()=='milant' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Login is successul')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error','wrong credentials')


root = CTk()
root.geometry('938x478')
root.resizable(0,0)
root.title("Login page")
image = CTkImage(Image.open('Image/cover.jpg'),size=(930,478))
imageLabel = CTkLabel(root,image=image,text="")
imageLabel.place(x=0,y=0)
headinglabel =CTkLabel(root,text='Employee Management Sustem',bg_color='#FAFAFA',font=('Goudy Old Style',20,'bold'),text_color='dark blue')
headinglabel.place(x=20,y=100)

usernameEntry = CTkEntry(root,placeholder_text='Enter Your Username',width=180)
usernameEntry.place(x=50,y=150)

passwordEntry = CTkEntry(root,placeholder_text='Enter Your Password',width=180,show='*')
passwordEntry.place(x=50,y=200)

loginButton = CTkButton(root,text='Login',cursor='hand2',command=login)
loginButton.place(x=70,y=250)



root.mainloop()




