from sys import exit
import mysql.connector as sql
import database
import pickle
conn=sql.connect(host='localhost',user='root',passwd='',database='project')
if conn.is_connected():
    print('successfully connected')
c1=conn.cursor()
print('---------------------------------------------')
print("COVID-19 PATIENT MANAGEMENT SYSTEM")
print('---------------------------------------------')

def welcome():
    print('WELCOME!')
    print("1.LOGIN")
    print("2.SIGN UP")
    print("3.EXIT")
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice==1:
        u1=str(input("enter user name:"))
        pwd1=str(input("enter the password:"))
        f=open("logindata.dat", "rb")
        while True:
            try:
                rec=pickle.load(f)
                if(rec["username"]==pwd1):
                   main()                   
                else:
                    print('Wrong username and/or password')
                    welcome()
            except EOFError:
                break
        f.close()
    if choice==2:
        u1=str(input("enter user name:"))
        pwd1=str(input("enter the password:"))
        rec={"username": us1, "password": pwd1}
        f=open("student.dat", "ab")
        pickle.dump(rec,f)
        f.close()
        welcome()
    if choice==3:
        exit()

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