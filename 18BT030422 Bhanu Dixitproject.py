from tkinter import*
from tkinter import messagebox
import sqlite3
base = sqlite3.connect("Employee_Management.db")
base.execute ('''create table if not exists Employee_Data(
                Employee_Id  integer primary key,
                Employee_Name text not null,
                Date_Of_Joining text not null,
                Email text not null,
                Mobile_No text not null,
                Address text not null)''')
base.commit()
a = Tk()
a.geometry('900x900')
Employee_Id = IntVar()
Employee_Name= StringVar()
Date_of_Joining = StringVar()
Email = StringVar()
Mobile_No = StringVar()
Address =StringVar()


l1 = Label(a,text=' Employee Id:  ',font=('TimesNewRoman',20),fg='black',bg='white').grid(row=1,column=1)
e2 = Entry(a,textvariable=Employee_Id,font=('TimesNewRoman',20)).grid(row=1,column=2)
l2 = Label(a,text=' Employee Name : ',font=('TimesNewRoman',20),fg='black',bg='white').grid(row=2,column=1)
e2 = Entry(a,textvariable=Employee_Name,font=('TimesNewRoman',20)).grid(row=2,column=2)
l3 = Label(a,text='Date Of Joining : ',font=('TimesNewRoman',20),fg='black',bg='white').grid(row=3,column=1)
e3 = Entry(a,textvariable=Date_of_Joining,font=('TimesNewRoman',20)).grid(row=3,column=2)
l4 = Label(a,text='Email:  ',font=('TimesNewRoman',20),fg='black',bg='white').grid(row=4,column=1)
e4 = Entry(a,textvariable=Email,font=('TimesNewRoman',20)).grid(row=4,column=2)
l5 = Label(a,text='Mobile Number :  ',font=('TimesNewRoman',20),fg='black',bg='white').grid(row=11,column=1)
e5 = Entry(a,textvariable=Mobile_No,font=('TimesNewRoman',20)).grid(row=11,column=2)
l6 = Label(a,text='Address :  ',font=('TimesNewRoman',20),fg='black',bg='white').grid(row=12,column=1)
e7 = Entry(a,textvariable=Address,font=('TimesNewRoman',20)).grid(row=12,column=2)
def add():
    em_id = Employee_Id.get()
    print(em_id)
    em_name = Employee_Name.get()
    print(em_name)
    date = Date_of_Joining.get()
    print(date)
    email= Email.get()
    print(email)
    ph = Mobile_No.get()
    print(ph)
    ad=Address.get()
    print(ad)
    base.execute("insert into Employee_Data(Employee_Id,Employee_Name,Date_of_Joining,Email,Mobile_NO,Address) values(?,?,?,?,?,?)",(em_id,em_name,date,email,ph,ad))
    base.commit()
    messagebox.showinfo('Enter','Your Deatils Have been Added')
r4=Button(a,text="Add details",command=add).grid(row=18,column=1)
def update():
    em_id = Employee_Id.get()
    print(em_id)
    em_name = Employee_Name.get()
    print(em_name)
    date = Date_of_Joining.get()
    print(date)
    email= Email.get()
    print(email)
    ph = Mobile_No.get()
    print(ph)
    ad=Address.get()
    print(ad)
    base.execute("Update Employee_Data set Employee_Name=?,Date_of_Joining=?,Email=?,Mobile_NO=?,Address=? where Employee_Id=?",(em_name,date,email,ph,ad,em_id))
    base.commit()
    messagebox.showinfo('Update Details','Resent Data Has Been Updated')
r4=Button(a,text="Update Details",command=update).grid(row=18,column=2)
def Clear():
    em_id = Employee_Id.get()
    print(em_id)
    base.execute("Delete from Employee_Data where Employee_Id=? ",(em_id,))
    base.commit()
    
    messagebox.showinfo('Clear Deatils Details','Resent Data Has Been Cleared')
r4=Button(a,text="Clear Details",command=Clear).grid(row=18,column=4)
a.mainloop()
base.close()

