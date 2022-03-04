from sys import exit
import datetime
import mysql.connector as sql
import pickle
import csv
import time

conn=sql.connect(host='localhost',user='root',passwd='amaatra',database='project')
if conn.is_connected():
    print('successfully connected')
c1=conn.cursor()
print('---------------------------------------------')
print("COVID-19 PATIENT MANAGEMENT SYSTEM")
print('---------------------------------------------')


hospital={'manipal':'Manipal Hospital', 'sakra':'Sakra Hospital', 'columbia':'Columbia Asia', 'narayana':'Narayana Hrudhalaya', 'blossom':'Blossom Hospital', 'fortis':'Fortis Clinic', 'apollo':'Apollo Hospital', 'aster':'Aster CMI', 'sparsh':'Sparsh Hospital', 'bgs':"BGS Gleneagles Hospital", 'sagar':"Sagar Hospital", 'ramaiah':"Ramaiah Memorial Hospital", 'blrbaptist':"Bangalore Baptist Hospital", 'kauvery':"Kauvery Hospital", 'mallya':"Mallya Hospital"}

c1.execute('create table patient_details(Name varchar(30), Age int, Hospital varchar(30), Services varchar(100), Number varchar(15), Timing date)')
conn.commit()
c1.execute('create table doctor_details(Name varchar(30), Age int, Hospital varchar(30), Department varchar(30), Phone_Number varchar(15))')
conn.commit()
c1.execute('create table worker_details(Name varchar(30), Age int, Hospital varchar(30), workname varchar(30), Phone_Number varchar(15))')
conn.commit()

c1.execute('create table hospitals(srno int, name varchar(250), location varchar(250), area varchar(250))')
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

def sub_table_name():
    for key,value in hospital.items():
        global hospital_name
        if value==hospital_name:
            return key
        else:
            return 'Hospital not found'
        
maintablecount=1
def add_hospital():
    print('General Services')
        print('-----x-----x-----x-----x-----x-----x-----x-----')
        name=str(input("Enter Hospital name : "))
        sub_table_name=name.replace(' ','')
        hospital[sub_table_name]=name
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
            conn.commit()
            maintablecount+=1
            c1.execute('create table '+ sub_table_name+'(srno int, data_name varchar(255), data varchar(255))')
            conn.commit()
        x={Contact:'Contact Details', consult_cost:'Consultation Cost', Beds:'Beds Availability', Beds_cost:'Cost of Beds', o2:'Oxygen Availability', amb:'Ambulance Service Cost', Cov_vaccine:'Covid Vaccines Available', ct: 'CT SCAN Availibility', ct_cost:'Cost of CT SCAN', mri:'MRI SCAN Availability', mri_cost:'Cost of MRI SCAN', cov:'COVID TEST Availability', cov_cost:'Cost of COVID TEST', xray:'X-RAY SCAN Availability', xray_cost:'Cost of X-RAY SCAN'}
        count=1
        for key,value in x.items():
            c1.execute("insert into "+sub_table_name+' values( '+'"'+str(count)+ '","'+str(value)+'","'+str(key)+'")')
            conn.commit()
            count+=1
        print('Updating Data',end='')
        for i in range(15):
            print('.',end='')
            time.sleep(1)
        print('Data Successfully Updated')

        ask=input('enter if you want to repeat')
        if ask=='y':
            admin_mode()

def remove_hospital():
    global hospital_name
    hospital_name=input('Enter the name of the Hospital to be REMOVED PERMANENTLY')
    print('The Hospital entered will be entered PERMANENTLY with no means to recover data')
    def recover():
        recover=input('Enter Yes to continue or No to Cancel deletion : ')
        if recover in ['Yes','YES','yes','y','Y']:
            print('DELETING TABLE ',hospital_name)
            c1.execute('delete from hospitals where name='+"'"+hospital_name+"'")
            conn.commit()
            c1.execute('drop table '+sub_table_name())
            conn.commit()
            print('Deleting.',end='')
            for i in range(15):
                print('.',end='')
                time.sleep(0.75)
            print('Succesfully Deleted',hospital_name)
            admin_mode()
        elif recover in ['no','NO','No','N','n']:
            print('You have cancelled deletion')
            admin_mode()
        else:
            print('ERROR : VALUE ENTERED NOT RECOGNISED - PLEASE ENTER ONLY YES OR NO')
            recover()
    recover()

def update_hospital():
    global hospital_name
    hospital_name=input('Enter the name of the Hospital for which you want to update the data')
    print('1:Name \n2:Location \n3:Area \4:Contact Details \n5:Consultation Cost \n6:Beds Availability \n7:Cost Of Beds \n8:Oxygen Availability \n9: Ambulance Service Cost \n10:Covid Vaccines Availability \n11:CT SCAN Availability \n12:Cost of CT SCAN \n13: MRI SCAN Availability')
    print('14:Cost of MRI SCAN \n15:COVID TEST Availability \n16:Cost of COVID TEST \n17:X-RAY SCAN Availability \n18:Cost of X-RAY SCAN')
    new_name=sub_table_name()
    data_name=input('Enter the numbers corresponding to the Data_Name(s) to be updated separated by comma(,)')
    if '1' in data_name:
        data=input('Enter the new Name :')
        c1.execute('update hospitals set name ='+"'"+data+"'"+' where name ='+"'"+hospital_name+"'")
        conn.commit()
        print('Successfully Updated Name')
    if '2' in data_name:
        data=input('Enter the new Location :')
        c1.execute('update hospitals set location ='+"'"+data+"'"+' where name ='+"'"+hospital_name+"'")
        conn.commit()
        print('Successfully Updated Location')
    if '3' in data_name:
        data=input('Enter the new Area :')
        c1.execute('update hospitals set area ='+"'"+data+"'"+' where name ='+"'"+hospital_name+"'")
        conn.commit()
        print('Successfully Updated Area')
    if '4' in data_name:
        data=input('Enter the new Contact Details :')
        c1.execute('update hospitals set data ='+"'"+data+"'"+' where data_name = "Contact Details"')
        conn.commit()
        print('Successfully Updated Contact Details')
    if '5' in data_name:
        data=input('Enter the new Consultation Cost :')
        c1.execute('update hospitals set data ='+"'"+data+"'"+' where data_name ="Consultation Cost"')
        conn.commit()
        print('Successfully Updated Consultation Cost')
    if '6' in data_name:
        data=input('Enter the new Beds Availability :')
        c1.execute('update hospitals set data ='+"'"+data+"'"+' where data_name ="Beds Availability"')
        conn.commit()
        print('Successfully Updated Beds Availability')
    if '7' in data_name:
        data=input('Enter the new Cost Of Beds :')
        c1.execute('update hospitals set data ='+"'"+data+"'"+' where data_name ="Cost Of Beds"')
        conn.commit()
        print('Successfully Updated Cost Of Beds')
    if '8' in data_name:
        data=input('Enter the new Oxygen Availability :')
        c1.execute('update hospitals set data ='+"'"+data+"'"+' where data_name ="Oxygen Availability"')
        conn.commit()
        print('Successfully Updated Oxygen Availability')
    if '9' in data_name:
        data=input('Enter the new Ambulance Service Cost :')
        c1.execute('update hospitals set data ='+"'"+data+"'"+' where data_name ="Ambulance Service Cost"')
        conn.commit()
        print('Successfully Updated Ambulance Service Cost')
    if '10' in data_name:
        data=input('Enter the new Covid Vaccines Availability :')
        c1.execute('update hospitals set data ='+"'"+data+"'"+' where data_name ="Covid Vaccines Availability"')
        conn.commit()
        print('Successfully Updated Covid Vaccines Availability')
    if '11' in data_name:
        data=input('Enter the new CT SCAN Availability :')
        c1.execute('update hospitals set data ='+"'"+data+"'"+' where data_name ="CT SCAN Availability"')
        conn.commit()
        print('Successfully Updated CT SCAN Availability')
    if '12' in data_name:
        data=input('Enter the new Cost of CT SCAN :')
        c1.execute('update hospitals set data ='+"'"+data+"'"+' where data_name ="Cost of CT SCAN"')
        conn.commit()
        print('Successfully Updated Cost of CT SCAN')
    if '13' in data_name:
        data=input('Enter the new MRI SCAN Availability :')
        c1.execute('update hospitals set data ='+"'"+data+"'"+' where data_name ="MRI SCAN Availability"')
        conn.commit()
        print('Successfully Updated MRI SCAN Availability')
    if '14' in data_name:
        data=input('Enter the new Cost of MRI SCAN :')
        c1.execute('update hospitals set data ='+"'"+data+"'"+' where data_name ="Cost of MRI SCAN"')
        conn.commit()
        print('Successfully Updated Cost of MRI SCAN')
    if '15' in data_name:
        data=input('Enter the new COVID TEST Availability :')
        c1.execute('update hospitals set data ='+"'"+data+"'"+' where data_name ="COVID TEST Availability"')
        conn.commit()
        print('Successfully Updated COVID TEST Availability')
    if '16' in data_name:
        data=input('Enter the new Cost of COVID TEST :')
        c1.execute('update hospitals set data ='+"'"+data+"'"+' where data_name ="Cost of COVID TEST"')
        conn.commit()
        print('Successfully Updated Cost of COVID TEST')
    if '17' in data_name:
        data=input('Enter the new X-RAY SCAN Availability :')
        c1.execute('update hospitals set data ='+"'"+data+"'"+' where data_name ="X-RAY SCAN Availability"')
        conn.commit()
        print('Successfully Updated X-RAY SCAN Availability')
    if '18' in data_name:
        data=input('Enter the new Cost of X-RAY SCAN :')
        c1.execute('update hospitals set data ='+"'"+data+"'"+' where data_name ="Cost of X-RAY SCAN"')
        conn.commit()
        print('Successfully Updated Cost of X-RAY SCAN')
    
    
def admin_mode():
    print("1.Add hospital")
    print("2.Remove hospital")
    print("3.Alter hospital data")
    ch = int(input("Enter choice"))
    if ch==1:
        add_hospital()
    elif ch==2:
        remove_hospital()
    elif ch==3:
        update_hospital()
    else:
        print('ERROR!: UNRECOGNISED VALUE - ENTER 1 OR 2 OR 3')
        admin_mode()     


