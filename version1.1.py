from sys import exit
import mysql.connector as sql
import pickle
import time
conn=sql.connect(host='localhost',user='root',passwd='amaatra',database='project')
if conn.is_connected():
    print('successfully connected')
c1=conn.cursor()
print('---------------------------------------------')
print("COVID-19 PATIENT MANAGEMENT SYSTEM")
print('---------------------------------------------')

import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='amaatra',database='project')
if conn.is_connected():
      print('successfully connected')
c1.execute('drop table hospitals')
hospital_list=['maipal', 'sakra', 'columbia', 'narayana', 'blossom', 'fortis', 'apollo', 'aster', 'sparsh', 'bgs', 'sagar', 'ramaiah', 'blrbaptist', 'kauvery', 'mallya']
for i in hospital_list:
    c1.execute('drop table' +" '"+ i +"' ")
c1=conn.cursor()
c1.execute('create table hospitals(no int, name varchar(50), location varchar(50), area varchar(50))')
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


def patient_mode():
    c1.execute('select * from hospital')
    r = c1.fetchall()
    for i in r:
        print(i)
    hosp=int(input("Choose a hospital to view details (1-15):"))
    if hosp==1:
        hosp='manipal'
        c1.execute('select * from manipal')
    if hosp==2:
        hosp='sakra'
        c1.execute('select * from sakra')
    if hosp==3:
        hosp='columbia'
        c1.execute('select * from columbia')
    if hosp==4:
        hosp='narayana'
        c1.execute('select * from narayana')
    if hosp==5:
        hosp='blossom'
        c1.execute('select * from blossom')
    if hosp==6:
        hosp='fortis'
        c1.execute('select * from fortis')
    if hosp==7:
        hosp='apollo'
        c1.execute('select * from apollo')
    if hosp==8:
        hosp='aster'
        c1.execute('select * from aster')
    if hosp==9:
        hosp='sparsh'
        c1.execute('select * from sparsh')
    if hosp==10:
        hosp='bgs'
        c1.execute('select * from bgs')
    if hosp==11:
        hosp='sagar'
        c1.execute('select * from sagar')
    if hosp==12:
        hosp='ramaiah'
        c1.execute('select * from ramaiah')
    if hosp==13:
        hosp='blrbaptist'
        c1.execute('select * from blrbaptist')
    if hosp==14:
        hosp='kauvery'
        c1.execute('select * from kauvery')
    if hosp==15:
        hosp='mallya'
        c1.execute('select * from mallya')
    else:
        print('input invalid!')
        exit()
    print("1.Book an Appointment")
    print("2.Go back")
    print()
    x=int(print("Choose an option:"))
    if(x==1):
      p_name=input('Enter Patient Name:')
      p_age=int(input('Enter Age:'))
      p_problems=input('Enter the services requested:')
      p_phono=int(input('Enter Phone number:'))
      p_hospital=hosp
      sql_insert="insert into patient_details values(""'"+p_name+"',"+str(p_age)+",'"+p_problems+"',"+str(p_phono)+"',"+p_hospital+")"
      c1.execute(sql_insert)
      print('SUCCESSFULLY REGISTERED')
      conn.commit()

maintablecount=1
def admin_mode():
    print("1.Add hospital")
    print("2.Remove hospital")
    print("3.Alter hospital data")
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

def main():
    print("successfully connected") 
    print('1.List Hospitals (Patient Mode)')
    print('2.Register Hospital (Admin Mode)')
    print('3.Exit')
    choice=int(input('ENTER YOUR CHOICE:'))
    if choice==1:
        paitenit_mode()
    if choice==2:
        admin_mode()
    else:
        exit()
        
def welcome():
    print('WELCOME!')
    print("1.LOGIN")
    print("2.SIGN UP")
    print("3.EXIT")
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice==1:
        us1=str(input("enter user name:"))
        pwd1=str(input("enter the password:"))
        f=open("logindata.dat", "wb+")
        for i in range(1,2):
            try:
                rec=pickle.load(f)
                if(rec["username"]==pwd1):
                   for i in rec:
                       print(i)
                       main()
                   
                else:
                    print('Wrong username and/or password')
                    welcome()
            except EOFError:
                break
        f.close()
    if choice==2:
        us1=str(input("enter user name:"))
        pwd1=str(input("enter the password:"))
        rec={"username": us1, "password": pwd1}
        f=open("student.dat", "ab")
        pickle.dump(rec,f)
        f.close()
        welcome()
    if choice==3:
        exit()

welcome()
