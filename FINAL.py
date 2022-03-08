from sys import exit
import datetime
import mysql.connector as sql
import pickle
import csv
import time

conn=sql.connect(host='localhost',user='root',passwd='Sanju@123',database='project')
if conn.is_connected():
    print('successfully connected')
c1=conn.cursor()
print('---------------------------------------------')
print("HOSPITAL MANAGEMENT SYSTEM")
print('---------------------------------------------')

hospital={'manipal':'Manipal Hospital', 'sakra':'Sakra Hospital', 'columbia':'Columbia Asia', 'narayana':'Narayana Hrudhalaya', 'blossom':'Blossom Hospital', 'fortis':'Fortis Clinic', 'apollo':'Apollo Hospital', 'aster':'Aster CMI', 'sparsh':'Sparsh Hospital', 'bgs':"BGS Gleneagles Hospital", 'sagar':"Sagar Hospital", 'ramaiah':"Ramaiah Memorial Hospital", 'blrbaptist':"Bangalore Baptist Hospital", 'kauvery':"Kauvery Hospital", 'mallya':"Mallya Hospital"}

c1.execute("show tables like '%hospitals%'")
isthere=c1.fetchall()
if ('hospitals' in isthere):

    c1.execute('create table patient_details(Name varchar(30), Age int, Hospital varchar(30), Services varchar(100), Number varchar(15), Timing date)')
    conn.commit()
    c1.execute('create table doctor_details(Name varchar(30), Age int, Hospital varchar(30), Department varchar(30), Phone_Number varchar(15))')
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

    c1.execute('create table manipal(srno varchar(225), data_name varchar(225), data varchar(225))' )
    conn.commit()
    c1.execute('create table sakra(srno varchar(225), data_name varchar(225), data varchar(225))' )
    conn.commit()
    c1.execute('create table columbia(srno varchar(225), data_name varchar(225), data varchar(225))' )
    conn.commit()
    c1.execute('create table narayana(srno varchar(225), data_name varchar(225), data varchar(225))' )
    conn.commit()
    c1.execute('create table blossom(srno varchar(225), data_name varchar(225), data varchar(225))' )
    conn.commit()
    c1.execute('create table fortis(srno varchar(225), data_name varchar(225), data varchar(225))' )
    conn.commit()
    c1.execute('create table apollo(srno varchar(225), data_name varchar(225), data varchar(225))' )
    conn.commit()
    c1.execute('create table aster(srno varchar(225), data_name varchar(225), data varchar(225))' )
    conn.commit()
    c1.execute('create table sparsh(srno varchar(225), data_name varchar(225), data varchar(225))' )
    conn.commit()
    c1.execute('create table bgs(srno varchar(225), data_name varchar(225), data varchar(225))' )
    conn.commit()
    c1.execute('create table sagar(srno varchar(225), data_name varchar(225), data varchar(225))' )
    conn.commit()
    c1.execute('create table ramaiah(srno varchar(225), data_name varchar(225), data varchar(225))' )
    conn.commit()
    c1.execute('create table blrbaptist(srno varchar(225), data_name varchar(225), data varchar(225))' )
    conn.commit()
    c1.execute('create table kauvery(srno varchar(225), data_name varchar(225), data varchar(225))' )
    conn.commit()
    c1.execute('create table mallya(srno varchar(225), data_name varchar(225), data varchar(225))' )
    conn.commit()


manipald={'Contact Details':'1800-102-5555', 'Consultation Cost':'Rs. 1000', 'Beds Availability':'300', 'Cost of Beds':'Rs. 8000', 'Oxygen Availability':'Yes', 'Ambulance Service Cost':'Rs. 2000', 'Covid Vaccines Available':'Covaxin, Covishield', 'CT SCAN Availibility':'Yes', 'Cost of CT SCAN':'Rs. 7000', 'MRI SCAN Availability':'Yes', 'Cost of MRI SCAN':'Rs. 10000', 'COVID TEST Availability':'Yes', 'Cost of COVID TEST':'Rs. 1200', 'X-RAY SCAN Availability':'Yes', 'Cost of X-RAY SCAN':'Rs. 1200'}
sakrad={'Contact Details':'080-4969-4969', 'Consultation Cost':'Rs. 1200', 'Beds Availability':'200', 'Cost of Beds':'Rs. 12000', 'Oxygen Availability':'Yes', 'Ambulance Service Cost':'Rs. 3000', 'Covid Vaccines Available':'Covaxin, Covishield, Sputnik', 'CT SCAN Availibility':'Yes', 'Cost of CT SCAN':'Rs. 10000', 'MRI SCAN Availability':'Yes', 'Cost of MRI SCAN':'Rs. 15000', 'COVID TEST Availability':'Yes', 'Cost of COVID TEST':'Rs. 800', 'X-RAY SCAN Availability':'Yes', 'Cost of X-RAY SCAN':'Rs. 1500'}
columbiad={'Contact Details':'074061 066688', 'Consultation Cost':'Rs. 1100', 'Beds Availability':'200', 'Cost of Beds':'Rs. 7000', 'Oxygen Availability':'Yes', 'Ambulance Service Cost':'Rs. 2500', 'Covid Vaccines Available':'Covaxin, Covishield, Sputnik', 'CT SCAN Availibility':'Yes', 'Cost of CT SCAN':'Rs. 7500', 'MRI SCAN Availability':'Yes', 'Cost of MRI SCAN':'Rs. 11000', 'COVID TEST Availability':'Yes', 'Cost of COVID TEST':'Rs. 1200', 'X-RAY SCAN Availability':'Yes', 'Cost of X-RAY SCAN':'Rs. 1100'}
narayanad={'Contact Details':'180-0309-0309', 'Consultation Cost':'Rs. 800', 'Beds Availability':'700', 'Cost of Beds':'Rs. 5000', 'Oxygen Availability':'Yes', 'Ambulance Service Cost':'Rs. 1500', 'Covid Vaccines Available':'Covaxin, Covishield, Sputnik', 'CT SCAN Availibility':'Yes', 'Cost of CT SCAN':'Rs. 6500', 'MRI SCAN Availability':'Yes', 'Cost of MRI SCAN':'Rs. 9000', 'COVID TEST Availability':'Yes', 'Cost of COVID TEST':'Rs. 800', 'X-RAY SCAN Availability':'Yes', 'Cost of X-RAY SCAN':'Rs. 800'}
blossomd={'Contact Details':'08108 08108', 'Consultation Cost':'Rs. 600', 'Beds Availability':'100', 'Cost of Beds':'Rs. 3500', 'Oxygen Availability':'Yes', 'Ambulance Service Cost':'Rs. 1500', 'Covid Vaccines Available':'Covaxin', 'CT SCAN Availibility':'No', 'Cost of CT SCAN':'N/A', 'MRI SCAN Availability':'No', 'Cost of MRI SCAN':'N/A', 'COVID TEST Availability':'Yes', 'Cost of COVID TEST':'Rs. 1200', 'X-RAY SCAN Availability':'Yes', 'Cost of X-RAY SCAN':'Rs. 800'}
fortisd={'Contact Details':'96633 67253', 'Consultation Cost':'Rs. 1200', 'Beds Availability':'400', 'Cost of Beds':'Rs. 7000', 'Oxygen Availability':'Yes', 'Ambulance Service Cost':'Rs. 2000', 'Covid Vaccines Available':'Covaxin, Covishield', 'CT SCAN Availibility':'Yes', 'Cost of CT SCAN':'Rs. 8000', 'MRI SCAN Availability':'Yes', 'Cost of MRI SCAN':'Rs. 11000', 'COVID TEST Availability':'Yes', 'Cost of COVID TEST':'Rs. 1200', 'X-RAY SCAN Availability':'Yes', 'Cost of X-RAY SCAN':'Rs. 1100'}
apollod={'Contact Details':'080-4612-4444', 'Consultation Cost':'Rs. 1100', 'Beds Availability':'400', 'Cost of Beds':'Rs. 8000', 'Oxygen Availability':'Yes', 'Ambulance Service Cost':'Rs. 2500', 'Covid Vaccines Available':'Covaxin, Covishield, Sputnik', 'CT SCAN Availibility':'Yes', 'Cost of CT SCAN':'Rs. 8000', 'MRI SCAN Availability':'Yes', 'Cost of MRI SCAN':'Rs. 11000', 'COVID TEST Availability':'Yes', 'Cost of COVID TEST':'Rs. 1200', 'X-RAY SCAN Availability':'Yes', 'Cost of X-RAY SCAN':'Rs. 1200'}
asterd={'Contact Details':'080-4342-0100', 'Consultation Cost':'Rs. 1200', 'Beds Availability':'500', 'Cost of Beds':'Rs. 8500', 'Oxygen Availability':'Yes', 'Ambulance Service Cost':'Rs. 2200', 'Covid Vaccines Available':'Covaxin, Sputnik', 'CT SCAN Availibility':'Yes', 'Cost of CT SCAN':'Rs. 9000', 'MRI SCAN Availability':'Yes', 'Cost of MRI SCAN':'Rs. 12000', 'COVID TEST Availability':'Yes', 'Cost of COVID TEST':'Rs. 1200', 'X-RAY SCAN Availability':'Yes', 'Cost of X-RAY SCAN':'Rs. 1150'}
sparshd={'Contact Details':'080-6122-2200', 'Consultation Cost':'Rs. 950', 'Beds Availability':'200', 'Cost of Beds':'Rs. 7000', 'Oxygen Availability':'Yes', 'Ambulance Service Cost':'Rs. 1800', 'Covid Vaccines Available':'Covaxin', 'CT SCAN Availibility':'Yes', 'Cost of CT SCAN':'Rs. 8000', 'MRI SCAN Availability':'Yes', 'Cost of MRI SCAN':'Rs. 10500', 'COVID TEST Availability':'Yes', 'Cost of COVID TEST':'Rs. 1200', 'X-RAY SCAN Availability':'Yes', 'Cost of X-RAY SCAN':'Rs. 1000'}
bgsd={'Contact Details':'080-2625-5555', 'Consultation Cost':'Rs. 1000', 'Beds Availability':'350', 'Cost of Beds':'Rs. 7500', 'Oxygen Availability':'Yes', 'Ambulance Service Cost':'Rs. 2000', 'Covid Vaccines Available':'Covaxin, Covishield', 'CT SCAN Availibility':'Yes', 'Cost of CT SCAN':'Rs. 8600', 'MRI SCAN Availability':'Yes', 'Cost of MRI SCAN':'Rs. 10000', 'COVID TEST Availability':'Yes', 'Cost of COVID TEST':'Rs. 1200', 'X-RAY SCAN Availability':'Yes', 'Cost of X-RAY SCAN':'Rs. 1100'}
sagard={'Contact Details':'080-6955-5555', 'Consultation Cost':'Rs. 900', 'Beds Availability':'200', 'Cost of Beds':'Rs. 6000', 'Oxygen Availability':'Yes', 'Ambulance Service Cost':'Rs. 2000', 'Covid Vaccines Available':'Covaxin, Covishield', 'CT SCAN Availibility':'Yes', 'Cost of CT SCAN':'Rs. 6500', 'MRI SCAN Availability':'Yes', 'Cost of MRI SCAN':'Rs. 9000', 'COVID TEST Availability':'Yes', 'Cost of COVID TEST':'Rs. 1200', 'X-RAY SCAN Availability':'Yes', 'Cost of X-RAY SCAN':'Rs. 800'}
ramaiahd={'Contact Details':'080-2360-9999', 'Consultation Cost':'Rs. 1000', 'Beds Availability':'400', 'Cost of Beds':'Rs. 7000', 'Oxygen Availability':'Yes', 'Ambulance Service Cost':'Rs. 1700', 'Covid Vaccines Available':'Covaxin, Covishield', 'CT SCAN Availibility':'Yes', 'Cost of CT SCAN':'Rs. 7500', 'MRI SCAN Availability':'Yes', 'Cost of MRI SCAN':'Rs. 10000', 'COVID TEST Availability':'Yes', 'Cost of COVID TEST':'Rs. 1200', 'X-RAY SCAN Availability':'Yes', 'Cost of X-RAY SCAN':'Rs. 900'}
blrbaptistd={'Contact Details':'080-2202-4700', 'Consultation Cost':'Rs. 500', 'Beds Availability':'300', 'Cost of Beds':'Rs. 4500', 'Oxygen Availability':'Yes', 'Ambulance Service Cost':'Rs. 1000', 'Covid Vaccines Available':'Covaxin', 'CT SCAN Availibility':'No', 'Cost of CT SCAN':'N/A', 'MRI SCAN Availability':'No', 'Cost of MRI SCAN':'N/A', 'COVID TEST Availability':'Yes', 'Cost of COVID TEST':'Rs. 1200', 'X-RAY SCAN Availability':'Yes', 'Cost of X-RAY SCAN':'Rs. 700'}
kauveryd={'Contact Details':'080-6801-6801', 'Consultation Cost':'Rs. 700', 'Beds Availability':'300', 'Cost of Beds':'Rs. 5000', 'Oxygen Availability':'Yes', 'Ambulance Service Cost':'Rs. 1500', 'Covid Vaccines Available':'Covaxin', 'CT SCAN Availibility':'No', 'Cost of CT SCAN':'N/A', 'MRI SCAN Availability':'No', 'Cost of MRI SCAN':'N/A', 'COVID TEST Availability':'Yes', 'Cost of COVID TEST':'Rs. 1200', 'X-RAY SCAN Availability':'Yes', 'Cost of X-RAY SCAN':'Rs. 900'}
mallyad={'Contact Details':'080-6869-7979', 'Consultation Cost':'Rs. 650', 'Beds Availability':'300', 'Cost of Beds':'Rs. 5000', 'Oxygen Availability':'Yes', 'Ambulance Service Cost':'Rs. 1200', 'Covid Vaccines Available':'Covaxin', 'CT SCAN Availibility':'No', 'Cost of CT SCAN':'N/A', 'MRI SCAN Availability':'No', 'Cost of MRI SCAN':'N/A', 'COVID TEST Availability':'Yes', 'Cost of COVID TEST':'Rs. 1200', 'X-RAY SCAN Availability':'Yes', 'Cost of X-RAY SCAN':'Rs. 700'}

def sub_table_name(hospital_name):
    print(hospital_name)
    for key,value in hospital.items():
        if value==hospital_name:
            return key
def manipal():
    m=1
    for key,value in manipald.items():
        c1.execute('insert into manipal values('+str(m)+", "+"'"+key+"'"+", "+"'"+value+"'"+")")
        conn.commit()
        m+=1
def sakra():
    m=1
    for key,value in sakrad.items():
        c1.execute('insert into sakra values('+str(m)+", "+"'"+key+"'"+", "+"'"+value+"'"+")")
        conn.commit()
        m+=1
def columbia():
    m=1
    for key,value in columbiad.items():
        c1.execute('insert into columbia values('+str(m)+", "+"'"+key+"'"+", "+"'"+value+"'"+")")
        conn.commit()
        m+=1
def narayana():
    m=1
    for key,value in narayanad.items():
        c1.execute('insert into narayana values('+str(m)+", "+"'"+key+"'"+", "+"'"+value+"'"+")")
        conn.commit()
        m+=1    
def blossom():
    m=1
    for key,value in blossomd.items():
        c1.execute('insert into blossom values('+str(m)+", "+"'"+key+"'"+", "+"'"+value+"'"+")")
        conn.commit()
        m+=1       
def fortis():
    m=1
    for key,value in fortisd.items():
        c1.execute('insert into fortis values('+str(m)+", "+"'"+key+"'"+", "+"'"+value+"'"+")")
        conn.commit()
        m+=1      
def apollo():
    m=1
    for key,value in apollod.items():
        c1.execute('insert into apollo values('+str(m)+", "+"'"+key+"'"+", "+"'"+value+"'"+")")
        conn.commit()
        m+=1       
def aster():
    m=1
    for key,value in asterd.items():
        c1.execute('insert into aster values('+str(m)+", "+"'"+key+"'"+", "+"'"+value+"'"+")")
        conn.commit()
        m+=1    
def sparsh():
    m=1
    for key,value in sparshd.items():
        c1.execute('insert into sparsh values('+str(m)+", "+"'"+key+"'"+", "+"'"+value+"'"+")")
        conn.commit()
        m+=1   
def bgs():
    m=1
    for key,value in bgsd.items():
        c1.execute('insert into bgs values('+str(m)+", "+"'"+key+"'"+", "+"'"+value+"'"+")")
        conn.commit()
        m+=1     
def sagar():
    m=1
    for key,value in sagard.items():
        c1.execute('insert into sagar values('+str(m)+", "+"'"+key+"'"+", "+"'"+value+"'"+")")
        conn.commit()
        m+=1    
def ramaiah():
    m=1
    for key,value in ramaiahd.items():
        c1.execute('insert into ramaiah values('+str(m)+", "+"'"+key+"'"+", "+"'"+value+"'"+")")
        conn.commit()
        m+=1
def blrbaptist():
    m=1
    for key,value in blrbaptistd.items():
        c1.execute('insert into blrbaptist values('+str(m)+", "+"'"+key+"'"+", "+"'"+value+"'"+")")
        conn.commit()
        m+=1       
def kauvery():
    m=1
    for key,value in kauveryd.items():
        c1.execute('insert into kauvery values('+str(m)+", "+"'"+key+"'"+", "+"'"+value+"'"+")")
        conn.commit()
        m+=1  
def mallya():
    m=1
    for key,value in mallyad.items():
        c1.execute('insert into mallya values('+str(m)+", "+"'"+key+"'"+", "+"'"+value+"'"+")")
        conn.commit()
        m+=1
def beauty(j):
    for i in range(4):
        print('#',end='')
        time.sleep(0.1)
    print(j,end='')

def hospital_database():
    manipal()
    print('Fetching Database : \n0.00%',end='')
    sakra()
    beauty('7%')
    columbia()
    beauty('14%')
    narayana()
    beauty('22%')
    blossom()
    beauty('30%')
    fortis()
    beauty('38%')
    apollo()
    beauty('47%')
    aster()
    beauty('56%')
    sparsh()
    beauty('63%')
    bgs()
    beauty('70%')
    sagar()
    beauty('79%')
    ramaiah()
    beauty('86%')
    blrbaptist()
    beauty('92%')
    kauvery()
    beauty('97%')
    mallya()
    beauty('100%')
    print('')
    print('Successfully Fetched Database')
    print('===============================================')
    
    def ct():
            global ct_cost,ct
            ct=str(input("Enter if CT Scans are Available : "))
            ct_cost=0
            if ct in ('yes', 'Yes', 'YES', 'y'):
                ct="Yes"
                ct_cost=str(input("Enter the cost of a CT SCAN : "))
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
                mri_cost=str(input("Enter the cost of a MRI SCAN : "))
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
                cov_cost=str(input("Enter the cost of a COVID TEST : "))
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
                xray_cost=str(input("Enter the cost of a X-RAY SCAN : "))
            elif xray in ('no', 'No', 'NO', 'n'):
                xray="No"
                xray_cost="N/A"
            else:
                Print("ERROR : Input Not Recognised --- Please Enter either Yes or No")
                xray()
                
def ask():
    ask=input('enter if you want to repeat')
    if ask=='y'or'yes'or'YES'or'Yes'or'Y':
        add_hospital()
    elif ask=='n'or'no'or'NO'or'No'or'N':
        admin_mode()
    else:
        print('ERROR: ENTER ONLY YES OR NO')

def recover():
    global hospital_name
    recover=input('Enter Yes to continue or No to Cancel deletion : ')
    if recover in ['Yes','YES','yes','y','Y']:
        print('DELETING TABLE ',hospital_name)
        c1.execute('delete from hospitals where name='+"'"+hospital_name+"'")
        conn.commit()
        c1.execute('drop table '+sub_table_name(hospital_name))
        conn.commit()
        print('Deleting.',end='')
        for i in range(15):
            print('.',end='')
            time.sleep(0.75)
        print('')
        print('Succesfully Deleted',hospital_name)
        admin_mode()
    elif recover in ['no','NO','No','N','n']:
        print('You have cancelled deletion')
        admin_mode()
    else:
        print('ERROR : VALUE ENTERED NOT RECOGNISED - PLEASE ENTER ONLY YES OR NO')
        recover()
def remove_hospital():
    global hospital_name
    hospital_name=input('Enter the name of the Hospital to be REMOVED PERMANENTLY')
    print('The Hospital entered will be deleted PERMANENTLY with no means to recover data')
    recover()
def doctor_add():
     d_name=input('Enter Doctor Name:')
     d_age=int(input('Enter Age:'))
     d_hospital=str(input('Enter hospital:'))
     d_department=input('Enter the Department:')
     d_phono=int(input('Enter Phone number:'))
     c1.execute("insert into doctor_details values(%s, %s, %s, %s, %s)",(d_name, d_age, d_hospital, d_department, d_phono))
     conn.commit()
     print('successfully registered')
def recover_doctor():
        recover_doctor=input('Enter Yes to continue or No to Cancel deletion : ')
        if recover_doctor in ['Yes','YES','yes','y','Y']:
            print('DELETING Doctor Record of ',name_d)
            c1.execute('delete from doctor_details where name='+"'"+name_d+"'")
            conn.commit()
            print('Deleting.',end='')
            for i in range(15):
                print('.',end='')
                time.sleep(0.5)
            print('')
            print('Succesfully Deleted Doctor Records of ',name_d)
            admin_mode()
        elif recover in ['no','NO','No','N','n']:
            print('You have cancelled deletion')
            admin_mode()
        else:
            print('ERROR : VALUE ENTERED NOT RECOGNISED - PLEASE ENTER ONLY YES OR NO')
            recover_doctor()
def recover_patient():
        recover_patient=input('Enter Yes to continue or No to Cancel deletion : ')
        if recover_patient in ['Yes','YES','yes','y','Y']:
            print('DELETING Doctor Record of ',name_p)
            c1.execute('delete from patient_details where name='+"'"+name_p+"'")
            conn.commit()
            print('Deleting.',end='')
            for i in range(15):
                print('.',end='')
                time.sleep(0.5)
            print('')
            print('Succesfully Deleted Doctor Records of ',name_p)
            admin_mode()
        elif recover in ['no','NO','No','N','n']:
            print('You have cancelled deletion')
            admin_mode()
        else:
            print('ERROR : VALUE ENTERED NOT RECOGNISED - PLEASE ENTER ONLY YES OR NO')
            recover_doctor()
def doctor_remove():
    name_d=input('Enter Doctor Name to be removed(First+Last) :')
    print('The Doctor records entered will be deleted PERMANENTLY with no means to recover data')
    recover_doctor()
def patient_remove():
    name_p=input('Enter Patient Name to be removed(First+Last) :')
    print('The Patient records entered will be deleted PERMANENTLY with no means to recover data')
    recover_patient()
def view_doctor():
    c1.execute("select * from doctor_details group by hospital")
    r=c1.fetchall()
    for x in r:
        print(x)
def view_patients():
    c1.execute("select * from patient_details group by hospital")
    r=c1.fetchall()
    for x in r:
        print(x)

def hospital_details_deeper():
            global hosp
            hosp=int(input("Choose a hospital to view details (1-"+str(j-1)+"): "))#NO BUGS TILL HERE
            if(int(hosp)>0 and int(hosp)<j+1):
                c1.execute("select * from "+sub_table_name(dictt[hosp]))
                record = c1.fetchall()
                if len(record)>0:
                    for x in record:
                        print(x)
                if mode=='a':
                    admin_mode()
                elif mode=='p':
                    patient_mode()
            else:
                print('ERROR : Hospital Entered Not Recognised - Check Spelling and Re-Enter Hospital Name')
                hospital_details_deeper()
def hospitals():
    global j
    j=1
    c1.execute('select name, location, area from hospitals order by area asc')
    r = c1.fetchall()
    global dictt
    dictt={}
    print("   NAME     LOCATION        AREA")
    for i in r:
        print(j,' - ',i)
        dictt[j]=i[0]
        j+=1
    hospital_details_deeper()
    
def update_hospital():
    global hospital_name
    hospital_name=input('Enter the name of the Hospital for which you want to update the data')
    print('1:Name \n2:Location \n3:Area \4:Contact Details \n5:Consultation Cost \n6:Beds Availability \n7:Cost Of Beds \n8:Oxygen Availability \n9: Ambulance Service Cost \n10:Covid Vaccines Availability \n11:CT SCAN Availability \n12:Cost of CT SCAN \n13: MRI SCAN Availability')
    print('14:Cost of MRI SCAN \n15:COVID TEST Availability \n16:Cost of COVID TEST \n17:X-RAY SCAN Availability \n18:Cost of X-RAY SCAN')
    new_name=sub_table_name(hospital_name)
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
    
def patient_mode():        
      p_name=input('Enter Patient Name:')
      p_age=int(input('Enter Age:'))
      p_hospital=str(input("Enter hospial name from list"))
      p_problems=input('Enter the services requested:')
      p_phono=int(input('Enter Phone number:'))
      p_datetime=eval(input('Enter appointment date and time in YYMMDD hh:mm:00 xm format'))
      p_hospital=hosp
      c1.execute("insert into patient_details(Name, Age, Hospital, Services, Number) values(%s, %s, %s, %s, %s)",(p_name, p_age, p_hospital, p_problems, p_phono,))
      conn.commit()
      c1.execute("insert into patient_details(Timing) values(%s)",(p_datetime))
      conn.commit()
      print('SUCCESSFULLY REGISTERED')
      print('Your appointment(s):')
      c1.execute("select * from patient_details where Number=%s",(p_phono,))
      print("Redirecting...")
      main()
    
def admin_mode():
    print("1.Add hospital")
    print("2.Remove hospital")
    print("3.Alter hospital data")
    print('4.Show Doctors')
    print('5.Add Doctor')
    print('6.Remove Doctor')
    print('7.Show Hospitals')
    print('8.Show Patients')
    print('9.Delete Patients')
    print('10.Go back')
    ch = int(input("Enter choice"))
    if ch==1:
        add_hospital()
    elif ch==2:
        remove_hospital()
    elif ch==3:
        update_hospital()
    elif ch==4:
        view_doctor()
    elif ch==5:
        doctor_add()
    elif ch==6:
        doctor_remove()
    elif ch==7:
        hospitals()
    elif ch==8:
        view_patients()
    elif ch==9:
        patient_remove()
    elif ch==9:
        main()
    else:
        print('ERROR!: UNRECOGNISED VALUE - ENTER VALUE 1-9')
        
key='jfktn4runr1nf893kk'
l=[]
def main():
    global mode
    print("successfully connected") 
    print('1.Enter Patient Mode')
    print('2.Enter Administrator Mode ')
    print('3.Exit')
    choice=int(input('ENTER YOUR CHOICE:'))
    if choice==1:
        mode='p'
        hospitals()
    if choice==2:
        if key in l:
            mode='a'
            l.clear()
            admin_mode()
        else:
            print("ACCESS DENIED! Redirecting...")
            main()
    else:
        exit()

def Action():
    action=int(input('Enter 1 to book apointment or 2 to exit to main page'))
    if action==1:
        patient_mode()
    elif(action==2):
        main()
    else:
        print('ERROR!: ENTERED VALUE NOT RECOGNISED')
        Action()
    Action()
    
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
