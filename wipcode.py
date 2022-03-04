from sys import exit
import datetime
import mysql.connector as sql
import pickle
import csv

conn=sql.connect(host='localhost',user='root',passwd='amaatra',database='project')
if conn.is_connected():
    print('successfully connected')
c1=conn.cursor()
print('---------------------------------------------')
print("COVID-19 PATIENT MANAGEMENT SYSTEM")
print('---------------------------------------------')

c1.execute('create table patient_details(Name varchar(30), Age int, Hospital varchar(30), Services varchar(100), Number varchar(15), Timing date')
conn.commit()
c1.execute('create table doctor_details(Name varchar(30), Age int, Hospital varchar(30), Department varchar(30), Phone_Number varchar(15)')
conn.commit()
c1.execute('create table worker_details(Name varchar(30), Age int, Hospital varchar(30), workname varchar(30), Phone_Number varchar(15)')
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
    c1.execute('select * from hospitals group by area')
    r = c1.fetchall()
    for i in r:
        print(i)
    global hosp=int(input("Choose a hospital to view details (1-15):"))
    while(int(hosp)>0 and int(hosp)<16):
        print("When done, press 0 to book an appointment or anything else to go back")
        c1.execute("select srno from hospitals")
        s = c1.fetchone()
        c1.execute("select name from hospitals")
        place = c1.fetchall()
        for p in place:
            c1.execute("select * from hospitals where srno=+"s"+ and name=+"place"+")
            record = c1.fetchall()
            if len(record)>0:
                for x in record:
                    print(x)
     if hosp==0:
        patient_mode()
     else:
        main()
        
def patient_mode():        
      p_name=input('Enter Patient Name:')
      p_age=int(input('Enter Age:'))
      p_hospital=str(input("Enter hospial name from list")
      p_problems=input('Enter the services requested:')
      p_phono=int(input('Enter Phone number:'))
      p_datetime=eval(input('Enter appointment date and time in dd-mm-yy hh:mm:00 xm format'))
      p_hospital=hosp
      sql_insert="insert into patient_details(Name, Age, Hospital, Services, Number) values(""'"+p_name+"',"+str(p_age)+",'+",'+p_hospital+","+"+p_problems+"',"+str(p_phono)")"
      c1.execute(sql_insert)
      conn.commit()
      c1.execute("insert into patient_details("Timing") values(convert("datetime"+","+ "p_datetime"+","+ "5")")
      conn.commit()
      print('SUCCESSFULLY REGISTERED')
      print('Your appointment(s):')
      c1.execute("select * from patient_details where Number=p_phono")
      print("Redirecting...")
      main()
        
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
