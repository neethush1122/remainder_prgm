from tkinter import *
import cx_Oracle
root = Tk()
root.geometry('600x500')
root.title("Remainder_Set_up")
day=StringVar()
month=StringVar()
name = StringVar()
event= StringVar()
def db():
                            # to Create and insert values into the database
    day1=day.get()
    month1=month.get()
    name1=name.get()
    event1=event.get()
    conn = cx_Oracle.connect("system/saint12345@localhost/XE")
    cursor=conn.cursor()
    cursor.execute('CREATE TABLE Remainder (day varchar(30) not null,month varchar(30) not null,name varchar(30) not null,event varchar(30) not null)')
    cursor.execute('INSERT INTO Remainder (day,month,name,event) VALUES(:1,:2,:3,:4)',(day1,month1,name1,event1))
    conn.commit()
    lab6.config(text="Remainder Added")


def update():
                            #To Update the Remainder. Field 'Name' is taken into consideration for the update condition since there is no primary key  used
    day1=day.get()
    month1=month.get()
    name1=name.get()
    event1=event.get()
    conn = cx_Oracle.connect("system/saint12345@localhost/XE")
    cursor=conn.cursor()
    cursor.execute('UPDATE Remainder SET day = :1,month=:2,event=:4 WHERE name = :3',(day1,month1,event1,name1))
    conn.commit()
    lab6.config(text="Remainder Updated")


def remind():
                                #to return the events  (as per system date)
    import time
    conn = cx_Oracle.connect("system/saint12345@localhost/XE")
    cursor=conn.cursor()
    cursor.execute('SELECT day,month,name,event FROM Remainder ')
    current=time.strftime('%d')
    x=cursor.fetchall();
    count=cursor.rowcount
    e=""
    for i in range(0,count):
        if x[i][0]==current:
             e=e+'Name : '+str(x[i][2])+' -- '+'Event : '+str(x[i][3]+'\n')
    lab6.config(text="%s"%e,font=("bold", 10))
    conn.commit()
   
def view():
    
                                #to view all the remainders
    import time
    conn = cx_Oracle.connect("system/saint12345@localhost/XE")
    cursor=conn.cursor()
    cursor.execute('SELECT day,month,name,event FROM Remainder ')
    x=cursor.fetchall();
    count=cursor.rowcount
    e=""
    for i in range(0,count):
        
        e=e+'Date : '+str(x[i][0])+'/'+str(x[i][1])+' -- '+'Name :'+str(x[i][2])+' -- '+'Event : '+str(x[i][3]+'\n')
    lab6.config(text="%s"%e,font=("bold", 10))
    conn.commit()

lab1 = Label(root, text="REMAINDER APP",width=20,font=("bold", 25))
lab1.place(x=120,y=33)
lab2= Label(root, text="Day",width=20,font=("bold", 10))
lab2.place(x=80,y=130)

e1 = Entry(root,width=30,textvar=day)
e1.place(x=240,y=130)
lab3 = Label(root, text="Month",width=20,font=("bold", 10))
lab3.place(x=80,y=180)

e2 = Entry(root,width=30,textvar=month)
e2.place(x=240,y=180)
lab4 = Label(root, text="Name",width=20,font=("bold", 10))
lab4.place(x=80,y=230)

e3 = Entry(root,width=30,textvar=name)
e3.place(x=240,y=230)
lab5 = Label(root, text="Event",width=20,font=("bold", 10))
lab5.place(x=80,y=280)

e4 = Entry(root,width=30,textvar=event)
e4.place(x=240,y=280)
lab6 = Label(root,font=("bold", 10))
lab6.place(x=150,y=450)

bt1=Button(root, text='Submit',width=15,bg='brown',fg='white',command=db)
bt1.place(x=60,y=380)
bt2=Button(root, text='Remainder',width=15,bg='brown',fg='white',command=remind)
bt2.place(x=180,y=380)
bt3=Button(root, text='Update',width=15,bg='brown',fg='white',command=update)
bt3.place(x=300,y=380)
bt4=Button(root, text='Show All',width=15,bg='brown',fg='white',command=view)
bt4.place(x=420,y=380)
root.mainloop()


