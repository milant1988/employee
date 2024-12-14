from customtkinter import *
from PIL import Image
from tkinter import ttk, messagebox
import database

def delete_all():
    result = messagebox.askyesno('Confirm','Do you really want to delete all the records?')
    if result:
        database.deleteall_records()

def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set('Search By')


def search_employee():
    if searchEntry.get()=='':
        messagebox.showerror('Error','Enter value to search')
    elif searchBox.get()=='Search By':
        messagebox.showerror('Error','Please select an option')
    else:
        searched_data = database.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert('',END,values=employee)

def delete_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Select data to delete')
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showerror('Error','Data is deleted')

def update_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Selected data to update')
    else:
        database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success', 'Data is updating')


def selection(event):
    selected_item = tree.selection()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0,row[5])

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    roleBox.set('Web Developer')
    genderBox.set('Male')
    salaryEntry.delete(0,END)


def treeview_data():
   employees = database.fetch_employees()
   tree.delete(*tree.get_children())
   for employee in employees:
       tree.insert('',END,values=employee)




def add_employee():
    if idEntry.get()=='' or phoneEntry.get()=='' or nameEntry.get()=='' or salaryEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error','Id already exists')
    elif not idEntry.get().startswith('EMP'):
        messagebox.showerror('Error',"Invalid ID ormat. Use 'EMP' folloed by a number (e.g.,'EMP1').")


    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success', 'Data is added')


window=CTk()
window.geometry('1200x620+100+100')
window.resizable(False,False)
window.title('Emloyee Management System')
window.configure(fg_color='#161C30')
logo = CTkImage(Image.open('Image/bg.png'),size=(1200,158))
logoLabel = CTkLabel(window,image=logo,text='')
logoLabel.grid(row=0,column=0,columnspan=2)

leftFrame = CTkFrame(window,fg_color='#161C30')
leftFrame.grid(row=1,column=0)

idLabel = CTkLabel(leftFrame,text='Id',font=('arial',18,'bold'),text_color='white')
idLabel.grid(row=0,column=0,padx=20,pady=15,sticky='w')

idEntry = CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
idEntry.grid(row=0,column=1)

nameLabel = CTkLabel(leftFrame,text='Name',font=('arial',18,'bold'),text_color='white')
nameLabel.grid(row=1,column=0,padx=20,pady=15,sticky='w')

nameEntry = CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
nameEntry.grid(row=1,column=1)

phoneLabel = CTkLabel(leftFrame,text='Phone',font=('arial',18,'bold'),text_color='white')
phoneLabel.grid(row=2,column=0,padx=20,pady=15,sticky='w')

phoneEntry = CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
phoneEntry.grid(row=2,column=1)

roleLabel = CTkLabel(leftFrame,text='Role',font=('arial',18,'bold'),text_color='white')
roleLabel.grid(row=3,column=0,padx=20,pady=15,sticky='w')
role_options = ['Web Developer','Cloud AArchitect','Tehnicaal Writer','Network Enginer','Devops Enginer',
                'Data Devloper','Busines Amalust','IT Consyltant','UX/UI Desinger']

roleBox = CTkComboBox(leftFrame,values=role_options,width=180,font=('arial',15,'bold'))
roleBox.grid(row=3,column=1)
roleBox.set(role_options[0])

genderLabel = CTkLabel(leftFrame,text='Gender',font=('arial',18,'bold'),text_color='white')
genderLabel.grid(row=4,column=0,padx=20,pady=15,sticky='w')
gender_options = ['Male','Female']

genderBox = CTkComboBox(leftFrame,values=gender_options,width=180,font=('arial',15,'bold'),state='readonly')
genderBox.grid(row=4,column=1)
genderBox.set(gender_options[0])

salaryLabel = CTkLabel(leftFrame,text='Salary',font=('arial',18,'bold'),text_color='white')
salaryLabel.grid(row=5,column=0,padx=20,pady=15,sticky='w')

salaryEntry = CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
salaryEntry.grid(row=5,column=1)

rightFrame = CTkFrame(window)
rightFrame.grid(row=1,column=1)

search_options = ['Id','Name','Phone','Role','Gender','Salary']
searchBox = CTkComboBox(rightFrame,values=search_options,state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('Search By')

searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)

searchButton = CTkButton(rightFrame,text='Search',width=100,command=search_employee)
searchButton.grid(row=0,column=2)

showallButton = CTkButton(rightFrame,text='Show all',width=100,command=show_all)
showallButton.grid(row=0,column=3,pady=5)

tree = ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=('Id','Name','Phone','Role','Gender','Salary')

tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show='headings')

tree.column('Id',width=100)
tree.column('Name',width=160)
tree.column('Phone',width=160)
tree.column('Role',width=200)
tree.column('Gender',width=100)
tree.column('Salary',width=100)

style = ttk.Style()
style.configure('Treeview.Heading',font=('arial',18,'bold'))
style.configure('Treeview',font=('arial',15,'bold'),rowheight=20,backqround='#161C30',foreground='black')

scrollbar = ttk.Scrollbar(rightFrame,orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1,column=4,sticky='ns')

tree.config(yscrollcommand=scrollbar.set)

buttonFrame = CTkFrame(window,fg_color='#161C30')
buttonFrame.grid(row=2,column=0,columnspan=2,pady=10)

newButton = CTkButton(buttonFrame,text='Newn Employe',font=('arial',15,'bold'),width=160,corner_radius=15,command=lambda: clear(True))
newButton.grid(row=0,column=0,pady=5)

addButton = CTkButton(buttonFrame,text='Add Employe',font=('arial',15,'bold'),width=160,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=1,pady=5,padx=5)

updateButton = CTkButton(buttonFrame,text='Update Employe',font=('arial',15,'bold'),width=160,corner_radius=15, command=update_employee)
updateButton.grid(row=0,column=2,pady=5,padx=5)

deleteButton = CTkButton(buttonFrame,text='Delete Employe',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_employee)
deleteButton.grid(row=0,column=3,pady=5,padx=5)

deleteAllButton = CTkButton(buttonFrame,text='Delete All Employe',font=('arial',15,'bold'),width=160,corner_radius=15,command=delete_all)
deleteAllButton.grid(row=0,column=4,pady=5,padx=5)

treeview_data()

window.bind('<ButtonRelease>',selection)

window.mainloop()