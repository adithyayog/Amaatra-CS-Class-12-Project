#Completed GUI version of the Admin Mode
#Add Hospital, Remove Hospital, Update Hospital, Show Hospitals
#Add Doctor, Remove Doctor, Show Doctors
#Add Patients, Remove Patients, Show Patients
#Back to Home Screen



from tkinter import *
from tkinter import messagebox as tkmsg
import mysql.connector as sql
import csv

# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
#  CONNECTING TO MYSQL DATABASE
conn = sql.connect(host='localhost', user='root', passwd='amaatra', database='project')
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

# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# TKINTER PROGRAMMING BEGINS

root = Tk()


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FUNCTION TO GET CORRESPONDING TABLE NAME FROM HOSPITAL NAME
def sub_table_name(hospital_name):
    print(hospital_name)
    for key, value in hospital.items():
        if value == hospital_name:
            return key


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FUNCTIONS TO ADD HOSPITALS

def add_hospital():
    # -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
    add_hospital_toplevel = Toplevel()

    add_hospital_toplevel.configure(bg='#2B2B2B')
    add_hospital_toplevel.title('Add Hospital')

    def backbutton():
        print(add_hospital_toplevel.destroy())

    # =====X=====X=====X=====X=====X=====X=====X=====X=====X=====X=====X=====X=====X=====X=====X=====X=====X=====X=====X=====
    # CREATING A MENU
    back = Menu(add_hospital_toplevel)
    back.add_command(label='<<Back<<', command=backbutton)
    add_hospital_toplevel.config(menu=back)
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
    Label(add_hospital_toplevel, text='Name : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=1, column=0)
    Label(add_hospital_toplevel, text='Address : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=2, column=0)
    Label(add_hospital_toplevel, text='Area : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=3, column=0)
    Label(add_hospital_toplevel, text='Consultation Cost : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=4,
                                                                                                                column=0)
    Label(add_hospital_toplevel, text='Contact : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=5, column=0)
    Label(add_hospital_toplevel, text='Beds : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=6, column=0)
    Label(add_hospital_toplevel, text='Cost of Beds : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=7,
                                                                                                           column=0)
    Label(add_hospital_toplevel, text='Ambulance Service : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=8,
                                                                                                                column=0)
    Label(add_hospital_toplevel, text='Oxygen Available : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=9,
                                                                                                               column=0)
    Label(add_hospital_toplevel, text='Covid Vaccine Available : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(
        row=10,
        column=0)
    Label(add_hospital_toplevel, text='CT SCAN Available : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=11,
                                                                                                                column=0)
    Label(add_hospital_toplevel, text='MRI SCAN Available : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(row=13,
                                                                                                                 column=0)
    Label(add_hospital_toplevel, text='COVID TEST Available : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(
        row=15,
        column=0)
    Label(add_hospital_toplevel, text='XRAY SCAN Available : ', bg='#2B2B2B', fg='#A5B3C1', padx=20, pady=5).grid(
        row=17,
        column=0)
    Entry(add_hospital_toplevel, textvariable=name, bg='#3C3F41', fg='#A5B3C1').grid(row=1, column=1, padx=20, pady=5)
    Entry(add_hospital_toplevel, textvariable=address, bg='#3C3F41', fg='#A5B3C1').grid(row=2, column=1, padx=20,
                                                                                        pady=5)
    Entry(add_hospital_toplevel, textvariable=area, bg='#3C3F41', fg='#A5B3C1').grid(row=3, column=1, padx=20, pady=5)
    Entry(add_hospital_toplevel, textvariable=consult_cost, bg='#3C3F41', fg='#A5B3C1').grid(row=4, column=1, padx=20,
                                                                                             pady=5)
    Entry(add_hospital_toplevel, textvariable=contact, bg='#3C3F41', fg='#A5B3C1').grid(row=5, column=1, padx=20,
                                                                                        pady=5)
    Entry(add_hospital_toplevel, textvariable=beds, bg='#3C3F41', fg='#A5B3C1').grid(row=6, column=1, padx=20, pady=5)
    Entry(add_hospital_toplevel, textvariable=beds_cost, bg='#3C3F41', fg='#A5B3C1').grid(row=7, column=1, padx=20,
                                                                                          pady=5)
    Entry(add_hospital_toplevel, textvariable=o2, bg='#3C3F41', fg='#A5B3C1').grid(row=8, column=1, padx=20, pady=5)
    Entry(add_hospital_toplevel, textvariable=amb, bg='#3C3F41', fg='#A5B3C1').grid(row=9, column=1, padx=20, pady=5)
    Entry(add_hospital_toplevel, textvariable=vaccine, bg='#3C3F41', fg='#A5B3C1').grid(row=10, column=1, padx=20,
                                                                                        pady=5)

    def costofct():
        global ct
        ct = 'Yes'
        Label(add_hospital_toplevel, text='Cost of CT SCAN : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=12, column=0)
        Entry(add_hospital_toplevel, textvariable=ct_cost, bg='#3C3F41', fg='#A5B3C1').grid(row=12, column=1)

    def costofmri():
        global mri
        mri = 'Yes'
        Label(add_hospital_toplevel, text='Cost of MRI SCAN : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=14, column=0)
        Entry(add_hospital_toplevel, textvariable=mri_cost, bg='#3C3F41', fg='#A5B3C1').grid(row=14, column=1)

    def costofcov():
        global cov
        cov = 'Yes'
        Label(add_hospital_toplevel, text='Cost of COVID TEST : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=16, column=0)
        Entry(add_hospital_toplevel, textvariable=cov_cost, bg='#3C3F41', fg='#A5B3C1').grid(row=16, column=1)

    def costofxray():
        global xray
        xray = 'Yes'
        Label(add_hospital_toplevel, text='Cost of XRAY SCAN : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=18, column=0)
        Entry(add_hospital_toplevel, textvariable=xray_cost, bg='#3C3F41', fg='#A5B3C1').grid(row=18, column=1)

    Checkbutton(add_hospital_toplevel, text=' YES ', bg='#2B2B2B', fg='#A5B3C1', command=costofct, padx=20,
                pady=5).grid(row=11,
                             column=1)
    Checkbutton(add_hospital_toplevel, text=' YES ', bg='#2B2B2B', fg='#A5B3C1', command=costofmri, padx=20,
                pady=5).grid(row=13,
                             column=1)
    Checkbutton(add_hospital_toplevel, text=' YES ', bg='#2B2B2B', fg='#A5B3C1', command=costofcov, padx=20,
                pady=5).grid(row=15,
                             column=1)
    Checkbutton(add_hospital_toplevel, text=' YES ', bg='#2B2B2B', fg='#A5B3C1', command=costofxray, padx=20,
                pady=5).grid(
        row=17,
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
        add_hospital_toplevel.destroy()

    Button(add_hospital_toplevel, text='SUBMIT', command=submit, padx=120, bg='#5b5b5b', fg='#A5B3C1',
           activebackground='#2B2B2B').grid(row=19, column=0,
                                            columnspan=2,
                                            padx=20, pady=5)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FUNCTION TO REMOVE HOSPITALS

def remove_hospital():
    rem = Toplevel()
    rem.configure(bg='#2B2B2B')
    rem.title('Remove Hospital')
    Label(rem, text='Which Hospital Do You Want To Remove? : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=0, column=0,
                                                                                                 padx=20, pady=20)
    remvar = StringVar(value='Select Hospital')
    listofhosp = []
    for i in hospital.values():
        listofhosp.append(str(i))
    tempvar = OptionMenu(rem, remvar, *listofhosp)
    tempvar.grid(row=0, column=1, padx=10, pady=20)
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

    Button(rem, text='Delete Hospital', command=submit, width=50, bg='#2B2B2B', fg='#A5B3C1').grid(padx=15, pady=25,
                                                                                                   columnspan=2)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FUNCTION TO UPDATE DATABASE

def update_hospital():
    upd = Toplevel()
    upd.configure(bg='#2B2B2B')
    upd.title('Update Hospital Information')
    updvar = StringVar(value='Select Data Name')
    updtextvar = StringVar()
    updlist = ['Name', 'Location', 'Area', 'Contact Details', 'Consultation Cost', 'Beds Availability', 'Cost Of Beds',
               'Oxygen Availability', 'Ambulance Service Cost', 'Covid Vaccines Availability', 'CT SCAN Availability',
               'Cost of CT SCAN', 'MRI SCAN Availability', 'Cost of MRI SCAN', 'COVID TEST Availability',
               'Cost of COVID TEST', 'X-RAY SCAN Availability', 'Cost of X-RAY SCAN']
    remvar = StringVar(value='Select Hospital')
    listofhosp = []
    for i in hospital.values():
        listofhosp.append(str(i))
    tempvar = OptionMenu(upd, remvar, *listofhosp)
    tempvar.grid(row=0, column=1, padx=10, pady=20)
    tempvar.configure(bg='#2B2B2B', bd=0, fg='#A5B3C1', activebackground='grey')
    Label(upd, text='Which Hospital Do You Want To Update ? :', bg='#2B2B2B', fg='#A5B3C1').grid(row=0, column=0,
                                                                                                 padx=20,
                                                                                                 pady=20)
    tempvar = OptionMenu(upd, updvar, *updlist)
    tempvar.configure(bg='#2B2B2B', fg='#A5B3C1')
    tempvar.grid(row=1, column=1, padx=10, pady=10)
    Label(upd, text='What Do You Want To Update ? :', bg='#2B2B2B', fg='#A5B3C1').grid(row=1, column=0, padx=20,
                                                                                       pady=10)
    Label(upd, text='What Is The New Data ? :', bg='#2B2B2B', fg='#A5B3C1').grid(row=2, column=0, padx=20, pady=10)
    Entry(upd, textvariable=updtextvar, bg='#3C3F41', fg='#A5B3C1').grid(row=2, column=1, padx=10, pady=10)

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

    Button(upd, text='Update', command=update, bg='#2B2B2B', fg='#A5B3C1', width=50).grid(row=3, column=0, padx=10,
                                                                                          pady=10, columnspan=2)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FUNCTION TO SHOW HOSPITALS

def show_hospitals():
    showhosp = Toplevel()
    showhosp.configure(bg='#2b2b2b')
    showhosp.geometry('500x500')
    Label(showhosp, text='Which Hospital Do You Want To Look At ? : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=0, column=0,
                                                                                                        padx=20,
                                                                                                        pady=20)
    remvar = StringVar(value='Select Hospital')
    listofhosp = []
    for i in hospital.values():
        listofhosp.append(str(i))
    tempvar = OptionMenu(showhosp, remvar, *listofhosp)
    tempvar.grid(row=0, column=1, padx=10, pady=20)
    tempvar.configure(bg='#2B2B2B', bd=0, fg='#A5B3C1', activebackground='grey')

    def show():
        c1.execute(f'select * from {sub_table_name(remvar.get())}')
        x = c1.fetchall()
        j = -1
        for i in x:
            j += 1
            Label(showhosp, text=i[1], padx=10, pady=5, bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=j + 2, column=0)
            Label(showhosp, text=i[2], padx=10, pady=5, bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=j + 2, column=1)
            if j == 15:
                break

    Button(showhosp, text='Show Information', command=show, bg='#3C3F41', fg='#A5B3C1', width=60).grid(row=1, column=0,
                                                                                                       columnspan=2,
                                                                                                       padx=30)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FUNCTION TO SHOW DOCTORS

def show_doctors():
    showdoc = Toplevel()
    showdoc.title('Show Doctors')
    showdoc.geometry('470x350')
    showdoc.maxsize(470, 350)
    showdoc.minsize(470, 350)
    showdoc.configure(bg='#2B2B2B')
    baseframe = Frame(showdoc)
    baseframe.configure(bg='#2B2B2B', width=450, height=300)
    baseframe.grid(row=2, column=0, columnspan=2)
    doclist = ['Show All Doctors']
    datalist = ['Name           ', 'Age            ', 'Hospital       ', 'Department     ', 'Phone Number   ', 'x']
    c1.execute('select Name from doctor_details')
    for i in c1.fetchall():
        doclist.append(i[0])
    docvar = StringVar(value='Select Doctor')
    doctors = OptionMenu(showdoc, docvar, *doclist)

    doctors.configure(bg='#2B2B2B', bd=0, fg='#A5B3C1', activebackground='grey')
    Label(showdoc, text='Select Doctor To See Details : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=0, column=0,
                                                                                                  padx=20, pady=10)
    doctors.grid(row=0, column=1, pady=10)

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
            sb.pack(side='right', fill='y')
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

    Button(showdoc, text='Show Details', command=showdoctors, width=25, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=1,
                                                                                                               column=0,
                                                                                                               columnspan=2)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FUNCTION TO ADD DOCTORS

def add_doctor():
    addoc = Toplevel()
    addoc.title('Add Doctor')
    addoc.configure(bg='#2B2B2B')

    Label(addoc, text='Name : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=0, column=0, padx=20, pady=5)
    Label(addoc, text='Age : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=1, column=0, padx=20, pady=5)
    Label(addoc, text='Hospital : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=2, column=0, padx=20, pady=5)
    Label(addoc, text='Department : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=3, column=0, padx=20, pady=5)
    Label(addoc, text='Phone Number : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=4, column=0, padx=20, pady=5)
    docname = StringVar()
    docage = StringVar()
    dochospital = StringVar()
    docdept = StringVar()
    docphone = StringVar()
    Entry(addoc, textvariable=docname, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=0, column=1, padx=20,
                                                                                        pady=5)
    Entry(addoc, textvariable=docage, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=1, column=1, padx=20, pady=5)
    Entry(addoc, textvariable=dochospital, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=2, column=1, padx=20,
                                                                                            pady=5)
    Entry(addoc, textvariable=docdept, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=3, column=1, padx=20,
                                                                                        pady=5)
    Entry(addoc, textvariable=docphone, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=4, column=1, padx=20,
                                                                                         pady=5)

    def submitdocdetails():
        c1.execute(
            f'insert into doctor_details values("{docname.get()}","{docage.get()}","{dochospital.get()}","{docdept.get()}","{docphone.get()}")')
        conn.commit()
        tkmsg.showinfo('Successfully Submitted', f'Details about Doctor {docname.get()} successfully submitted')
        addoc.destroy()

    Button(addoc, text='Submit', command=submitdocdetails, bg='#3C3F41', bd=0, fg='#A5B3C1', width=40).grid(row=5,
                                                                                                            columnspan=2,
                                                                                                            pady=10)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FUNCTION TO REMOVE DOCTORS

def remove_doctor():
    remdoc = Toplevel()
    remdoc.configure(bg='#2B2B2B')
    remdoc.title('Remove Doctor')
    Label(remdoc, text='Which Doctor Do You Want To Remove? : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=0, column=0,
                                                                                                  padx=20, pady=20)
    remvar = StringVar(value='Select Doctor')
    listofdoc = []
    c1.execute('select Name from doctor_details')
    for i in c1.fetchall():
        listofdoc.append(str(i[0]))
    print(listofdoc)
    try:
        tempvar = OptionMenu(remdoc, remvar, *listofdoc)
        tempvar.grid(row=0, column=1, padx=10, pady=20)
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

        Button(remdoc, text='Delete Doctor', command=submit, width=50, bg='#2B2B2B', fg='#A5B3C1').grid(padx=15,
                                                                                                         pady=25,
                                                                                                         columnspan=2)
    except:
        pass
        remdoc.destroy()
        tkmsg.showinfo('ERROR','THERE ARE NO DOCTORS TO REMOVE! DOCTOR DATABASE IS EMPTY')


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FUNCTION TO SHOW PATIENTS

def show_patients():
    showpat = Toplevel()
    showpat.title('Show Doctors')
    showpat.geometry('470x350')
    showpat.maxsize(470, 350)
    showpat.minsize(470, 350)
    showpat.configure(bg='#2B2B2B')
    baseframe1 = Frame(showpat)
    baseframe1.configure(bg='#2B2B2B', width=450, height=300)
    baseframe1.grid(row=2, column=0, columnspan=2)
    patlist = ['Show All Patients']
    datalist = ['Name           ', 'Age            ', 'Hospital       ', 'Services       ', 'Phone Number   ',
                'Timing         ']
    c1.execute('select Name from patient_details')
    for i in c1.fetchall():
        patlist.append(i[0])
    patvar = StringVar(value='Select Patient')
    patients = OptionMenu(showpat, patvar, *patlist)

    patients.configure(bg='#2B2B2B', bd=0, fg='#A5B3C1', activebackground='grey')
    Label(showpat, text='Select Doctor To See Details : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=0, column=0,
                                                                                                  padx=20, pady=10)
    patients.grid(row=0, column=1, pady=10)

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

    Button(showpat, text='Show Details', command=showpatients, width=25, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=1,
                                                                                                                column=0,
                                                                                                                columnspan=2)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FUNCTION TO ADD PATIENTS

def add_patient():
    addpat = Toplevel()
    addpat.title('Add Doctor')
    addpat.configure(bg='#2B2B2B')

    Label(addpat, text='Name : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=0, column=0, padx=20, pady=5)
    Label(addpat, text='Age : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=1, column=0, padx=20, pady=5)
    Label(addpat, text='Hospital : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=2, column=0, padx=20, pady=5)
    Label(addpat, text='Service : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=3, column=0, padx=20, pady=5)
    Label(addpat, text='Phone Number : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=4, column=0, padx=20, pady=5)
    Label(addpat, text='Time : ', bg='#2B2B2B', bd=0, fg='#A5B3C1').grid(row=5, column=0, padx=20, pady=5)
    patname = StringVar()
    patage = StringVar()
    pathospital = StringVar()
    patserv = StringVar()
    patphone = StringVar()
    pattime = StringVar()
    Entry(addpat, textvariable=patname, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=0, column=1, padx=20,
                                                                                         pady=5)
    Entry(addpat, textvariable=patage, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=1, column=1, padx=20,
                                                                                        pady=5)
    Entry(addpat, textvariable=pathospital, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=2, column=1, padx=20,
                                                                                             pady=5)
    Entry(addpat, textvariable=patserv, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=3, column=1, padx=20,
                                                                                         pady=5)
    Entry(addpat, textvariable=patphone, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=4, column=1, padx=20,
                                                                                          pady=5)
    Entry(addpat, textvariable=pattime, width=30, bg='#3C3F41', bd=0, fg='#A5B3C1').grid(row=5, column=1, padx=20,
                                                                                         pady=5)

    def submitpatdetails():
        c1.execute(
            f'insert into patient_details values("{patname.get()}","{patage.get()}","{pathospital.get()}","{patserv.get()}","{patphone.get()}","{pattime.get()}")')
        conn.commit()
        tkmsg.showinfo('Successfully Submitted', f'Details about Patient {patname.get()} successfully submitted')
        addpat.destroy()

    Button(addpat, text='Submit', command=submitpatdetails, bg='#3C3F41', bd=0, fg='#A5B3C1', width=40).grid(row=6,
                                                                                                             columnspan=2,
                                                                                                             pady=10)


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# FUNCTION TO REMOVE PATIENTS

def remove_patient():
    rempat = Toplevel()
    rempat.configure(bg='#2B2B2B')
    rempat.title('Remove Patient')
    Label(rempat, text='Which Patient Do You Want To Remove? : ', bg='#2B2B2B', fg='#A5B3C1').grid(row=0, column=0,
                                                                                                  padx=20, pady=20)
    remvar = StringVar(value='Select Patient')
    listofpat = []
    c1.execute('select Name from patient_details')
    for i in c1.fetchall():
        listofpat.append(str(i[0]))
    try:
        tempvar = OptionMenu(rempat, remvar, *listofpat)
        tempvar.grid(row=0, column=1, padx=10, pady=20)
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
        tkmsg.showinfo('ERROR', 'THERE ARE NO PATIENTS TO REMOVE! PATIENT DATABASE IS EMPTY')


# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# ADMIN MODE
def admin_mode_func():
    admin_mode = Toplevel()
    admin_mode.configure(bg='#2B2B2B')
    Label(admin_mode, text="-----X-----X-----X-----X-----X-----X-----X-----X-----", bg='#2B2B2B', fg='#A5B3C1').grid(
        row=0, column=1)
    Label(admin_mode, text="                                                ", bg='#2B2B2B', fg='#A5B3C1').grid(row=0,
                                                                                                                column=0)
    Label(admin_mode, text="                                                ", bg='#2B2B2B', fg='#A5B3C1').grid(row=0,
                                                                                                                column=2)
    Label(admin_mode, text="                                                ", bg='#2B2B2B', fg='#A5B3C1').grid(row=1,
                                                                                                                column=0,
                                                                                                                columnspan=3)
    Label(admin_mode, text="                                                ", bg='#2B2B2B', fg='#A5B3C1').grid(row=11,
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
    Button(admin_mode, text='SHOW DOCTORS', width=50, bd=0, bg='#3C3F41', fg='#A5B3C1', command=show_doctors).grid(
        row=8, column=0, columnspan=3,
        pady=5)
    Button(admin_mode, text='ADD DOCTOR', width=50, bd=0, bg='#3C3F41', fg='#A5B3C1', command=add_doctor).grid(row=6,
                                                                                                               column=0,
                                                                                                               columnspan=3,
                                                                                                               pady=5)
    Button(admin_mode, text='REMOVE DOCTOR', width=50, bd=0, bg='#3C3F41', fg='#A5B3C1', command=remove_doctor).grid(
        row=7, column=0, columnspan=3,
        pady=5)
    Button(admin_mode, text='SHOW HOSPITALS', width=50, bd=0, bg='#3C3F41', fg='#A5B3C1', command=show_hospitals).grid(
        row=5,
        column=0,
        pady=5,
        columnspan=3)
    Button(admin_mode, text='SHOW PATIENTS', width=50, bd=0, bg='#3C3F41', fg='#A5B3C1', command=show_patients).grid(
        row=11, column=0,
        columnspan=3,
        pady=5)
    Button(admin_mode, text='ADD PATIENT', width=50, bd=0, bg='#3C3F41', fg='#A5B3C1', command=add_patient).grid(
        row=9, column=0,
        columnspan=3,
        pady=5)
    Button(admin_mode, text='REMOVE PATIENT', width=50, bd=0, bg='#3C3F41', fg='#A5B3C1', command=remove_patient).grid(
        row=10, column=0,
        columnspan=3,
        pady=5)
    Button(admin_mode, text='BACK TO WELCOME SCREEN', width=50, bd=0, bg='#3C3F41', fg='#A5B3C1',
           command=admin_mode.destroy).grid(row=12, column=0,
                                            columnspan=3, pady=5)
    Label(admin_mode, text='',bg='#2B2B2B').grid(row=13)

# -----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----X-----
# MAIN SCREEN
root.title('Hospital Database Management')
root.geometry('700x500')
root.minsize(700, 500)
root.maxsize(700, 500)
root.configure(bg='#2B2B2B')
Label(root, text="                                                ", bg='#2B2B2B').grid(row=0, column=0)
Label(root, text="                                                ", bg='#2B2B2B').grid(row=1, column=0)
Label(root, text="                                                ", bg='#2B2B2B').grid(row=2, column=0)
Label(root, text="                                                ", bg='#2B2B2B').grid(row=3, column=0)
Label(root, text='Hospital Management Solutions', font=('Ariel Rounded Mt', 28, 'bold'), bg='#2B2B2B', fg='#FA3232',
      padx=20, pady=10).grid(row=4, column=0)
Label(root, text='CBSE Project - The Amaatra Academy', font=('Ariel Rounded Mt', 14, 'bold'), bg='#2B2B2B',
      fg='#A5B3C1', padx=65).grid(sticky='w')
Label(root, text='Adithya Ranjith', font=('Ariel Rounded Mt', 14, 'bold'), bg='#2B2B2B', fg='#A5B3C1', padx=65,
      pady=0).grid(sticky='w')
Label(root, text='Adithya Yogesh', font=('Ariel Rounded Mt', 14, 'bold'), bg='#2B2B2B', fg='#A5B3C1', padx=65,
      pady=0).grid(sticky='w')
Label(root, text='Adit Basak', font=('Ariel Rounded Mt', 14, 'bold'), bg='#2B2B2B', fg='#A5B3C1', padx=65,
      pady=0).grid(sticky='w')
Button(root, text='Admin Mode', command=admin_mode_func, width=50, bd=0, bg='#3C3F41', fg='#A5B3C1').grid(padx=170,
                                                                                                          pady=40)

root.mainloop()
