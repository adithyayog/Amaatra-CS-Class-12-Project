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
