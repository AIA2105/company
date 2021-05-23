from tkinter import *

from Business.Business import Business

root = Tk()
root.geometry("900x600")


def viewCustomers():
    id.configure(text='ID\n----------\n' + Business.AllCustomersIds())
    name.configure(text='Name\t\t\n----------\n' + Business.AllCustomersNames())
    phone.configure(text='Phone\t\t\n----------\n' + Business.AllCustomersPhones())


def searchId():
    if len(inpt1.get())!=0:
        cus = Business.CustomerID(inpt1.get())
        id.configure(text='ID\n----------\n' + cus.getId())
        name.configure(text='Name\t\t\n----------\n' + cus.getName())
        phone.configure(text='Phone\t\t\n----------\n' + cus.getPhone())

def searchName():
    if len(inpt1.get())!=0:
        cussId=''
        cussName=''
        cussPhone=''
        allNames= Business.AllCustomersNames().split('\n')
        for n in allNames:
            if n.__contains__(inpt1.get().capitalize()) or n.__contains__(inpt1.get()[0].lower() + inpt1.get()[1:]):
                print(n)
                cussId=cussId+Business.CustomerName(n).getId()+'\n'
                cussName=cussName+Business.CustomerName(n).getName()+'\n'
                cussPhone=cussPhone+Business.CustomerName(n).getPhone()+'\n'

            id.configure(text='ID\n----------\n' + cussId)
            name.configure(text='Name\t\t\n----------\n' + cussName)
            phone.configure(text='Phone\t\t\n----------\n' + cussPhone)

def insert():
    Business.InsertCustomer(nameInput.get(),phoneInput.get())
    viewCustomers()
    nameInput.delete(0, END)
    phoneInput.delete(0, END)

def update():
    Business.UpdateCustomerPhoneNumber(idInput.get(),phoneInput.get())
    viewCustomers()
    idInput.delete(0, END)
    phoneInput.delete(0, END)

def delete():
    Business.DeleteCustomer(idInput.get())
    viewCustomers()
    idInput.delete(0, END)


idSearchBtn = Button(command=searchId, width=10, text='Id Search', font=(5))
idSearchBtn.grid(row=0, column=0, padx=(10, 0), pady=(20, 10))
nameSearchBtn = Button(command=searchName, width=10, text='Name Search', font=(5))
nameSearchBtn.grid(row=0, column=1, padx=(10, 0), pady=(20, 10))

inpt1 = Entry(width=20, font=(10))
inpt1.grid(row=0, column=2, padx=(10, 20), pady=(20, 10))

getAll = Button(command=viewCustomers, width=10, text='Get All', font=(8),bg='yellow')
getAll.grid(row=0, column=3, padx=(10, 20), pady=(20, 10))

insert = Button(command=insert, width=10, text='Insert', font=(8),bg='yellow')
insert.grid(row=0, column=4, padx=(10, 20), pady=(20, 10))
update = Button(command=update, width=10, text='Update', font=(8),bg='yellow')
update.grid(row=1, column=3, padx=(10, 20), pady=(20, 10))
delete = Button(command=delete, width=10, text='Delete', font=(8),bg='yellow')
delete.grid(row=1, column=4, padx=(10, 20), pady=(20, 10))

resultLabel = Label(text='----- R e s u l t -----', font=8,fg='red')
resultLabel.grid(row=1, column=1, padx=(10, 20), pady=(30, 30))

idLabel = Label(text='ID', font=8,fg='red')
idLabel.place(x=600,y=170)
idInput = Entry(width=24, font=(10))
idInput.place(x=600,y=200)
nameLabel = Label(text='Name', font=8,fg='red')
nameLabel.place(x=600,y=240)
nameInput = Entry(width=24, font=(10))
nameInput.place(x=600,y=270)
phoneLabel = Label(text='Phone', font=8,fg='red')
phoneLabel.place(x=600,y=310)
phoneInput = Entry(width=24, font=(10))
phoneInput.place(x=600,y=340)
hint= Label(text='• Insert Btn: Must input Name & Phone.\n'
                 '• Update Btn: Must input Id & Phone.\n'
                 '• Delete Btn: Must input Id.', font=("Arial", 12),fg='gray',justify=LEFT)
hint.place(x=600,y=380)

id = Label(font=(8), bg='white', justify=LEFT)
id.grid(row=3, column=0, padx=(0, 0), pady=(0, 0))
name = Label(font=(8), bg='white', justify=LEFT)
name.grid(row=3, column=1, padx=(0, 0), pady=(0, 0))
phone = Label(font=(8), bg='white', justify=LEFT)
phone.grid(row=3, column=2, padx=(0, 0), pady=(0, 0))

mainloop()
