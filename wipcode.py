from sys import exit
import datetime
import mysql.connector as sql
import pickle
import csv

conn=sql.connect(host='localhost',user='root',passwd='Sanju@123',database='project')
if conn.is_connected():
    print('successfully connected')
c1=conn.cursor()
print('---------------------------------------------')
print("COVID-19 PATIENT MANAGEMENT SYSTEM")
print('---------------------------------------------')

c1.execute("show tables like '%patient_details%'")
isthere=c1.fetchall()
if ('patient_details' in isthere):
    c1.execute("create table patient_details(Name varchar(30), Age int, Hospital varchar(30), Services varchar(100), Number varchar(15), Timing date)")
    conn.commit()
    c1.execute('create table doctor_details(Name varchar(30), Age int, Hospital varchar(30), Department varchar(30), Phone_Number varchar(15))')
    conn.commit()

    c1.execute('create table hospitals(srno int, name varchar(50), location varchar(50), area varchar(50))')
    conn.commit()
    c1.execute('insert into hospitals values(1, "Manipal Hospital", "HAL Old Airport Rd", "Marathahalli")')
    conn.commit()
    c1.execute('insert into hospitals values(2, "Sakra Hospital", "Outer Ring Rd", "Marathahalli")')
    conn.commit()
    c1.execute('insert into hospitals values(3, "Columbia Asia", "Varthur Kodi", "Whitefield")')
    conn.commit()
    c1.execute('insert into hospitals values(4, "Narayana Hrudhalaya", "Hosur Rd", "Electronic City")')
    conn.commit()
    c1.execute('insert into hospitals values(5, "Blossom Hospital", "Central Jail Rd", "Electronic City")')
    conn.commit()
    c1.execute('insert into hospitals values(6, "Fortis Clinic", "Bannerghatta Rd", "Electronic City")')
    conn.commit()
    c1.execute('insert into hospitals values(7, "Apollo Hospital", "14th Cross Rd", "Jayanagar")')
    conn.commit()
    c1.execute('insert into hospitals values(8, "Aster CMI", "New Airport Rd", "Hebbal")')
    conn.commit()
    c1.execute('insert into hospitals values(9, "Sparsh Hospital", "Infantry Rd", "Jayanagar")')
    conn.commit()
    c1.execute('insert into hospitals values(10, "BGS Gleneagles Hospital", "Richmond Rd", "Jaynagar")')
    conn.commit()
    c1.execute('insert into hospitals values(11, "Sagar Hospital", "Banashankari", "Jayanagar")')
    conn.commit()
    c1.execute('insert into hospitals values(12, "Ramaiah Memorial Hospital", "BEL Rd", "Hebbal")')
    conn.commit()
    c1.execute('insert into hospitals values(13, "Bangalore Baptist Hospital", "Vinayakanagar", "Hebbal")')
    conn.commit()
    c1.execute('insert into hospitals values(14, "Kauvery Hospital","Hewlett Packard Av", "Electronic City")')
    conn.commit()
    c1.execute('insert into hospitals values(15, "Mallya Hospital", "Cubbon Park", "Jayanagar")')
    conn.commit()

    c1.execute('create table manipal(Contact_No char(15), No_beds_available int, Cost_of_bed int, Oxygen_available char(3), ambulance int, covid_test_cost int, vaccines_available varchar(30), CT_scan_price int, MRI_scan_price int, XRAY_price int, general_consultation_price int)')
    conn.commit()
    c1.execute('create table sakra(Contact_No char(15), No_beds_available int, Cost_of_bed int, Oxygen_available char(3), ambulance int, covid_test_cost int, vaccines_available varchar(30), CT_scan_price int, MRI_scan_price int, XRAY_price int, general_consultation_price int)')
    conn.commit()
    c1.execute('create table columbia(Contact_No char(15), No_beds_available int, Cost_of_bed int, Oxygen_available char(3), ambulance int, covid_test_cost int, vaccines_available varchar(30), CT_scan_price int, MRI_scan_price int, XRAY_price int, general_consultation_price int)')
    conn.commit()
    c1.execute('create table narayana(Contact_No char(15), No_beds_available int, Cost_of_bed int, Oxygen_available char(3), ambulance int, covid_test_cost int, vaccines_available varchar(30), CT_scan_price int, MRI_scan_price int, XRAY_price int, general_consultation_price int)')
    conn.commit()
    c1.execute('create table blossom(Contact_No char(15), No_beds_available int, Cost_of_bed int, Oxygen_available char(3), ambulance int, covid_test_cost int, vaccines_available varchar(30), CT_scan_price int, MRI_scan_price int, XRAY_price int, general_consultation_price int)')
    conn.commit()
    c1.execute('create table fortis(Contact_No char(15), No_beds_available int, Cost_of_bed int, Oxygen_available char(3), ambulance int, covid_test_cost int, vaccines_available varchar(30), CT_scan_price int, MRI_scan_price int, XRAY_price int, general_consultation_price int)')
    conn.commit()
    c1.execute('create table apollo(Contact_No char(15), No_beds_available int, Cost_of_bed int, Oxygen_available char(3), ambulance int, covid_test_cost int, vaccines_available varchar(30), CT_scan_price int, MRI_scan_price int, XRAY_price int, general_consultation_price int)')
    conn.commit()
    c1.execute('create table aster(Contact_No char(15), No_beds_available int, Cost_of_bed int, Oxygen_available char(3), ambulance int, covid_test_cost int, vaccines_available varchar(30), CT_scan_price int, MRI_scan_price int, XRAY_price int, general_consultation_price int)')
    conn.commit()
    c1.execute('create table sparsh(Contact_No char(15), No_beds_available int, Cost_of_bed int, Oxygen_available char(3), ambulance int, covid_test_cost int, vaccines_available varchar(30), CT_scan_price int, MRI_scan_price int, XRAY_price int, general_consultation_price int)')
    conn.commit()
    c1.execute('create table bgs(Contact_No char(15), No_beds_available int, Cost_of_bed int, Oxygen_available char(3), ambulance int, covid_test_cost int, vaccines_available varchar(30), CT_scan_price int, MRI_scan_price int, XRAY_price int, general_consultation_price int)')
    conn.commit()
    c1.execute('create table sagar(Contact_No char(15), No_beds_available int, Cost_of_bed int, Oxygen_available char(3), ambulance int, covid_test_cost int, vaccines_available varchar(30), CT_scan_price int, MRI_scan_price int, XRAY_price int, general_consultation_price int)')
    conn.commit()
    c1.execute('create table ramaiah(Contact_No char(15), No_beds_available int, Cost_of_bed int, Oxygen_available char(3), ambulance int, covid_test_cost int, vaccines_available varchar(30), CT_scan_price int, MRI_scan_price int, XRAY_price int, general_consultation_price int)')
    conn.commit()
    c1.execute('create table blrbaptist(Contact_No char(15), No_beds_available int, Cost_of_bed int, Oxygen_available char(3), ambulance int, covid_test_cost int, vaccines_available varchar(30), CT_scan_price int, MRI_scan_price int, XRAY_price int, general_consultation_price int)')
    conn.commit()
    c1.execute('create table kauvery(Contact_No char(15), No_beds_available int, Cost_of_bed int, Oxygen_available char(3), ambulance int, covid_test_cost int, vaccines_available varchar(30), CT_scan_price int, MRI_scan_price int, XRAY_price int, general_consultation_price int)')
    conn.commit()
    c1.execute('create table mallya(Contact_No char(15), No_beds_available int, Cost_of_bed int, Oxygen_available char(3), ambulance int, covid_test_cost int, vaccines_available varchar(30), CT_scan_price int, MRI_scan_price int, XRAY_price int, general_consultation_price int)')
    conn.commit()

    c1.execute("insert into manipal values('1800-102-5555', 300, 8000, 'Yes', 2000, 1200, 'Covaxin, Covidshield', 7000, 10000, 1200, 1000)")
    conn.commit()

def hospitals():
    j=1
    c1.execute('select name, location, area from hospitals order by area asc')
    r = c1.fetchall()
    dictt={}
    for i in r:
        print(j,' - ',i)
        dictt[j]=i[0]
        j+=1
        
    global hosp
    hosp=int(input("Choose a hospital to view details (1-"+str(j-1)+"): "))#NO BUGS TILL HERE
    if(int(hosp)>0 and int(hosp)<j+1):
        c1.execute("select * from hospitals where name="+"'"+dictt[hosp]+"'")
        record = c1.fetchall()
        if len(record)>0:
            for x in record:
                print(x)
    action=int(input('Enter 1 to book apointment or 2 to exit to main page'))
    def Action():
        if action==1:
            patient_mode()
        elif(action==2):
            main()
        else:
            print('ERROR!: ENTERED VALUE NOT RECOGNISED')
            Action()
    Action()
        
def patient_mode():        
      p_name=input('Enter Patient Name:')
      p_age=int(input('Enter Age:'))
      p_hospital=str(input("Enter hospial name from list"))
      p_problems=input('Enter the services requested:')
      p_phono=int(input('Enter Phone number:'))
      p_datetime=eval(input('Enter appointment date and time in YYMMDD hh:mm:00 xm format'))
      p_hospital=hosp
      c1.execute("insert into patient_details(Name, Age, Hospital, Services, Number) values(%s, %s, %s, %s, %s)",(p_name, p_age, p_hospital, p_problems, p_phono))
      conn.commit()
      c1.execute("insert into patient_details(Timing) values(%s)",(p_datetime))
      conn.commit()
      print('SUCCESSFULLY REGISTERED')
      print('Your appointment(s):')
      c1.execute("select * from patient_details where Number=p_phono")
      print("Redirecting...")
      main()
    
def admin_mode():
    ch=0
    while(int(ch)>=0 and int(ch)<=10):
        print("1.Add hospital")
        print("2.Remove hospital")
        print("3.Add doctor")
        print("4.Remove doctor")
        print("5.View hospitals")
        print("6.View Patients")
        print("7.View doctors")
        print("8.Go back")
        ch = int(input("Enter choice"))
        if ch==1:
            print('General Services')
            print('-----x-----x-----x-----x-----x-----x-----x-----')
            name=str(input("Enter Hospital name : "))
            sub_table_name=name.replace(' ','')
            hospital.append(sub_table_name)
            location=str(input("Enter Hospital Location : "))
            area=str(input("Enter Hospital area : "))
            print('-----x-----x-----x-----x-----x-----x-----x-----')
            Contact=str(input("Enter the Contact Number or Helpline Number : "))
            consult_cost=int(input("Enter the Cost for General Consulatation"))
            Beds=int(input('Enter the number of Beds Available : '))
            Beds_cost=float(input('Enter the cost of a Bed : '))
            o2=str(input('Enter Yes/No for the availability of Oxygen : '))
            amb=int(input("Enter the cost of Ambulance Services : "))
            Cov_vaccine=str(input("Enter the Covid vaccines seperated by comma(,) if available : "))
            print('-----x-----x-----x-----x-----x-----x-----x-----x-----')
            print('Radiology and Scans')
            print('-----x-----x-----x-----x-----x-----x-----x-----x-----')
            
            def ct():
                global ct_cost,ct
                ct=str(input("Enter if CT Scans are Available : "))
                ct_cost=0
                if ct in ('yes', 'Yes', 'YES', 'y'):
                    ct="Yes"
                    ct_cost=float(input("Enter the cost of a CT SCAN : "))
                elif ct in ('no', 'No', 'NO', 'n'):
                    ct="No"
                    ct_cost='N/A'
                else:
                    Print("ERROR : Input Not Recognised --- Please Enter either Yes or No")
                    ct()
            def mri():
                global mri_cost,mri
                mri=str(input("Enter if MRI SCAN are Available : "))
                mri_cost=0
                if mri in ('yes', 'Yes', 'YES', 'y'):
                    mri="Yes"
                    mri_cost=float(input("Enter the cost of a MRI SCAN : "))
                elif mri in ('no', 'No', 'NO', 'n'):
                    mri="No"
                    mri_cost="N/A"
                else:
                    Print("ERROR : Input Not Recognised --- Please Enter either Yes or No")
                    mri()
            def cov():
                global cov_cost,cov
                cov=str(input("Enter if COVID TEST are Available : "))
                cov_cost=0
                if cov in ('yes', 'Yes', 'YES', 'y'):
                    cov="Yes"
                    cov_cost=float(input("Enter the cost of a COVID TEST : "))
                elif cov in ('no', 'No', 'NO', 'n'):
                    cov="No"
                    cov_cost="N/A"
                else:
                    Print("ERROR : Input Not Recognised --- Please Enter either Yes or No")
                    cov()
            def xray():
                global xray_cost,xray
                xray=str(input("Enter if X-RAY SCAN are Available : "))
                xray_cost=0
                if xray in ('yes', 'Yes', 'YES', 'y'):
                    xray="Yes"
                    xray_cost=float(input("Enter the cost of a X-RAY SCAN : "))
                elif xray in ('no', 'No', 'NO', 'n'):
                    xray="No"
                    xray_cost="N/A"
                else:
                    Print("ERROR : Input Not Recognised --- Please Enter either Yes or No")
                    xray()
            ct()
            mri()
            cov()
            xray()
            
            for i in range(1,2):
                global maintablecount
                c1.execute("insert into hospitals values("+ "'" +str(maintablecount)+"', '"+ name +"'," + "'" + location + "'," + "'" + area + "'" +")")
                maintablecount+=1
                c1.execute('create table '+ sub_table_name+'(srno int, data_name varchar(255), data varchar(255))')
            x={Contact:'Contact Details', consult_cost:'Consultation Cost', Beds:'Beds Availability', Beds_cost:'Cost of Beds', o2:'Oxygen Availability', amb:'Ambulance Service Cost', Cov_vaccine:'Covid Vaccines Available', ct: 'CT SCAN Availibility', ct_cost:'Cost of CT SCAN', mri:'MRI SCAN Availability', mri_cost:'Cost of MRI SCAN', cov:'COVID TEST Availability', cov_cost:'Cost of COVID TEST', xray:'X-RAY SCAN Availability', xray_cost:'Cost of X-RAY SCAN'}
            count=1
            for key,value in x.items():
                c1.execute("insert into "+sub_table_name+' values( '+'"'+str(count)+ '","'+str(value)+'","'+str(key)+'")')
                count+=1
            conn.commit()
            print('Updating Data',end='')
            for i in range(15):
                print('.',end='')
                time.sleep(1)
            print('Data Successfully Updated')

            ask=input('enter if you want to repeat')
            if ask=='y':
                admin_mode()                     
        elif ch==2:
           removeit=str(input("Enter Name of hospital to remove from list"))
           c1.execute("count(*) from hospitals where name=(%s)",(removeit))
           num = len(c1.fetchall())
           if num>0:
               c1.execute("select * from hospitals where name=(%s)",(removeit))
               r=c1.fetachall()
               for x in r:
                   print(x)
               confirm = print("Confirm deletion of record (Y/N)?")
               if confirm=='Y':
                   c1.execute("delete * from hospital where name=(%s)",(removeit))
                   conn.commit()
               else:
                   admin_mode()
           else:
               print("Error! No matching records found.")           
        elif ch==3:
           d_name=input('Enter Doctor Name:')
           d_age=int(input('Enter Age:'))
           d_hospital=str(input('Enter hospital:'))
           d_department=input('Enter the Department:')
           d_phono=int(input('Enter Phone number:'))
           c1.execute("insert into doctor_details values(%s, %s, %s, %s, %s)",(d_name, d_age, d_hospital, d_department, d_phono))
           conn.commit()
           print('successfully registered')
        elif ch==4:
           d_phono=str(input("Enter phone number of doctor to remove"))
           c1.execute("count(*) from doctor_details where Phone_Number=(%s)",(d_phono))
           num = len(c1.fetchall())
           if num>0:
               c1.execute("select * from doctor_details where Phone_Number=(%s)",(d_phono))
               r=c1.fetachall()
               for x in r:
                   print(x)
               confirm = print("Confirm deletion of record (Y/N)?")
               if confirm=='Y':
                   c1.execute("delete * from doctor_details where Phone_Number=(%s)",(d_phono))
                   conn.commit()
               else:
                   admin_mode()
           else:
               print("Error! No matching records found.")
        elif ch==5:
           hospitals()
        elif ch==6:
           c1.execute("select * from patient_details group by hospital")
           r=c1.fetchall()
           for x in r:
               print(x)
        elif ch==7:
           c1.execute("select * from doctor_details group by hospital")
           r=c1.fetchall()
           for x in r:
               print(x)
        elif ch==8:
           main()
        else:
           print("Invalid input!")
           exit()
    else:
       print("Invalid input!")
       exit()

        
key='jfktn4runr1nf893kk'
l=[]
def main():
    print("successfully connected") 
    print('1.List Hospitals (Patient Mode)')
    print('2.Register Hospital (Admin Mode)')
    print('3.Exit')
    choice=int(input('ENTER YOUR CHOICE:'))
    if choice==1:
        hospitals()
    if choice==2:
        if key in l:
            l.clear()
            admin_mode()
        else:
            print("ACCESS DENIED! Redirecting...")
            main()
    else:
        exit()
        
def welcome():
    print('WELCOME!')
    print("1.LOGIN")
    print("2.SIGN UP")
    print("3.EXIT")
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice==1:
        with open("logindata.csv", "r") as f:
            us1=str(input("Enter username:"))
            pwd1=str(input("Enter the password:"))
            auth=str(input("Enter administrator authentication key (ignore if patient):"))
            readit=csv.reader(f)
            for row in readit:
                if row == [us1, pwd1]:
                    print("login successful")
                    if auth == key:
                        l.append(key)
                    main()
                else:
                    print('Wrong username and/or password')
                    welcome()
    elif choice==2:
        with open("logindata.csv", "a") as f:
            us1=str(input("enter user name:"))
            pwd1=str(input("enter the password:"))
            writeit=csv.writer(f)
            writeit.writerow([us1, pwd1])
            welcome()
    elif choice==3:
        exit()
    else:
        print("Invalid Input! Redirecting....")
        welcome()             
welcome()
