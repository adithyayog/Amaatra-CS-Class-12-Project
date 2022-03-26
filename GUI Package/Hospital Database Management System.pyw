from tkinter import *
from tkinter import messagebox as tkmsg
from tkinter.ttk import Progressbar as Progressbar
from mysql.connector import connect
import csv
from tkinter import ttk

"""
THIS IS THE GUI VERSION OF THE HOSPITAL DATABASE MANAGEMENT SYSTEM
DEVELOPED FOR THE CBSE GRADE 12 CLASS PRACTICAL EXAMINATION

GUI DEVELOPED BY
ADITHYA RANJITH - THE AMAATRA ACADEMY

LOGIC DEVELOPED BY
ADITHYA RANJITH- THE AMAATRA ACADEMY
ADITHYA YOGESH - THE AMAATRA ACADEMY
ADIT BASAK - THE AMAATRA ACADEMY
"""


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
#  CONNECTING TO MYSQL DATABASE
conn =connect (host='localhost', user='root', passwd='amaatra', database='project')
c1 = conn.cursor()

# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
maintablecount = 1
# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# HOSPITAL NAME AND TABLE NAME DICTIONARY AND CSV FILE
# global hospital
hospital = {}

fcsv = open('hospital.csv', 'a+', newline='')
fcsv.seek(0)
for j in csv.reader(fcsv):
    key = j[0]
    value = j[1]
    hospital[key] = value

adminkeylist = []
with open('adminkey.csv', 'r') as f:
    for i in csv.reader(f):
        adminkeylist.append(str(i[0]))
    f.close()


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FUNCTION TO GET CORRESPONDING TABLE NAME FROM HOSPITAL NAME
def sub_table_name(hospital_name):
    print(hospital_name)
    for key, value in hospital.items():
        if value == hospital_name:
            return key


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# TKINTER PROGRAMMING BEGINS

login = Tk()
login.iconbitmap('C:/Users/saiba/Downloads/pic1.ico')
login.title('Login Page')
login.geometry('450x310+400+180')
login.maxsize(450, 310)
login.minsize(450, 310)
login.rowconfigure(0, weight=1)
login.columnconfigure(0, weight=1)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# CREATING THE FRAME FOR THE SHOWING HOSPITALS IN PATIENT MODE
def show_hospital_patient():
    showhosp = Frame(login)
    showhosp.grid(row=0, column=0, sticky=NSEW)
    showhosp.tkraise()
    showhosp.configure(bg='#2b2b2b')
    login.geometry('500x500')
    login.maxsize(500, 500)
    login.minsize(500, 500)
    login.title('Hospitals')
    Button(showhosp, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=patient_page, width=72).grid(row=0,
                                                                                                         column=0,
                                                                                                         columnspan=2)
    Label(showhosp, text='Which Hospital Do You Want To Look At ? : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=1, column=0,
                                                                                                        padx=20,
                                                                                                        pady=20)
    remvar = StringVar(value='Select Hospital')
    listofhosp = []
    for i in hospital.values():
        listofhosp.append(str(i))
    tempvar = OptionMenu(showhosp, remvar, *listofhosp)
    tempvar.grid(row=1, column=1, padx=10, pady=20)
    tempvar.configure(bg='#2B2B2B', bd=0, fg='#A5B3C1', activebackground='grey')

    def show():
        c1.execute(f'select * from {sub_table_name(remvar.get())}')
        x = c1.fetchall()
        j = 0
        for i in x:
            j += 1
            Label(showhosp, text=i[1], padx=10, pady=5, bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=j + 2, column=0)
            Label(showhosp, text=i[2], padx=10, pady=5, bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=j + 2, column=1)
            if j == 15:
                break
    Button(showhosp, text='Show Information', command=show, bg='#3C3F41', fg='#A5B3C1', width=60).grid(row=2, column=0,
                                                                                                       columnspan=2,
                                                                                                       padx=30)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# CREATING THE FRAME FOR SHOWING DOCTORS IN PATIENT MODE
def show_doctors_patient():
    showdoc = Frame(login)
    login.title('Show Doctors')
    login.geometry('472x380')
    login.maxsize(472, 380)
    login.minsize(472, 380)
    showdoc.grid(row=0, column=0, sticky=NSEW)
    showdoc.configure(bg='#2B2B2B', width=470, height=350)
    showdoc.tkraise()
    baseframe = Frame(showdoc)
    baseframe.configure(bg='#2B2B2B', width=450, height=300)
    baseframe.grid(row=3, column=0, columnspan=2)
    doclist = ['Show All Doctors']
    datalist = ['Name           ', 'Age            ', 'Hospital       ', 'Department     ', 'Phone Number   ', 'x']
    c1.execute('select Name from doctor_details')
    for i in c1.fetchall():
        doclist.append(i[0])
    docvar = StringVar(value='Select Doctor')
    doctors = OptionMenu(showdoc, docvar, *doclist)

    doctors.configure(bg='#2B2B2B', bd=0, fg='#A5B3C1', activebackground='grey')
    Label(showdoc, text='Select Doctor To See Details :', bg='#2B2B2B', bd=0, fg='#A5B3C1') \
        .grid(row=1, column=0, pady=10
              )
    Button(showdoc, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=patient_page, width=67).grid(row=0,
                                                                                                         column=0,
                                                                                                         columnspan=2)
    doctors.grid(row=1, column=1)

    def showdoctors():
        message = ''
        global tb
        global sb
        try:
            tb.destroy()
            sb.destroy()
        except:
            pass
        if docvar.get() == 'Show All Doctors':
            c1.execute('select * from doctor_details')
            x = c1.fetchall()
            holding = 1
            for i in x:
                k = 0
                for j in i:
                    message = message + datalist[k] + '    '
                    message = message + str(j) + '\n'
                    k += 1
                message = message + '\n'
            sb = Scrollbar(baseframe)
            sb.pack(side='right', fill='y', pady=1)
            tb = Text(baseframe, height=15, width=50)
            tb.config(yscrollcommand=sb.set)
            sb.config(command=tb.yview)
            tb.pack(side='top', anchor='n', padx=25, pady=20)
            tb.replace(0.0, END, message)
            tb.config(bg='#2B2B2B', bd=0, fg='#A5B3C1', state=DISABLED)

        else:
            c1.execute(f'select * from doctor_details where name="{docvar.get()}"')
            x = c1.fetchall()
            k = 0
            holding = 1
            for i in x:
                for j in i:
                    message = message + datalist[k] + '    '
                    message = message + str(j) + '\n'
                    k += 1
            tb = Text(baseframe, height=15, width=50)

            tb.pack(side='top', anchor='n', padx=25, pady=20)
            tb.insert(END, message)
            tb.config(bg='#2B2B2B', bd=0, fg='#A5B3C1', state=DISABLED)

    Button(showdoc, text='Show Details', command=showdoctors, width=25, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=2,
                                                                                                               column=0,
                                                                                                               columnspan=2,
                                                                                                               pady=10)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# LOGIC BEHIND PATIENT LOG IN
def patient_login_mode():
    global username
    global password
    username = patientloginusername.get()
    password = patientloginpassword.get()
    passtempvar = 0
    with open('hospitalusrpw.csv', 'r') as f:
        book = csv.reader(f)
        for i in book:
            if f'{patientloginusername.get()}' == i[0]:
                if f'{patientloginpassword.get()}' == i[1]:
                    global X
                    global Y
                    global Z
                    c1.execute(f'select * from patient_logins where Username="{username}"')
                    for i in c1.fetchall():
                        X = str(i[1])
                        Y = str(i[2])
                        Z = str(i[3])
                    patient_page()
                    passtempvar = 1
                    patientloginusername.set('')
                    patientloginpassword.set('')
                    break
                else:
                    passtempvar = 0
            else:
                passtempvar = 0
        if passtempvar == 0:
            tkmsg.showinfo('Login Error', 'Username or Password is not recognised')

        f.close()


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# LOGIC BEHIND PATIENT REGISTRATION
def patient_register_mode():
    global username
    global password
    password = patientregisterpassword.get()
    username = patientregisterusername.get()
    with open('hospitalusrpw.csv', 'r') as f:
        book = csv.reader(f)
        tempregistervar = 1
        for i in book:
            if patientregisterusername.get() == i[0]:
                tempregistervar = 0
                tkmsg.showerror('Username Already In Use',
                                'Please Use A Different Username As The One You Have Picked Is Already In Use')
                break
        f.close()
    with open('hospitalusrpw.csv', 'a', newline='') as f:
        if patientregisterpassword.get() == patientregisterconfirmpassword.get() and tempregistervar != 0:
            global X
            global Y
            global Z
            c1.execute(f'select * from patient_logins where Username="{username}"')
            for i in c1.fetchall():
                X = str(i[1])
                Y = str(i[2])
                Z = str(i[3])
            patient_datafetch()
        elif patientregisterpassword.get() != patientregisterconfirmpassword.get() and tempregistervar != 0:
            tkmsg.showerror('Password Error', 'Password Not Confirmed Correctly')
        elif patientregisterpassword.get() != patientregisterconfirmpassword.get():
            tkmsg.showerror('Password Error', 'Password Not Confirmed Correctly')
        f.close()


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# LOGIC BEHIND ADMIN KEY
def adminkey():
    global adminkeylist

    def back():
        adminup.destroy()
        admin_mode_func()

    adminup = Frame(login)
    adminup.configure(bg='#2B2B2B')
    login.title('Update AdminKey')
    login.geometry('590x480')
    login.maxsize(590, 480)
    login.minsize(590, 480)
    adminup.grid(row=0, column=0, sticky=NSEW)
    adminup.tkraise()
    Button(adminup, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=back,
           width=85).grid(row=0, column=0, columnspan=2)
    Label(adminup, text='Admin Key Options', font=('Ariel Rounded Mt', 24, 'bold'),
          bg='#2B2B2B', fg='#FA3232').grid(row=1, column=0, columnspan=2, pady=10)
    print(adminkeylist)
    message = ''
    tx = Text(adminup, height=17, width=60, bg='#3C3F41', bd=0, fg='#A5B3C1')
    tx.grid(row=2, column=0, columnspan=2, pady=10)
    for i in adminkeylist:
        message = message + i + '\n'
    tx.insert(1.0, message)

    def sub():
        global adminkeylist
        page = tx.get(1.0, END)
        print(page)
        newlist = []
        j = ''
        for i in page:
            if i == '\n':
                newlist.append(j)
                j = ''
            else:
                j += i
        print(newlist)
        with open('adminkey.csv', 'w', newline='') as f:
            for i in newlist:
                if len(i)<1:
                    continue
                else:
                    print(i)
                    pencil = csv.writer(f)
                    pencil.writerow([i])
            f.close()
        print(adminkeylist)
        adminkeylist = []
        with open('adminkey.csv', 'r') as f:
            for i in csv.reader(f):
                adminkeylist.append(str(i[0]))
            f.close()

        print(adminkeylist)

    Button(adminup, text='update', command=sub, width=68, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=3, column=0,
                                                                                                 columnspan=2, padx=20,
                                                                                                 pady=10)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# LOGIC BEHIND ADMIN LOG IN
def admin_login_mode():
    global adminusername
    global adminpassword
    passtempvar = 0
    with open('hospitaladminusrpw.csv', 'r') as f:
        book = csv.reader(f)
        for i in book:
            if f'{adminloginusername.get()}' == i[0]:
                if f'{adminloginpassword.get()}' == i[1]:
                    adminusername = adminloginusername.get()
                    adminpassword = adminloginpassword.get()
                    admin_mode_func()
                    passtempvar = 1
                    adminloginusername.set('')
                    adminloginpassword.set('')
                    break
                else:
                    passtempvar = 0
            else:
                passtempvar = 0
        if passtempvar == 0:
            tkmsg.showinfo('Login Error', 'Username or Password is not recognised')

        f.close()


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# LOGIC BEHIND ADMIN REGISTRATION
def admin_register_mode():
    global adminusername
    global adminpassword
    global adminkeylist
    if adminregisteradminkey.get() in adminkeylist:
        with open('hospitaladminusrpw.csv', 'r') as f:
            book = csv.reader(f)
            tempregistervar = 1
            for i in book:
                if adminregisterusername.get() == i[0]:
                    tempregistervar = 0
                    tkmsg.showerror('Username Already In Use',
                                    'Please Use A Different Username As The One You Have Picked Is Already In Use')
                    break
            f.close()
        with open('hospitaladminusrpw.csv', 'a', newline='') as f:
            if adminregisterpassword.get() == adminregisterconfirmpassword.get() and tempregistervar != 0:
                pencil = csv.writer(f)
                pencil.writerow((adminregisterusername.get(), adminregisterpassword.get()))
                tkmsg.showinfo('Successfully Registered', 'Your Data Has Been Successfully Registered')
                adminusername = adminloginusername.get()
                adminpassword = adminloginpassword.get()
                admin_mode_func()
            elif adminregisterpassword.get() != adminregisterconfirmpassword.get() and tempregistervar != 0:
                tkmsg.showerror('Password Error', 'Password Not Confirmed Correctly')
            elif adminregisterpassword.get() != adminregisterconfirmpassword.get():
                tkmsg.showerror('Password Error', 'Password Not Confirmed Correctly')
            f.close()
    else:
        tkmsg.showerror('Admin Key Incorrect', 'The Admin Key Entered Is Incorrect')


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# LOGIC AND FRAME TO UPDATE PROFILE IN PATIENT MODE
def profile_update():
    global username

    def back():
        profile.destroy()
        patient_page()

    profile = Frame(login)
    profile.configure(bg='#2B2B2B')
    login.title('Update Profile')
    login.geometry('450x310')
    login.maxsize(450, 310)
    login.minsize(450, 310)
    profile.grid(row=0, column=0, sticky=NSEW)
    profile.tkraise()
    Button(profile, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=back,
           width=64).grid(row=0, column=0, columnspan=2)
    Label(profile, text='PATIENT PROFILE', font=('Ariel Rounded Mt', 16, 'bold'), bg='#2B2B2B', fg='#FA3232') \
        .grid(row=1, column=0, columnspan=2, pady=10)
    Label(profile, text='Username : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=2, column=0, pady=10)
    Label(profile, text=f'{username}', bg='#2B2B2B', fg='#A5B3C1').grid(row=2, column=1, pady=10)
    Label(profile, text='Name : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=3, column=0, pady=10)
    Label(profile, text='Phone Number : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=4, column=0, pady=10)
    Label(profile, text='Age : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=5, column=0, pady=10)
    c1.execute(f'select * from patient_logins where Username="{username}"')
    profilename = StringVar()
    profilephone = StringVar()
    profileage = IntVar()
    for i in c1.fetchall():
        profilename.set(str(i[1]))
        profileage.set(int(i[2]))
        profilephone.set(str(i[3]))
    Entry(profile, textvariable=profilename, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=3, column=1)
    Entry(profile, textvariable=profilephone, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=4, column=1)
    Entry(profile, textvariable=profileage, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=5, column=1)

    def update():
        c1.execute(
            f'UPDATE patient_logins SET Name="{profilename.get()}", Age="{profileage.get()}", Phone="{profilephone.get()}" where Username="{username}"')
        conn.commit()
        tkmsg.showinfo('Successfully Updated', 'Your Profile Information Has Been Successfully Updated')

    Button(profile, text='Update', bg='#3C3F41', bd=0, fg='#A5B3C1', width=47, command=update).grid(row=6, column=0,
                                                                                                    columnspan=2,
                                                                                                    pady=5)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# LOGIC AND FRAME TO UPDATE PASSWORD IN PATIENT MODE
def password_update():
    global username
    global password

    def back():
        pwd.destroy()
        patient_page()

    pwd = Frame(login)
    pwd.configure(bg='#2B2B2B')
    login.title('Update Password')
    login.geometry('450x310')
    login.maxsize(450, 310)
    login.minsize(450, 310)
    pwd.grid(row=0, column=0, sticky=NSEW)
    pwd.tkraise()
    Button(pwd, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=back,
           width=64).grid(row=0, column=0, columnspan=2)

    Label(pwd, text='PASSWORD UPDATE', font=('Ariel Rounded Mt', 16, 'bold'), bg='#2B2B2B', fg='#FA3232') \
        .grid(row=1, column=0, columnspan=2, pady=10)
    Label(pwd, text='Old Password : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=2, column=0, pady=10)
    Label(pwd, text='New Password : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=3, column=0, pady=10)
    Label(pwd, text='Confirm New Password : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=4, column=0, pady=10)
    Button(pwd, text='Update Password', bg='#3C3F41', bd=0, fg='#A5B3C1', width=50).grid(row=5, column=0, columnspan=2,
                                                                                         pady=10)

    opwd = StringVar()
    npwd = StringVar()
    cnpwd = StringVar()

    Entry(pwd, textvariable=opwd, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=2, column=1, pady=10)
    Entry(pwd, textvariable=npwd, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=3, column=1, pady=10)
    Entry(pwd, textvariable=cnpwd, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=4, column=1, pady=10)

    def updatepwd():
        if opwd.get() == password:
            if npwd.get() == cnpwd.get():
                book = []
                with open('hospitalusrpw.csv', 'r')as f:
                    for i in csv.reader(f):
                        book.append(i)
                    f.close()
                with open('hospitalusrpw.csv', 'w', newline='') as f:
                    pencil = csv.writer(f)
                    for i in book:
                        if i[0] != username:
                            pencil.writerow(i)
                        else:
                            pencil.writerow((username, npwd.get()))
                    f.close()

                tkmsg.showinfo('Successfully Updated', 'Password Has Been Updated Successfully')
            else:
                tkmsg.showerror('Password Error', 'Password Not Confirmed Correctly')
        else:
            tkmsg.showerror('Password Error', 'Old Password Is Incorrect')

    Button(pwd, text='Update Password', bg='#3C3F41', bd=0, fg='#A5B3C1', width=50, command=updatepwd) \
        .grid(row=5, column=0, columnspan=2, pady=10)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# LOGIC AND FRAME FOR APPOINTMENTS IN PATIENT MODE
def appointments():
    def back():
        apo.destroy()
        patient_page()

    apo = Frame(login)
    apo.configure(bg='#2B2B2B')
    login.title('Appointments')
    login.geometry('450x310')
    login.maxsize(450, 310)
    login.minsize(450, 310)
    apo.grid(row=0, column=0, sticky=NSEW)
    apo.tkraise()
    Button(apo, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=back,
           width=64).grid(row=0, column=0, columnspan=2)
    Label(apo, text='APPOINTMENTS', font=('Ariel Rounded Mt', 16, 'bold'), bg='#2B2B2B', fg='#FA3232') \
        .grid(row=1, column=0, columnspan=2, pady=15)
    Label(apo, text='HOSPITAL : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=2, column=0, pady=10)
    Label(apo, text='SERVICE : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=3, column=0, pady=10)
    Label(apo, text='TIME : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=4, column=0, pady=10)
    Label(apo, text='DATE : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=5, column=0, pady=10)
    servapo = StringVar()
    timeapo = StringVar()
    dateapo = StringVar()
    Entry(apo, bg='#3C3F41', bd=0, fg='#A5B3C1', textvariable=servapo).grid(row=3, column=1, pady=10)
    Entry(apo, bg='#3C3F41', bd=0, fg='#A5B3C1', textvariable=timeapo).grid(row=4, column=1, pady=10)
    Entry(apo, bg='#3C3F41', bd=0, fg='#A5B3C1', textvariable=dateapo).grid(row=5, column=1, pady=10)
    hosplist1 = []
    for i in hospital.values():
        hosplist1.append(str(i))
    hosptempvar = StringVar(value='Select Hospital')
    hospvar = OptionMenu(apo, hosptempvar, *hosplist1)
    hospvar.configure(bg='#2B2B2B', bd=0, fg='#A5B3C1')
    hospvar.grid(row=2, column=1, pady=10)

    def apointmentssubmit():
        c1.execute(
            f'insert into patient_details values("{X}","{Y}","{hosptempvar.get()}","{servapo.get()}","{Z}","{timeapo.get() + " " + dateapo.get()}")')
        conn.commit()
        tkmsg.showinfo('Appointment', 'Your Appointment Has Been Scheduled Successfully')

    Button(apo, text='Schedule Appointment', bg='#3C3F41', bd=0, fg='#A5B3C1', width=45,
           command=apointmentssubmit).grid(row=6, column=0,
                                           columnspan=2,
                                           pady=10)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# LOGIC AND FRAME FOR APPOINTMENTS IN PATIENT MODE
def apohistory():
    def back():
        showpat.destroy()
        patient_page()

    showpat = Frame(login)
    login.title('Appointment History')
    login.geometry('470x350')
    login.maxsize(470, 350)
    login.minsize(470, 350)
    showpat.configure(bg='#2B2B2B')
    showpat.grid(row=0, column=0, sticky=NSEW)

    Button(showpat, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=back, width=72).grid(row=0,
                                                                                                 column=0,
                                                                                                 columnspan=2)

    baseframe1 = Frame(showpat)
    baseframe1.configure(bg='#2B2B2B', width=450, height=300)
    baseframe1.grid(row=3, column=0, columnspan=2)
    patlist = ['Show All Patients']
    datalist = ['Name           ', 'Age            ', 'Hospital       ', 'Services       ', 'Phone Number   ',
                'Timing         ']
    c1.execute('select Name from patient_details')
    for i in c1.fetchall():
        patlist.append(i[0])
    patvar = StringVar(value='Select Patient')
    patients = OptionMenu(showpat, patvar, *patlist)

    patients.configure(bg='#2B2B2B', bd=0, fg='#A5B3C1', activebackground='grey')
    Label(showpat, text='Select Patient To See Details : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=1, column=0,
                                                                                                   padx=20, pady=10)
    patients.grid(row=1, column=1, pady=10)

    def showpatients():
        message = ''
        global tb1
        global sb1
        try:
            tb1.destroy()
            sb1.destroy()
        except:
            pass
        if patvar.get() == 'Show All Patients':
            c1.execute('select * from patient_details')
            x = c1.fetchall()
            for i in x:
                k = 0
                for j in i:
                    message = message + datalist[k] + '    '
                    message = message + str(j) + '\n'
                    k += 1
                message = message + '\n'
            sb1 = Scrollbar(baseframe1)
            sb1.pack(side='right', fill='y')
            tb1 = Text(baseframe1, height=15, width=50)
            tb1.config(yscrollcommand=sb1.set)
            sb1.config(command=tb1.yview)
            tb1.pack(side='top', anchor='n', padx=25, pady=20)
            tb1.replace(0.0, END, message)
            tb1.config(bg='#2B2B2B', bd=0, fg='#A5B3C1', state=DISABLED)

        else:
            c1.execute(f'select * from patient_details where name="{patvar.get()}"')
            x = c1.fetchall()
            k = 0
            for i in x:
                for j in i:
                    message = message + datalist[k] + '    '
                    message = message + str(j) + '\n'
                    k += 1
            tb1 = Text(baseframe1, height=15, width=50)

            tb1.pack(side='top', anchor='n', padx=25, pady=20)
            tb1.insert(END, message)
            tb1.config(bg='#2B2B2B', bd=0, fg='#A5B3C1', state=DISABLED)

    Button(showpat, text='Show Details', command=showpatients, width=25, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=2,
                                                                                                                column=0,
                                                                                                                columnspan=2)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME FOR THE MAIN PAGE
def login_frame():
    loginframe = Frame(login)
    loginframe.configure(bg='#2B2B2B')
    loginframe.grid(row=0, column=0, sticky=NSEW)
    loginframe.tkraise()
    login.title('Hospital Database Management')
    login.geometry('450x310')
    login.maxsize(450, 310)
    login.minsize(450, 310)
    Label(loginframe, text='\nAre You A Patient Or Administrator ? ', font=('Ariel Rounded Mt', 13, 'bold'),
          bg='#2B2B2B',
          fg='#A5B3C1').pack(side='top', pady=10)
    Button(loginframe, text='Patient ', bg='#3C3F41', bd=0, fg='#A5B3C1', width=50, command=patient_login_page).pack(
        side='top',
        pady=10,
        ipady=5)
    Button(loginframe, text='Administrator', bg='#3C3F41', bd=0, fg='#A5B3C1', width=50, command=admin_login_page).pack(
        side='top', pady=10, ipady=5)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME FOR THE MAIN PAGE
def first_frame():
    firstframe = Frame(login)
    firstframe.configure(bg='#2B2B2B')
    firstframe.grid(row=0, column=0, sticky=NSEW)
    firstframe.tkraise()
    login.title('Hospital Database Management')
    login.geometry('450x310')
    login.maxsize(450, 310)
    login.minsize(450, 310)
    Label(firstframe, text='\n    Hospital Database \n  Management Solutions', font=('Ariel Rounded Mt', 24, 'bold'),
          bg='#2B2B2B', fg='#FA3232',
          padx=20, pady=0).grid(row=4, column=0)
    style = ttk.Style()
    style.theme_use('default')
    style.configure('danger.Striped.Horizontal.TProgressbar', background='#FA3232', troughcolor='#2B2B2B',
                    borderwidth=0)
    progressbar = Progressbar(firstframe, orient=HORIZONTAL, length=400, mode='determinate', takefocus=TRUE,
                              style='danger.Striped.Horizontal.TProgressbar')
    progressbar.grid(sticky='w', padx=27, pady=20)
    Label(firstframe, text='CBSE Project - The Amaatra Academy', font=('Ariel Rounded Mt', 14, 'bold'), bg='#2B2B2B',
          fg='#A5B3C1', padx=35).grid(sticky='w')
    Label(firstframe, text='Adithya Ranjith', font=('Ariel Rounded Mt', 14, 'bold'), bg='#2B2B2B', fg='#A5B3C1',
          padx=35,
          pady=0).grid(sticky='w')
    Label(firstframe, text='Adithya Yogesh', font=('Ariel Rounded Mt', 14, 'bold'), bg='#2B2B2B', fg='#A5B3C1', padx=35,
          pady=0).grid(sticky='w')
    Label(firstframe, text='Adit Basak', font=('Ariel Rounded Mt', 14, 'bold'), bg='#2B2B2B', fg='#A5B3C1', padx=35,
          pady=0).grid(sticky='w')

    def bar():
        if progressbar['value'] < 101:
            progressbar['value'] += 0.02
            login.after(1, bar)

    bar()
    login.after(6000, login_frame)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME FOR THE PATIENT REGISTRATION PAGE
def patient_registration_page():
    global patientregisterusername
    global patientregisterpassword
    global patientregisterconfirmpassword

    patientregisterframe = Frame(login)
    patientregisterframe.grid(row=0, column=0, sticky=NSEW)
    patientregisterframe.configure(bg='#2B2B2B')
    patientregisterframe.tkraise()
    login.title('Sign Up')
    login.geometry('450x310')
    login.maxsize(450, 310)
    login.minsize(450, 310)

    Label(patientregisterframe, bg='#2B2B2B', fg='#FA3232', text='       New User, Register Here :',
          font=('Ariel Rounded Mt', 16, 'bold')) \
        .grid(row=1, column=0, columnspan=2, pady=25, padx=50)
    Label(patientregisterframe, text='Username :                                                                 ',
          bg='#2B2B2B', fg='#A5B3C1'). \
        grid(row=2, column=0, columnspan=2, pady=5)
    patientregisterusername = StringVar()
    Entry(patientregisterframe, textvariable=patientregisterusername, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=2,
                                                                                                             column=1,
                                                                                                             pady=5)
    Label(patientregisterframe, text='Password :                                                                ',
          bg='#2B2B2B', fg='#A5B3C1'). \
        grid(row=3, column=0, columnspan=2, pady=5)
    patientregisterpassword = StringVar()
    Entry(patientregisterframe, textvariable=patientregisterpassword, bg='#3C3F41', bd=0, fg='#A5B3C1', show='*').grid(
        row=3, column=1, pady=5)
    Label(patientregisterframe,
          text='Confirm Password :                                                               ', bg='#2B2B2B',
          fg='#A5B3C1').grid(row=4, column=0, columnspan=2, pady=5)
    patientregisterconfirmpassword = StringVar()
    Entry(patientregisterframe, textvariable=patientregisterconfirmpassword, bg='#3C3F41', bd=0, fg='#A5B3C1',
          show='*'). \
        grid(row=4, column=1, pady=5)
    Button(patientregisterframe, text='Sign Up!', bg='#3C3F41', bd=0, fg='#A5B3C1', width=41,
           command=patient_register_mode) \
        .grid(row=5, column=0, columnspan=2, pady=10)
    Button(patientregisterframe, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=patient_login_page,
           width=66).grid(
        row=0, column=0, columnspan=2)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME FOR THE PATIENT INFORMATION REGISTRATION PAGE
def patient_datafetch():
    global v
    v = 0

    def continuefetch():
        if namefetchvar.get() != '' and phonefetchvar.get() != '' and agefetchvar.get() != 0:
            c1.execute(f'insert into patient_logins values("{patientregisterusername.get()}","{namefetchvar.get()}",'
                       f'"{agefetchvar.get()}","{phonefetchvar.get()}")')
            conn.commit()
            with open('hospitalusrpw.csv', 'a', newline='') as f:
                pencil = csv.writer(f)
                pencil.writerow((patientregisterusername.get(), patientregisterpassword.get()))
                patient_page()
                tkmsg.showinfo('Successfully Registered', 'Your Data Has Been Successfully Registered')

        else:
            tkmsg.showerror('Error', 'All Fields Are Mandatory')

    def cancel():
        datafetch.destroy()
        patient_login_page()

    datafetch = Frame(login)
    datafetch.grid(row=0, column=0, sticky=NSEW)
    datafetch.configure(bg='#2B2B2B')
    datafetch.tkraise()
    login.geometry('450x310')
    login.maxsize(450, 310)
    login.minsize(450, 310)

    Label(datafetch, text='        Before We Continue !          ', font=('Ariel Rounded Mt', 16, 'bold')
          , bg='#2B2B2B', fg='#FA3232').grid(row=0, column=0, columnspan=2, padx=60, pady=15)
    Label(datafetch, text='Patient Name :                                                             ', bg='#2B2B2B',
          fg='#A5B3C1').grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    Label(datafetch, text='Phone Number :                                                               ', bg='#2B2B2B',
          fg='#A5B3C1').grid(row=2, columnspan=2, column=0, padx=10, pady=10)
    Label(datafetch, text='Patient Age :                                                                 ',
          bg='#2B2B2B', fg='#A5B3C1').grid(row=3, column=0, columnspan=2,
                                           padx=10, pady=10)
    namefetchvar = StringVar()
    phonefetchvar = StringVar()
    agefetchvar = IntVar()
    Entry(datafetch, textvariable=namefetchvar, bg='#3C3F41', bd=0, fg='#A5B3C1', width=20).grid(row=1, column=1,
                                                                                                 padx=10)
    Entry(datafetch, textvariable=phonefetchvar, bg='#3C3F41', bd=0, fg='#A5B3C1', width=20).grid(row=2, column=1,
                                                                                                  padx=10)
    Entry(datafetch, textvariable=agefetchvar, bg='#3C3F41', bd=0, fg='#A5B3C1', width=20).grid(row=3, column=1,
                                                                                                padx=10)

    Button(datafetch, text='Continue', bg='#3C3F41', bd=0, fg='#A5B3C1', width=39, command=continuefetch).grid(row=4,
                                                                                                               column=0,
                                                                                                               columnspan=2,
                                                                                                               padx=10,
                                                                                                               pady=10)
    Button(datafetch, text='Cancel', bg='#3C3F41', bd=0, fg='#A5B3C1', width=39, command=cancel).grid(row=5, column=0,
                                                                                                      columnspan=2,
                                                                                                      padx=10, pady=10)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME FOR THE PATIENT LOGIN PAGE
def patient_login_page():
    global patientloginusername
    global patientloginpassword

    patientloginframe = Frame(login)
    patientloginframe.grid(row=0, column=0, sticky=NSEW)
    patientloginframe.tkraise()
    login.title('Login')
    login.geometry('450x310')
    login.maxsize(450, 310)
    login.minsize(450, 310)

    Button(patientloginframe, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=login_frame, width=66).grid(row=0,
                                                                                                                  column=0,
                                                                                                                  columnspan=2)
    patientloginframe.configure(bg='#2B2B2B')
    Label(patientloginframe, text=' Welcome Patients, Log in to continue:  ', font=('Ariel Rounded Mt', 16, 'bold')
          , bg='#2B2B2B', fg='#FA3232').grid(row=1, column=0, rowspan=3, columnspan=2, padx=20, pady=10)
    Label(patientloginframe, text='Username :                                                             ',
          bg='#2B2B2B',
          fg='#A5B3C1').grid(row=4, column=0, columnspan=2, pady=5)
    Label(patientloginframe, text='Password :                                                             ',
          bg='#2B2B2B',
          fg='#A5B3C1').grid(row=5, column=0, columnspan=2, pady=5)
    patientloginusername = StringVar()
    patientloginpassword = StringVar()
    Entry(patientloginframe, bg='#3C3F41', textvariable=patientloginusername, bd=0, fg='#A5B3C1', width=30).grid(row=4,
                                                                                                                 column=1,
                                                                                                                 pady=5,
                                                                                                                 padx=70)
    Entry(patientloginframe, bg='#3C3F41', textvariable=patientloginpassword, bd=0, fg='#A5B3C1', width=30,
          show='*').grid(row=5, column=1,
                         pady=5, padx=70)
    Button(patientloginframe, bg='#3C3F41', bd=0, fg='#A5B3C1', text='Log In', command=patient_login_mode,
           width=34).grid(row=6,
                          column=0,
                          columnspan=2,
                          pady=3)
    Label(patientloginframe, bg='#2B2B2B', fg='#FA3232', text='                                    ',
          font=('Ariel Rounded Mt', 13, 'bold')) \
        .grid(row=7, column=0, columnspan=2, pady=0)
    Label(patientloginframe, bg='#2B2B2B', fg='#FA3232',
          text='New User, Register Here :                                    ',
          font=('Ariel Rounded Mt', 13, 'bold')) \
        .grid(row=8, column=0, columnspan=2, pady=5)
    Button(patientloginframe, bg='#3C3F41', bd=0, fg='#A5B3C1', text='SIGN UP', command=patient_registration_page,
           width=34) \
        .grid(row=9, column=0, columnspan=2, pady=3)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME FOR THE PATIENT PAGE
def patient_page():
    patientframe = Frame(login)
    patientframe.grid(row=0, column=0, sticky=NSEW)
    patientframe.configure(bg='#2B2B2B')
    patientframe.tkraise()
    login.title('Patient Page')
    login.geometry('450x310')
    login.maxsize(450, 310)
    login.minsize(450, 310)

    mb = Menubutton(patientframe, text='Profile', bg='#3C3F41', bd=0, fg='#A5B3C1')
    mb.grid(row=0, column=0)
    mb_menu = Menu(mb, tearoff=0)
    mb['menu'] = mb_menu
    mb_menu.add_command(label='Profile', command=profile_update)
    mb_menu.add_command(label='Change Password', command=password_update)
    mb_menu.add_command(label='Log Out', command=patient_login_page)

    Label(patientframe, text='Welcome !', font=('Ariel Rounded Mt', 16, 'bold'), bg='#2B2B2B', fg='#FA3232').grid(
        padx=120,
        row=1, column=1, pady=10)

    Button(patientframe, text='Show Hospitals', bg='#3C3F41', bd=0, fg='#A5B3C1', width=40, height=1,
           command=show_hospital_patient).grid(padx=30, row=2, column=1,
                                               columnspan=2, pady=10)
    Button(patientframe, text='View Doctors', bg='#3C3F41', bd=0, fg='#A5B3C1', width=40, height=1,
           command=show_doctors_patient). \
        grid(padx=30, row=3, column=1,
             columnspan=2, pady=10)
    Button(patientframe, text='Book Appointments', bg='#3C3F41', bd=0, fg='#A5B3C1', width=40, height=1,
           command=appointments) \
        .grid(padx=30,
              row=4,
              column=1,
              columnspan=2,
              pady=10)
    Button(patientframe, text='View Appointment History', bg='#3C3F41', bd=0, fg='#A5B3C1', width=40, height=1,
           command=apohistory).grid(
        padx=30, row=5,
        column=1, columnspan=2, pady=10)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME FOR THE ADMINISTRATION LOGIN PAGE
def admin_login_page():
    global adminloginusername
    global adminloginpassword

    adminloginframe = Frame(login)
    adminloginframe.grid(row=0, column=0, sticky=NSEW)
    adminloginframe.tkraise()
    login.title('Admin Login')
    login.geometry('450x310')
    login.maxsize(450, 310)
    login.minsize(450, 310)

    Button(adminloginframe, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=login_frame, width=66).grid(row=0,
                                                                                                                column=0,
                                                                                                                columnspan=2)
    adminloginframe.configure(bg='#2B2B2B')
    Label(adminloginframe, text=' Program Administration Login:  ', font=('Ariel Rounded Mt', 16, 'bold')
          , bg='#2B2B2B', fg='#FA3232').grid(row=1, column=0, rowspan=3, columnspan=2, padx=20, pady=10)
    Label(adminloginframe, text='Username :                                                             ', bg='#2B2B2B',
          fg='#A5B3C1').grid(row=4, column=0, columnspan=2, pady=5)
    Label(adminloginframe, text='Password :                                                             ', bg='#2B2B2B',
          fg='#A5B3C1').grid(row=5, column=0, columnspan=2, pady=5)
    adminloginusername = StringVar()
    adminloginpassword = StringVar()
    Entry(adminloginframe, bg='#3C3F41', textvariable=adminloginusername, bd=0, fg='#A5B3C1', width=30).grid(row=4,
                                                                                                             column=1,
                                                                                                             pady=5,
                                                                                                             padx=70)
    Entry(adminloginframe, bg='#3C3F41', textvariable=adminloginpassword, bd=0, fg='#A5B3C1', width=30, show='*').grid(
        row=5, column=1,
        pady=5, padx=70)
    Button(adminloginframe, bg='#3C3F41', bd=0, fg='#A5B3C1', text='Log In', command=admin_login_mode, width=34).grid(
        row=6,
        column=0,
        columnspan=2,
        pady=3)
    Label(adminloginframe, bg='#2B2B2B', fg='#FA3232', text='                                    ',
          font=('Ariel Rounded Mt', 13, 'bold')) \
        .grid(row=7, column=0, columnspan=2, pady=0)
    Label(adminloginframe, bg='#2B2B2B', fg='#FA3232', text='New Admin, Register Here :                  ',
          font=('Ariel Rounded Mt', 13, 'bold')) \
        .grid(row=8, column=0, columnspan=2, pady=5)

    Button(adminloginframe, bg='#3C3F41', bd=0, fg='#A5B3C1', text='SIGN UP', command=admin_registration_page,
           width=34) \
        .grid(row=9, column=0, columnspan=2, pady=3)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME FOR THE ADMINISTRATION REGISTRATION PAGE
def admin_registration_page():
    global adminregisterusername
    global adminregisterpassword
    global adminregisterconfirmpassword
    global adminregisteradminkey

    adminregisterframe = Frame(login)
    adminregisterframe.grid(row=0, column=0, sticky=NSEW)
    adminregisterframe.configure(bg='#2B2B2B')
    adminregisterframe.tkraise()
    login.title('Admin Registration')
    login.geometry('450x310')
    login.maxsize(450, 310)
    login.minsize(450, 310)

    Label(adminregisterframe, bg='#2B2B2B', fg='#FA3232', text='New Admin, Register Here :',
          font=('Ariel Rounded Mt', 16, 'bold')) \
        .grid(row=1, column=0, columnspan=2, pady=25, padx=50)
    Label(adminregisterframe, text='Username :                                                                 ',
          bg='#2B2B2B', fg='#A5B3C1'). \
        grid(row=2, column=0, columnspan=2, pady=5)
    adminregisterusername = StringVar()
    Entry(adminregisterframe, textvariable=adminregisterusername, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=2,
                                                                                                         column=1,
                                                                                                         pady=5)
    Label(adminregisterframe, text='Password :                                                                ',
          bg='#2B2B2B', fg='#A5B3C1'). \
        grid(row=3, column=0, columnspan=2, pady=5)
    adminregisterpassword = StringVar()
    Entry(adminregisterframe, textvariable=adminregisterpassword, bg='#3C3F41', bd=0, fg='#A5B3C1', show='*').grid(
        row=3, column=1, pady=5)
    Label(adminregisterframe, text='Confirm Password :                                                               ',
          bg='#2B2B2B',
          fg='#A5B3C1').grid(row=4, column=0, columnspan=2, pady=5)
    adminregisterconfirmpassword = StringVar()
    Entry(adminregisterframe, textvariable=adminregisterconfirmpassword, bg='#3C3F41', bd=0, fg='#A5B3C1', show='*'). \
        grid(row=4, column=1, pady=5)
    Label(adminregisterframe, text='Admin Pass Key :                                                               ',
          bg='#2B2B2B',
          fg='#A5B3C1').grid(row=5, column=0, columnspan=2, pady=5)
    adminregisteradminkey = StringVar()
    Entry(adminregisterframe, textvariable=adminregisteradminkey, bg='#3C3F41', bd=0, fg='#A5B3C1', show='*'). \
        grid(row=5, column=1, pady=5)
    Button(adminregisterframe, text='Sign Up!', bg='#3C3F41', bd=0, fg='#A5B3C1', width=41, command=admin_register_mode) \
        .grid(row=6, column=0, columnspan=2, pady=10)
    Button(adminregisterframe, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=admin_login_page, width=66).grid(
        row=0,
        column=0,
        columnspan=2)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME TO ADD HOSPITALS
def add_hospital():
    def back():
        add_hospital_toplevel.destroy()
        admin_mode_func()

    add_hospital_toplevel = Frame(login)
    add_hospital_toplevel.configure(bg='#2B2B2B')
    add_hospital_toplevel.grid(row=0, column=0, sticky=NSEW)
    Button(add_hospital_toplevel, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=back,
           width=50).grid(row=0, column=0, columnspan=2)
    add_hospital_toplevel.tkraise()
    login.title('Add Hospital')
    login.geometry('350x500')
    login.maxsize(350, 500)
    login.minsize(350, 500)

    # DEFINING THE VARIABLES
    name = StringVar()
    address = StringVar()
    area = StringVar()
    consult_cost = StringVar()
    contact = StringVar()
    beds = StringVar()
    beds_cost = StringVar()
    o2 = StringVar()
    amb = StringVar()
    vaccine = StringVar()
    ct = StringVar(value='No')
    ct_cost = StringVar(value='N/A')
    mri = StringVar(value='No')
    mri_cost = StringVar(value='N/A')
    cov = StringVar(value='No')
    cov_cost = StringVar(value='N/A')
    xray = StringVar(value='No')
    xray_cost = StringVar(value='N/A')
    # =====X=====X=====X=====X=====X=====X=====X=====X=====X=====X=====X=====X=====X=====X=====X=====X=====X=====X=====X=====
    # LABEL AND ENTRIES AND CHECK BUTTONS
    Label(add_hospital_toplevel, text='Name : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=2, column=0)
    Label(add_hospital_toplevel, text='Address : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=3, column=0)
    Label(add_hospital_toplevel, text='Area : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=4, column=0)
    Label(add_hospital_toplevel, text='Consultation Cost : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=5,
                                                                                                                column=0)
    Label(add_hospital_toplevel, text='Contact : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=6, column=0)
    Label(add_hospital_toplevel, text='Beds : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=7, column=0)
    Label(add_hospital_toplevel, text='Cost of Beds : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=8,
                                                                                                           column=0)
    Label(add_hospital_toplevel, text='Ambulance Service : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=9,
                                                                                                                column=0)
    Label(add_hospital_toplevel, text='Oxygen Available : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=10,
                                                                                                               column=0)
    Label(add_hospital_toplevel, text='Covid Vaccine Available : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(
        row=11,
        column=0)
    Label(add_hospital_toplevel, text='CT SCAN Available : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=12,
                                                                                                                column=0)
    Label(add_hospital_toplevel, text='MRI SCAN Available : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=14,
                                                                                                                 column=0)
    Label(add_hospital_toplevel, text='COVID TEST Available : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(
        row=16,
        column=0)
    Label(add_hospital_toplevel, text='XRAY SCAN Available : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(
        row=18,
        column=0)
    Entry(add_hospital_toplevel, textvariable=name, bg='#3C3F41', fg='#A5B3C1').grid(row=2, column=1, padx=20, pady=5)
    Entry(add_hospital_toplevel, textvariable=address, bg='#3C3F41', fg='#A5B3C1').grid(row=3, column=1, padx=20,
                                                                                        pady=5)
    Entry(add_hospital_toplevel, textvariable=area, bg='#3C3F41', fg='#A5B3C1').grid(row=4, column=1, padx=20, pady=5)
    Entry(add_hospital_toplevel, textvariable=consult_cost, bg='#3C3F41', fg='#A5B3C1').grid(row=5, column=1, padx=20,
                                                                                             pady=5)
    Entry(add_hospital_toplevel, textvariable=contact, bg='#3C3F41', fg='#A5B3C1').grid(row=6, column=1, padx=20,
                                                                                        pady=5)
    Entry(add_hospital_toplevel, textvariable=beds, bg='#3C3F41', fg='#A5B3C1').grid(row=7, column=1, padx=20, pady=5)
    Entry(add_hospital_toplevel, textvariable=beds_cost, bg='#3C3F41', fg='#A5B3C1').grid(row=8, column=1, padx=20,
                                                                                          pady=5)
    Entry(add_hospital_toplevel, textvariable=o2, bg='#3C3F41', fg='#A5B3C1').grid(row=9, column=1, padx=20, pady=5)
    Entry(add_hospital_toplevel, textvariable=amb, bg='#3C3F41', fg='#A5B3C1').grid(row=10, column=1, padx=20, pady=5)
    Entry(add_hospital_toplevel, textvariable=vaccine, bg='#3C3F41', fg='#A5B3C1').grid(row=11, column=1, padx=20,
                                                                                        pady=5)

    def costofct():
        global ct
        login.geometry('350x520')
        login.maxsize(350, 520)
        login.minsize(350, 520)
        ct = 'Yes'
        Label(add_hospital_toplevel, text='Cost of CT SCAN : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=13, column=0)
        Entry(add_hospital_toplevel, textvariable=ct_cost, bg='#3C3F41', fg='#A5B3C1').grid(row=13, column=1)

    def costofmri():
        global mri
        login.geometry('350x540')
        login.maxsize(350, 540)
        login.minsize(350, 540)
        mri = 'Yes'
        Label(add_hospital_toplevel, text='Cost of MRI SCAN : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=15, column=0)
        Entry(add_hospital_toplevel, textvariable=mri_cost, bg='#3C3F41', fg='#A5B3C1').grid(row=15, column=1)

    def costofcov():
        global cov
        login.geometry('350x560')
        login.maxsize(350, 560)
        login.minsize(350, 560)
        cov = 'Yes'
        Label(add_hospital_toplevel, text='Cost of COVID TEST : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=17, column=0)
        Entry(add_hospital_toplevel, textvariable=cov_cost, bg='#3C3F41', fg='#A5B3C1').grid(row=17, column=1)

    def costofxray():
        global xray
        login.geometry('350x585')
        login.maxsize(350, 585)
        login.minsize(350, 585)
        xray = 'Yes'
        Label(add_hospital_toplevel, text='Cost of XRAY SCAN : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=19, column=0)
        Entry(add_hospital_toplevel, textvariable=xray_cost, bg='#3C3F41', fg='#A5B3C1').grid(row=19, column=1)

    Checkbutton(add_hospital_toplevel, text=' YES ', bg='#2B2B2B', fg='#A5B3C1', command=costofct, padx=20,
                pady=5).grid(row=12,
                             column=1)
    Checkbutton(add_hospital_toplevel, text=' YES ', bg='#2B2B2B', fg='#A5B3C1', command=costofmri, padx=20,
                pady=5).grid(row=14,
                             column=1)
    Checkbutton(add_hospital_toplevel, text=' YES ', bg='#2B2B2B', fg='#A5B3C1', command=costofcov, padx=20,
                pady=5).grid(row=16,
                             column=1)
    Checkbutton(add_hospital_toplevel, text=' YES ', bg='#2B2B2B', fg='#A5B3C1', command=costofxray, padx=20,
                pady=5).grid(
        row=18,
        column=1)

    def submit():

        for i in range(1, 2):
            global maintablecount
            c1.execute("insert into hospitals values(" + "'" + str(
                maintablecount) + "', '" + name.get() + "'," + "'" + address.get() + "'," + "'" + area.get() + "'" + ")")
            conn.commit()
            maintablecount += 1
            c1.execute(
                f'create table {name.get().replace(" ", "")}(srno int, data_name varchar(255), data varchar(255))')
            conn.commit()
        x = {contact.get(): 'Contact Details', consult_cost.get(): 'Consultation Cost', beds.get(): 'Beds Availability',
             beds_cost.get(): 'Cost of Beds', o2.get(): 'Oxygen Availability', amb.get(): 'Ambulance Service Cost',
             vaccine.get(): 'Covid Vaccines Available', ct.get(): 'CT SCAN Availability',
             ct_cost.get(): 'Cost of CT SCAN',
             mri.get(): 'MRI SCAN Availability', mri_cost.get(): 'Cost of MRI SCAN',
             cov.get(): 'COVID TEST Availability',
             cov_cost.get(): 'Cost of COVID TEST', xray.get(): 'X-RAY SCAN Availability',
             xray_cost.get(): 'Cost of X-RAY SCAN'}
        count = 1
        for key, value in x.items():
            c1.execute(
                f'insert into {name.get().replace(" ", "")} values("{str(count)}", "{str(value)}", "{str(key)}")')
            conn.commit()
            count += 1
        print('Data Successfully Updated')
        global hospital
        global fcsv
        csv.writer(fcsv).writerow((name.get().replace(' ', ''), name.get()))
        hospital[name.get().replace(' ', '')] = name.get()
        print(hospital)
        tkmsg.showinfo('Data Successfully Submitted',
                       'Your Data Has Been Submitted Successfully \nClick OK to return to Admin Mode')
        admin_mode_func()

    Button(add_hospital_toplevel, text='SUBMIT', command=submit, padx=120, bg='#5b5b5b', fg='#A5B3C1',
           activebackground='#2B2B2B').grid(row=20, column=0,
                                            columnspan=2,
                                            padx=20, pady=10)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME TO UPDATE HOSPITALS
def update_hospital():
    def back():
        upd.destroy()
        admin_mode_func()

    upd = Frame(login)
    upd.configure(bg='#2B2B2B')
    login.title('Update Hospital Date')
    login.geometry('450x220')
    login.maxsize(450, 220)
    login.minsize(450, 220)
    upd.grid(row=0, column=0, sticky=NSEW)
    upd.tkraise()
    Button(upd, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=back,
           width=64).grid(row=0, column=0, columnspan=2)
    updvar = StringVar(value='Select Data Name')
    updtextvar = StringVar()
    updlist = ['Name', 'Location', 'Area', 'Contact Details', 'Consultation Cost', 'Beds Availability', 'Cost Of Beds',
               'Oxygen Availability', 'Ambulance Service Cost', 'Covid Vaccines Availability', 'CT SCAN Availability',
               'Cost of CT SCAN', 'MRI SCAN Availability', 'Cost of MRI SCAN', 'COVID TEST Availability',
               'Cost of COVID TEST', 'X-RAY SCAN Availability', 'Cost of X-RAY SCAN']
    remvar = StringVar(value='   Select Hospital  ')
    listofhosp = []
    for i in hospital.values():
        listofhosp.append(str(i))
    tempvar = OptionMenu(upd, remvar, *listofhosp)
    tempvar.grid(row=1, column=1, padx=10, pady=20)
    tempvar.configure(bg='#2B2B2B', bd=0, fg='#A5B3C1', activebackground='grey')
    Label(upd, text='Which Hospital Do You Want To Update ? :', bg='#2B2B2B', fg='#A5B3C1').grid(row=1, column=0,
                                                                                                 padx=20,
                                                                                                 pady=20)
    temp1var = OptionMenu(upd, updvar, *updlist)
    temp1var.configure(bg='#2B2B2B', fg='#A5B3C1', bd=0)
    temp1var.grid(row=2, column=1, padx=10, pady=10)
    Label(upd, text='What Do You Want To Update ? :', bg='#2B2B2B', fg='#A5B3C1').grid(row=2, column=0, padx=20,
                                                                                       pady=10)
    Label(upd, text='What Is The New Data ? :', bg='#2B2B2B', fg='#A5B3C1').grid(row=3, column=0, padx=20, pady=10)
    Entry(upd, textvariable=updtextvar, bg='#3C3F41', fg='#A5B3C1').grid(row=3, column=1, padx=10, pady=10)

    def update():
        if updvar.get() in ('Name', 'Location', 'Area'):
            c1.execute(
                f'update hospitals set {updvar.get().lower()} = "{updtextvar.get()}" where name ="{remvar.get()}"')
            conn.commit()
        else:
            c1.execute(
                f'update {sub_table_name(remvar.get())} set data = "{updtextvar.get()}" where data_name = "{updvar.get()}"')
            conn.commit()
        tkmsg.showinfo('Successfully Updated', f'{updvar.get()} Has Been Successfully Updated in {remvar.get()}')

    Button(upd, text='Update', command=update, bg='#3C3F41', fg='#A5B3C1', bd=0, width=50).grid(row=4, column=0,
                                                                                                padx=10,
                                                                                                pady=10, columnspan=2)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME TO REMOVE HOSPITALS
def remove_hospital():
    def back():
        rem.destroy()
        admin_mode_func()

    rem = Frame(login)
    rem.configure(bg='#2B2B2B')
    login.title('Remove Hospital')
    rem.grid(row=0, column=0, sticky=NSEW)
    rem.tkraise()
    login.geometry('420x200')
    login.maxsize(420, 200)
    login.minsize(420, 200)
    Button(rem, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=back, width=62).grid(row=0,
                                                                                             column=0,
                                                                                             columnspan=2)
    Label(rem, text='Which Hospital Do You Want To Remove? : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=1, column=0,
                                                                                                       ipadx=10,
                                                                                                       pady=20)
    remvar = StringVar(value='Select Hospital')
    listofhosp = []
    for i in hospital.values():
        listofhosp.append(str(i))
    tempvar = OptionMenu(rem, remvar, *listofhosp)
    tempvar.grid(row=1, column=1, padx=30, pady=20)
    tempvar.configure(bg='#2B2B2B', bd=0, fg='#A5B3C1', activebackground='grey')

    def submit():
        yesno = tkmsg.askyesno('Are You Sure?', f'Are You Sure You Want To Delete {remvar.get()} From The Database?')
        if yesno == TRUE:
            c1.execute(f'drop table {sub_table_name(remvar.get())}')
            conn.commit()
            tkmsg.showinfo('Hospital Successfully Removed',
                           f'{remvar.get()} has been successfully removed from the database.')
        else:
            pass

    Button(rem, text='Delete Hospital', command=submit, width=50, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(padx=15,
                                                                                                         pady=25,
                                                                                                         columnspan=2)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME TO SHOW DOCTORS
def show_doctors_admin():
    def back():
        showdoc.destroy()
        admin_mode_func()

    showdoc = Frame(login)
    login.title('Show Doctors')
    login.geometry('468x373')
    login.maxsize(468, 373)
    login.minsize(468, 373)
    showdoc.configure(bg='#2B2B2B')
    showdoc.grid(row=0, column=0, sticky=NSEW)
    showdoc.tkraise()
    Button(showdoc, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=back, width=66).grid(row=0,
                                                                                                 column=0,
                                                                                                 columnspan=2)
    baseframe = Frame(showdoc)
    baseframe.configure(bg='#2B2B2B', width=448, height=300)
    baseframe.grid(row=3, column=0, columnspan=2)
    doclist = ['Show All Doctors']
    datalist = ['Name           ', 'Age            ', 'Hospital       ', 'Department     ', 'Phone Number   ', 'x']
    c1.execute('select Name from doctor_details')
    for i in c1.fetchall():
        doclist.append(i[0])
    docvar = StringVar(value='Select Doctor')
    doctors = OptionMenu(showdoc, docvar, *doclist)

    doctors.configure(bg='#2B2B2B', bd=0, fg='#A5B3C1', activebackground='grey')
    Label(showdoc, text='Select Doctor To See Details : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=1, column=0,
                                                                                                  padx=20, pady=10)
    doctors.grid(row=1, column=1, pady=10)

    def showdoctors():
        message = ''
        global tb
        global sb
        try:
            tb.destroy()
            sb.destroy()
        except:
            pass
        if docvar.get() == 'Show All Doctors':
            c1.execute('select * from doctor_details')
            x = c1.fetchall()
            holding = 1
            for i in x:
                k = 0
                for j in i:
                    message = message + datalist[k] + '    '
                    message = message + str(j) + '\n'
                    k += 1
                message = message + '\n'
            sb = Scrollbar(baseframe)
            sb.pack(side='right', fill='y', padx=5)
            tb = Text(baseframe, height=15, width=50)
            tb.config(yscrollcommand=sb.set)
            sb.config(command=tb.yview)
            tb.pack(side='top', anchor='n', padx=22, pady=20)
            tb.replace(0.0, END, message)
            tb.config(bg='#2B2B2B', bd=0, fg='#A5B3C1', state=DISABLED)

        else:
            c1.execute(f'select * from doctor_details where name="{docvar.get()}"')
            x = c1.fetchall()
            k = 0
            holding = 1
            for i in x:
                for j in i:
                    message = message + datalist[k] + '    '
                    message = message + str(j) + '\n'
                    k += 1
            tb = Text(baseframe, height=15, width=50)

            tb.pack(side='top', anchor='n', padx=25, pady=20)
            tb.insert(END, message)
            tb.config(bg='#2B2B2B', bd=0, fg='#A5B3C1', state=DISABLED)

    Button(showdoc, text='Show Details', command=showdoctors, width=25, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=2,
                                                                                                               column=0,
                                                                                                               columnspan=2)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME TO ADD DOCTORS
def add_doctor():
    def back():
        addoc.destroy()
        admin_mode_func()

    addoc = Frame()
    addoc.configure(bg='#2B2B2B')
    addoc.grid(row=0, column=0, sticky=NSEW)
    Button(addoc, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=back,
           width=50).grid(row=0, column=0, columnspan=2)
    addoc.tkraise()
    login.title('Add Doctor')
    login.geometry('350x240')
    login.maxsize(350, 240)
    login.minsize(350, 240)
    Label(addoc, text='Add Doctor Information ', bg='#2B2B2B', bd=0, fg='#FA3232',
          font=('Ariel Rounded Mt', 13, 'bold')).grid(row=1, column=0, columnspan=2, padx=20, pady=15)
    Label(addoc, text='Name : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=2, column=0, padx=20, pady=5)
    Label(addoc, text='Age : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=3, column=0, padx=20, pady=5)
    Label(addoc, text='Hospital : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=4, column=0, padx=20, pady=5)
    Label(addoc, text='Department : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=5, column=0, padx=20, pady=5)
    Label(addoc, text='Phone Number : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=6, column=0, padx=20, pady=5)
    docname = StringVar()
    docage = StringVar()
    dochospital = StringVar()
    docdept = StringVar()
    docphone = StringVar()
    Entry(addoc, textvariable=docname, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=2, column=1, padx=20,
                                                                                        pady=5)
    Entry(addoc, textvariable=docage, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=3, column=1, padx=20, pady=5)
    Entry(addoc, textvariable=dochospital, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=4, column=1, padx=20,
                                                                                            pady=5)
    Entry(addoc, textvariable=docdept, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=5, column=1, padx=20,
                                                                                        pady=5)
    Entry(addoc, textvariable=docphone, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=6, column=1, padx=20,
                                                                                         pady=5)

    def submitdocdetails():
        c1.execute(
            f'insert into doctor_details values("{docname.get()}","{docage.get()}","{dochospital.get()}","{docdept.get()}","{docphone.get()}")')
        conn.commit()
        tkmsg.showinfo('Successfully Submitted', f'Details about Doctor {docname.get()} successfully submitted')

    Button(addoc, text='Submit', command=submitdocdetails, bg='#3C3F41', bd=0, fg='#A5B3C1', width=50).grid(row=7,
                                                                                                            columnspan=2,
                                                                                                            pady=10)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME TO REMOVE DOCTORS
def remove_doctor():
    def back():
        remdoc.destroy()
        admin_mode_func()

    remdoc = Frame(login)
    remdoc.configure(bg='#2B2B2B')
    remdoc.grid(row=0, column=0, sticky=NSEW)
    Button(remdoc, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=back,
           width=57).grid(row=0, column=0, columnspan=2)
    remdoc.tkraise()
    login.title('Delete Doctor')
    login.geometry('402x136')
    login.maxsize(404, 136)
    login.minsize(404, 136)
    Label(remdoc, text='Which Doctor Do You Want To Remove? : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=1, column=0,
                                                                                                  padx=20, pady=20)
    remvar = StringVar(value='Select Doctor')
    listofdoc = []
    c1.execute('select Name from doctor_details')
    for i in c1.fetchall():
        listofdoc.append(str(i[0]))
    print(listofdoc)
    try:
        tempvar = OptionMenu(remdoc, remvar, *listofdoc)
        tempvar.grid(row=1, column=1, padx=10, pady=20)
        tempvar.configure(bg='#2B2B2B', bd=0, fg='#A5B3C1', activebackground='grey')

        def submit():
            yesno = tkmsg.askyesno('Are You Sure?',
                                   f'Are You Sure You Want To Delete {remvar.get()} From The Database?')
            if yesno == TRUE:
                c1.execute(f'delete from doctor_details where name="{remvar.get()}"')
                conn.commit()
                tkmsg.showinfo('Doctor Successfully Removed',
                               f'{remvar.get()} has been successfully removed from the database.')

            else:
                pass

        Button(remdoc, text='Delete Doctor', command=submit, width=57, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(
            pady=25,
            columnspan=2)
    except:
        pass
        remdoc.destroy()
        admin_mode_func()
        tkmsg.showinfo('ERROR', 'THERE ARE NO DOCTORS TO REMOVE! DOCTOR DATABASE IS EMPTY')


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME TO SHOW HOSPITALS
def show_hospitals():
    def back():
        showhosp.destroy()
        admin_mode_func()

    showhosp = Frame(login)
    showhosp.configure(bg='#2b2b2b')
    showhosp.grid(row=0, column=0, sticky=NSEW)
    showhosp.tkraise()
    login.geometry('500x500')
    login.maxsize(500, 500)
    login.minsize(500, 500)
    login.title('Hospitals')
    Button(showhosp, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=back, width=72).grid(row=0,
                                                                                                  column=0,
                                                                                                  columnspan=2)

    Label(showhosp, text='Which Hospital Do You Want To Look At ? : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=1, column=0,
                                                                                                        padx=20,
                                                                                                        pady=20)
    remvar = StringVar(value='Select Hospital')
    listofhosp = []
    for i in hospital.values():
        listofhosp.append(str(i))
    tempvar = OptionMenu(showhosp, remvar, *listofhosp)
    tempvar.grid(row=1, column=1, padx=10, pady=20)
    tempvar.configure(bg='#2B2B2B', bd=0, fg='#A5B3C1', activebackground='grey')

    def show():
        c1.execute(f'select * from {sub_table_name(remvar.get())}')
        x = c1.fetchall()
        j = 0
        for i in x:
            j += 1
            Label(showhosp, text=i[1], padx=10, pady=5, bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=j + 2, column=0)
            Label(showhosp, text=i[2], padx=10, pady=5, bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=j + 2, column=1)
            if j == 15:
                break

    Button(showhosp, text='Show Information', command=show, bg='#3C3F41', fg='#A5B3C1', width=60).grid(row=2, column=0,
                                                                                                       columnspan=2,
                                                                                                       padx=30)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME TO ADD PATIENTS
def add_patient():
    def back():
        addpat.destroy()
        admin_mode_func()

    addpat = Frame()
    addpat.configure(bg='#2B2B2B')
    addpat.grid(row=0, column=0, sticky=NSEW)
    Button(addpat, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=back,
           width=50).grid(row=0, column=0, columnspan=2)
    addpat.tkraise()
    login.title('Add Patient')
    login.geometry('350x267')
    login.maxsize(350, 267)
    login.minsize(350, 267)
    Label(addpat, text='Add Patient Information ', bg='#2B2B2B', bd=0, fg='#FA3232',
          font=('Ariel Rounded Mt', 13, 'bold')).grid(row=1, column=0, columnspan=2, padx=20, pady=15)
    Label(addpat, text='Name : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=2, column=0, padx=20, pady=5)
    Label(addpat, text='Age : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=3, column=0, padx=20, pady=5)
    Label(addpat, text='Hospital : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=4, column=0, padx=20, pady=5)
    Label(addpat, text='Service : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=5, column=0, padx=20, pady=5)
    Label(addpat, text='Phone Number : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=6, column=0, padx=20, pady=5)
    Label(addpat, text='Time : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=7, column=0, padx=20, pady=5)
    patname = StringVar()
    patage = StringVar()
    pathospital = StringVar()
    patserv = StringVar()
    patphone = StringVar()
    pattime = StringVar()
    Entry(addpat, textvariable=patname, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=2, column=1, padx=20,
                                                                                         pady=5)
    Entry(addpat, textvariable=patage, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=3, column=1, padx=20,
                                                                                        pady=5)
    Entry(addpat, textvariable=pathospital, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=4, column=1, padx=20,
                                                                                             pady=5)
    Entry(addpat, textvariable=patserv, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=5, column=1, padx=20,
                                                                                         pady=5)
    Entry(addpat, textvariable=patphone, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=6, column=1, padx=20,
                                                                                          pady=5)
    Entry(addpat, textvariable=pattime, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=7, column=1, padx=20,
                                                                                         pady=5)

    def submitpatdetails():
        c1.execute(
            f'insert into patient_details values("{patname.get()}","{patage.get()}","{pathospital.get()}","{patserv.get()}","{patphone.get()}","{pattime.get()}")')
        conn.commit()
        tkmsg.showinfo('Successfully Submitted', f'Details about Patient {patname.get()} successfully submitted')
        addpat.destroy()

    Button(addpat, text='Submit', command=submitpatdetails, bg='#3C3F41', bd=0, fg='#A5B3C1', width=50).grid(row=8,
                                                                                                             columnspan=2,
                                                                                                             pady=10)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME TO SHOW PATIENTS
def show_appointments():
    def back():
        showpat.destroy()
        admin_mode_func()

    showpat = Frame(login)
    login.title('Show Appointments')
    login.geometry('490x373')
    login.maxsize(490, 373)
    login.minsize(490, 373)
    showpat.configure(bg='#2B2B2B')
    showpat.grid(row=0, column=0, sticky=NSEW)

    Button(showpat, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=back, width=72).grid(row=0,
                                                                                                 column=0,
                                                                                                 columnspan=2)

    baseframe1 = Frame(showpat)
    baseframe1.configure(bg='#2B2B2B', width=450, height=300)
    baseframe1.grid(row=3, column=0, columnspan=2)
    patlist = ['Show All Patients']
    datalist = ['Name           ', 'Age            ', 'Hospital       ', 'Services       ', 'Phone Number   ',
                'Timing         ']
    c1.execute('select Name from patient_details')
    for i in c1.fetchall():
        patlist.append(i[0])
    patvar = StringVar(value='Select Patient')
    patients = OptionMenu(showpat, patvar, *patlist)

    patients.configure(bg='#2B2B2B', bd=0, fg='#A5B3C1', activebackground='grey')
    Label(showpat, text='Select Patient To See Details : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=1, column=0,
                                                                                                   padx=20, pady=10)
    patients.grid(row=1, column=1, pady=10)

    def showpatients():
        message = ''
        global tb1
        global sb1
        try:
            tb1.destroy()
            sb1.destroy()
        except:
            pass
        if patvar.get() == 'Show All Patients':
            c1.execute('select * from patient_details')
            x = c1.fetchall()
            for i in x:
                k = 0
                for j in i:
                    message = message + datalist[k] + '    '
                    message = message + str(j) + '\n'
                    k += 1
                message = message + '\n'
            sb1 = Scrollbar(baseframe1)
            sb1.pack(side='right', fill='y')
            tb1 = Text(baseframe1, height=15, width=50)
            tb1.config(yscrollcommand=sb1.set)
            sb1.config(command=tb1.yview)
            tb1.pack(side='top', anchor='n', padx=25, pady=20)
            tb1.replace(0.0, END, message)
            tb1.config(bg='#2B2B2B', bd=0, fg='#A5B3C1', state=DISABLED)

        else:
            c1.execute(f'select * from patient_details where name="{patvar.get()}"')
            x = c1.fetchall()
            k = 0
            for i in x:
                for j in i:
                    message = message + datalist[k] + '    '
                    message = message + str(j) + '\n'
                    k += 1
            tb1 = Text(baseframe1, height=15, width=50)

            tb1.pack(side='top', anchor='n', padx=25, pady=20)
            tb1.insert(END, message)
            tb1.config(bg='#2B2B2B', bd=0, fg='#A5B3C1', state=DISABLED)

    Button(showpat, text='Show Details', command=showpatients, width=25, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=2,
                                                                                                                column=0,
                                                                                                                columnspan=2)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME TO SHOW PATIENTS
def show_patients_profiles():
    def back():
        showppf.destroy()
        admin_mode_func()

    showppf = Frame(login)
    login.title('Patient Profiles')
    login.geometry('490x373')
    login.maxsize(490, 373)
    login.minsize(490, 373)
    showppf.configure(bg='#2B2B2B')
    showppf.grid(row=0, column=0, sticky=NSEW)

    Button(showppf, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=back, width=72).grid(row=0,
                                                                                                 column=0,
                                                                                                 columnspan=2)

    baseframe1 = Frame(showppf)
    baseframe1.configure(bg='#2B2B2B', width=450, height=300)
    baseframe1.grid(row=3, column=0, columnspan=2)
    patlist = ['Show All Patients']
    datalist = ['Username           ', 'Name               ', 'Age                ', 'Phone Number       ']
    c1.execute('select Name from patient_logins')
    for i in c1.fetchall():
        patlist.append(i[0])
    ppfvar = StringVar(value='Select Patient')
    patients = OptionMenu(showppf, ppfvar, *patlist)

    patients.configure(bg='#2B2B2B', bd=0, fg='#A5B3C1', activebackground='grey')
    Label(showppf, text='Select Patient To See Details : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=1, column=0,
                                                                                                   padx=20, pady=10)
    patients.grid(row=1, column=1, pady=10)

    def show0patients():
        message = ''
        global tb1
        global sb1
        try:
            tb1.destroy()
            sb1.destroy()
        except:
            pass
        if ppfvar.get() == 'Show All Patients':
            c1.execute('select * from patient_logins')
            x = c1.fetchall()
            for i in x:
                k = 0
                for j in i:
                    message = message + datalist[k] + '    '
                    message = message + str(j) + '\n'
                    k += 1
                message = message + '\n'
            sb1 = Scrollbar(baseframe1)
            sb1.pack(side='right', fill='y')
            tb1 = Text(baseframe1, height=15, width=50)
            tb1.config(yscrollcommand=sb1.set)
            sb1.config(command=tb1.yview)
            tb1.pack(side='top', anchor='n', padx=25, pady=20)
            tb1.replace(0.0, END, message)
            tb1.config(bg='#2B2B2B', bd=0, fg='#A5B3C1', state=DISABLED)

        else:
            c1.execute(f'select * from patient_logins where name="{ppfvar.get()}"')
            x = c1.fetchall()
            k = 0
            for i in x:
                for j in i:
                    message = message + datalist[k] + '    '
                    message = message + str(j) + '\n'
                    k += 1
            tb1 = Text(baseframe1, height=15, width=50)

            tb1.pack(side='top', anchor='n', padx=25, pady=20)
            tb1.insert(END, message)
            tb1.config(bg='#2B2B2B', bd=0, fg='#A5B3C1', state=DISABLED)

    Button(showppf, text='Show Details', command=show0patients, width=25, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=2,
                                                                                                                 column=0,
                                                                                                                 columnspan=2)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME TO REMOVE PATIENTS
def remove_patient():
    def back():
        rempat.destroy()
        admin_mode_func()

    rempat = Frame(login)
    login.title('Show Doctors')
    login.geometry('470x350')
    login.maxsize(470, 350)
    login.minsize(470, 350)
    rempat.configure(bg='#2B2B2B')
    rempat.grid(row=0, column=0, sticky=NSEW)

    Button(rempat, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=back, width=72).grid(row=0,
                                                                                                column=0,
                                                                                                columnspan=2)
    Label(rempat, text='Which Patient Do You Want To Remove? : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=1, column=0,
                                                                                                   padx=20, pady=20)
    remvar = StringVar(value='Select Patient')
    listofpat = []
    c1.execute('select Name from patient_details')
    for i in c1.fetchall():
        listofpat.append(str(i[0]))
    try:
        tempvar = OptionMenu(rempat, remvar, *listofpat)
        tempvar.grid(row=1, column=1, padx=10, pady=20)
        tempvar.configure(bg='#2B2B2B', bd=0, fg='#A5B3C1', activebackground='grey')

        def submit():
            yesno = tkmsg.askyesno('Are You Sure?',
                                   f'Are You Sure You Want To Delete {remvar.get()} From The Database?')
            if yesno == TRUE:
                c1.execute(f'delete from patient_details where name="{remvar.get()}"')
                conn.commit()
                tkmsg.showinfo('Patient Successfully Removed',
                               f'{remvar.get()} has been successfully removed from the database.')
            else:
                pass

        Button(rempat, text='Delete Patient', command=submit, width=50, bg='#2B2B2B', fg='#A5B3C1').grid(padx=15,
                                                                                                         pady=25,
                                                                                                         columnspan=2)
    except:
        pass
        rempat.destroy()
        admin_mode_func()
        tkmsg.showinfo('ERROR', 'THERE ARE NO PATIENTS TO REMOVE! PATIENT DATABASE IS EMPTY')


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME TO REMOVE PATIENT PROFILES
def remove_patient_profile():
    def back():
        rempff.destroy()
        admin_mode_func()

    rempff = Frame(login)
    login.title('Show Doctors')
    login.geometry('500x350')
    login.maxsize(500, 350)
    login.minsize(500, 350)
    rempff.configure(bg='#2B2B2B')
    rempff.grid(row=0, column=0, sticky=NSEW)

    Button(rempff, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=back, width=72).grid(row=0,
                                                                                                column=0,
                                                                                                columnspan=2)
    Label(rempff, text='Which Patient Do You Want To Remove? : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=1, column=0,
                                                                                                   padx=20, pady=20)
    remvar = StringVar(value='Select Patient')
    listofpat = []
    c1.execute('select Name from patient_logins')
    for i in c1.fetchall():
        listofpat.append(str(i[0]))
    try:
        tempvar = OptionMenu(rempff, remvar, *listofpat)
        tempvar.grid(row=1, column=1, padx=10, pady=20)
        tempvar.configure(bg='#2B2B2B', bd=0, fg='#A5B3C1', activebackground='grey')

        def submit():
            yesno = tkmsg.askyesno('Are You Sure?',
                                   f'Are You Sure You Want To Delete {remvar.get()} From The Database?')
            if yesno == TRUE:
                c1.execute(f'delete from patient_logins where Name="{remvar.get()}"')
                conn.commit()
                tkmsg.showinfo('Patient Successfully Removed',
                               f'{remvar.get()} has been successfully removed from the database.')
            else:
                pass

        Button(rempff, text='Delete Patient', command=submit, width=50, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(padx=15,
                                                                                                               pady=25,
                                                                                                               columnspan=2)
    except:
        pass
        rempff.destroy()
        admin_mode_func()
        tkmsg.showinfo('ERROR', 'THERE ARE NO PATIENTS TO REMOVE! PATIENT DATABASE IS EMPTY')


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME TO ADD PATIENT PROFILES
def add_patient_profiles():
    def back():
        addpff.destroy()
        admin_mode_func()

    addpff = Frame()
    addpff.configure(bg='#2B2B2B')
    addpff.grid(row=0, column=0, sticky=NSEW)
    Button(addpff, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=back,
           width=50).grid(row=0, column=0, columnspan=2)
    addpff.tkraise()
    login.title('Add Patient')
    login.geometry('350x267')
    login.maxsize(350, 267)
    login.minsize(350, 267)
    Label(addpff, text='Add Patient Information ', bg='#2B2B2B', bd=0, fg='#FA3232',
          font=('Ariel Rounded Mt', 13, 'bold')).grid(row=1, column=0, columnspan=2, padx=20, pady=15)
    Label(addpff, text='Username : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=2, column=0, padx=20, pady=5)
    Label(addpff, text='Password : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=3, column=0, padx=20, pady=5)
    Label(addpff, text='Name : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=4, column=0, padx=20, pady=5)
    Label(addpff, text='Age : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=5, column=0, padx=20, pady=5)
    Label(addpff, text='Phone Number : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=6, column=0, padx=20, pady=5)
    patfname = StringVar()
    patfage = StringVar()
    patfhospital = StringVar()
    patfserv = StringVar()
    patfphone = StringVar()
    Entry(addpff, textvariable=patfname, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=2, column=1, padx=20,
                                                                                          pady=5)
    Entry(addpff, textvariable=patfage, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=3, column=1, padx=20,
                                                                                         pady=5)
    Entry(addpff, textvariable=patfhospital, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=4, column=1,
                                                                                              padx=20,
                                                                                              pady=5)
    Entry(addpff, textvariable=patfserv, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=5, column=1, padx=20,
                                                                                          pady=5)
    Entry(addpff, textvariable=patfphone, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=6, column=1, padx=20,
                                                                                           pady=5)

    def submitpatdetails():
        c1.execute(
            f'insert into patient_logins values("{patfname.get()}","{patfhospital.get()}","{patfserv.get()}","{patfphone.get()}")')
        conn.commit()
        with open('hospitalusrpw.csv', 'a', newline='') as f:
            pencil = csv.writer(f)
            pencil.writerow((patfname.get(), patfage.get()))
            f.close()
        tkmsg.showinfo('Successfully Submitted', f'Details about Patient {patfname.get()} successfully submitted')

    Button(addpff, text='Submit', command=submitpatdetails, bg='#3C3F41', bd=0, fg='#A5B3C1', width=50).grid(row=8,
                                                                                                             columnspan=2,
                                                                                                             pady=10)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FRAME TO UPDATE ADMIN PROFILE PASSWORD
def admin_update_pw():
    global adminusername
    global adminpassword

    def back():
        pwd.destroy()
        admin_mode_func()

    pwd = Frame(login)
    pwd.configure(bg='#2B2B2B')
    login.title('Update Password')
    login.geometry('450x310')
    login.maxsize(450, 310)
    login.minsize(450, 310)
    pwd.grid(row=0, column=0, sticky=NSEW)
    pwd.tkraise()
    Button(pwd, text='<Back', bg='#3C3F41', bd=0, fg='#A5B3C1', command=back,
           width=64).grid(row=0, column=0, columnspan=2)

    Label(pwd, text='PASSWORD UPDATE', font=('Ariel Rounded Mt', 16, 'bold'), bg='#2B2B2B', fg='#FA3232') \
        .grid(row=1, column=0, columnspan=2, pady=10)
    Label(pwd, text='Old Password : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=2, column=0, pady=10)
    Label(pwd, text='New Password : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=3, column=0, pady=10)
    Label(pwd, text='Confirm New Password : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=4, column=0, pady=10)
    Button(pwd, text='Update Password', bg='#3C3F41', bd=0, fg='#A5B3C1', width=50).grid(row=5, column=0,
                                                                                         columnspan=2,
                                                                                         pady=10)

    opwd = StringVar()
    npwd = StringVar()
    cnpwd = StringVar()

    Entry(pwd, textvariable=opwd, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=2, column=1, pady=10)
    Entry(pwd, textvariable=npwd, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=3, column=1, pady=10)
    Entry(pwd, textvariable=cnpwd, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=4, column=1, pady=10)

    def updatepwd():
        if opwd.get() == adminpassword:
            if npwd.get() == cnpwd.get():
                book = []
                with open('hospitaladminusrpw.csv', 'r')as f:
                    for i in csv.reader(f):
                        book.append(i)
                    f.close()
                with open('hospitaladminusrpw.csv', 'w', newline='') as f:
                    pencil = csv.writer(f)
                    for i in book:
                        if i[0] != adminusername:
                            pencil.writerow(i)
                        else:
                            pencil.writerow((adminusername, npwd.get()))
                    f.close()

                tkmsg.showinfo('Successfully Updated', 'Password Has Been Updated Successfully')
            else:
                tkmsg.showerror('Password Error', 'Password Not Confirmed Correctly')
        else:
            tkmsg.showerror('Password Error', 'Old Password Is Incorrect')

    Button(pwd, text='Update Password', bg='#3C3F41', bd=0, fg='#A5B3C1', width=50, command=updatepwd) \
        .grid(row=5, column=0, columnspan=2, pady=10)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# ADMIN MODE PAGE
def admin_mode_func():
    def back():
        admin_mode.destroy()
        admin_login_page()

    admin_mode = Frame(login)
    admin_mode.configure(bg='#2B2B2B')
    admin_mode.grid(row=0, column=0, sticky=NSEW)
    admin_mode.tkraise()
    login.title('Admin Mode')
    login.geometry('590x480')
    login.maxsize(590, 480)
    login.minsize(590, 480)
    mb = Menubutton(admin_mode, text='Options', bg='#3C3F41', bd=0, fg='#A5B3C1',
                    width=100, activebackground='#45484A')
    mb.grid(row=0, column=0, columnspan=3)
    mb_menu = Menu(mb, tearoff=0)
    mb['menu'] = mb_menu
    mb_menu.add_command(label='Change Password', command=admin_update_pw)
    mb_menu.add_command(label='Admin Key Options', command=adminkey)
    mb_menu.add_command(label='Log Out', command=back)

    Label(admin_mode, text="                                                ", bg='#2B2B2B', fg='#A5B3C1').grid(
        row=1,
        column=0)
    Label(admin_mode, text="                                                ", bg='#2B2B2B', fg='#A5B3C1').grid(
        row=1,
        column=2)
    Label(admin_mode, text="                                                ", bg='#2B2B2B', fg='#A5B3C1').grid(
        row=1,
        column=0,
        columnspan=3)
    Label(admin_mode, text="                                                ", bg='#2B2B2B', fg='#A5B3C1').grid(
        row=11,
        column=0,
        columnspan=3)
    Button(admin_mode, text='ADD HOSPITAL', width=50, bd=0, command=add_hospital, bg='#3C3F41', fg='#A5B3C1').grid(
        row=2,
        column=0,
        columnspan=3,
        pady=5)
    Button(admin_mode, text='REMOVE HOSPITAL', width=50, bd=0, command=remove_hospital, bg='#3C3F41',
           fg='#A5B3C1').grid(
        row=3, column=0,
        columnspan=3, pady=5)
    Button(admin_mode, text='UPDATE HOSPITAL DATA', width=50, bd=0, bg='#3C3F41', fg='#A5B3C1',
           command=update_hospital).grid(
        row=4, column=0,
        columnspan=3, pady=5)
    Button(admin_mode, text='SHOW DOCTORS', width=50, bd=0, bg='#3C3F41', fg='#A5B3C1',
           command=show_doctors_admin).grid(
        row=8, column=0, columnspan=3,
        pady=5)
    Button(admin_mode, text='ADD DOCTOR', width=50, bd=0, bg='#3C3F41', fg='#A5B3C1', command=add_doctor).grid(
        row=6,
        column=0,
        columnspan=3,
        pady=5)
    Button(admin_mode, text='REMOVE DOCTOR', width=50, bd=0, bg='#3C3F41', fg='#A5B3C1',
           command=remove_doctor).grid(
        row=7, column=0, columnspan=3,
        pady=5)
    Button(admin_mode, text='SHOW HOSPITALS', width=50, bd=0, bg='#3C3F41', fg='#A5B3C1',
           command=show_hospitals).grid(
        row=5,
        column=0,
        pady=5,
        columnspan=3)
    Button(admin_mode, text='SHOW APPOINTMENTS', width=50, bd=0, bg='#3C3F41', fg='#A5B3C1',
           command=show_appointments).grid(
        row=12, column=0,
        columnspan=3,
        pady=5)
    Button(admin_mode, text='ADD APPOINTMENT', width=50, bd=0, bg='#3C3F41', fg='#A5B3C1', command=add_patient).grid(
        row=13, column=0,
        columnspan=3,
        pady=5)
    Button(admin_mode, text='REMOVE APPOINTMENT', width=50, bd=0, bg='#3C3F41', fg='#A5B3C1',
           command=remove_patient).grid(
        row=14, column=0,
        columnspan=3,
        pady=5)
    Button(admin_mode, text='SHOW PATIENT PROFILES', width=50, bd=0, bg='#3C3F41', fg='#A5B3C1',
           command=show_patients_profiles).grid(
        row=9, column=0,
        columnspan=3,
        pady=5)
    Button(admin_mode, text='REMOVE PATIENT PROFILE', width=50, bd=0, bg='#3C3F41', fg='#A5B3C1',
           command=remove_patient_profile).grid(
        row=11, column=0,
        columnspan=3,
        pady=5)
    Button(admin_mode, text='ADD PATIENT PROFILES', width=50, bd=0, bg='#3C3F41', fg='#A5B3C1',
           command=add_patient_profiles).grid(
        row=10, column=0,
        columnspan=3,
        pady=5)


first_frame()

login.mainloop()

