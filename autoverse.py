#################################################
import mysql.connector
def register():
    print("\t \t \t \t Registration Page \t")
    while True:
        print("Press 1 : Customer")
        print("Press 2 : Auto Driver")
        try:
            ch = input("Enter your choice: ")
            if ch=="1":
                print("\t \t \t \t Customer \t")
                try:
                    cust=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='project')
                    cust_cur=cust.cursor()
                except Exception as error3:
                    print(error3)
                    print("Something went wrong please try again")
                    print("Please enusre that you have genuine access to software ")
                    print("Auto exiting program")
                    exit() 
                cust_name=input("Enter the name: ")
                cust_mobile  =int(input("Enter the number: "))
                cust_passwd=input("Enter a passwd: ")
                cust_pincode=input("Enter the pincode:")
                qry="select max(cust_id) from customer "
                cust_cur.execute(qry)
                idd=cust_cur.fetchone()
                num=int(idd[0].lstrip("C_"))+1
                num='C_'+str(num)
                cust_query="insert into customer (cust_id,cust_name,mobile_number,cust_passwd,pincode) values('{}','{}','{}','{}','{}')".format(num,cust_name,cust_mobile,cust_passwd,cust_pincode)
                cust_cur.execute(cust_query)
                cust.commit()
                try:
                    cust2=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='project')
                    cust2_cur=cust2.cursor()
                except Exception as error4:
                    print(error4)
                    print("Something went wrong please try again")
                    print("Please enusre that you have genuine access to software ")
                    print("Auto exiting program")
                    exit()
                cust2_query="select cust_id from customer where mobile_number='{}'".format(cust_mobile)
                cust2_cur.execute(cust2_query)
                x=cust2_cur.fetchall()
                cust2.commit
                print("Successfully registered please login with the details below")
                print(x,"is you customer id")
                print(cust_passwd,"is your password")
                login_fun()
                break
            elif ch=="2":
                try:
                    auto=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='project')
                    auto_cur=auto.cursor()
                except Exception as error1:
                    print(error1)
                    print("Something went wrong please try again")
                    print("Please enusre that you have genuine access to software ")
                    print("Auto exiting program")
                    exit() 
                print("\t \t \t \t Auto Driver \t")
                driver_name=input("Enter your name: ")
                mob_number=input("Enter your  mobile number: " )
                number_plate=input("Enter the your vehicle's number or number plate code: ")
                auto_passwd=input("Enter a password: ")
                driver_pincode=input("Enter your pincode:")
                landmark=input('Enter a landmark near your stand:')
                status="default"
                qry1="select max(driver_id) from auto_driver "
                auto_cur.execute(qry1)
                idd1=auto_cur.fetchone()
                num1=int(idd1[0].lstrip("A_"))+1
                num1='A_'+str(num1)
                auto_query="insert into auto_driver (driver_id,driver_name,mobile_number,number_plate,auto_passwd,driver_pincode,landmark) values ('{}','{}','{}','{}','{}','{}','{}')".format(num1,driver_name,mob_number,number_plate,auto_passwd,driver_pincode,landmark)
                auto_cur.execute(auto_query)
                auto.commit()
                try:
                    auto2=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='project')
                    auto2_cur=auto.cursor()
                except Exception as error2:
                    print(error2)
                    print("Something went wrong please try again")
                    print("Please enusre that you have the database")
                    print("Auto exiting program")
                    exit()
                auto2_query="select driver_id from auto_driver where mobile_number='{}'".format(mob_number)
                auto2_cur.execute(auto2_query)
                q=auto2_cur.fetchall()
                auto2.commit
                print("Successfully registered please login with the details below")
                print(q,"is you driver id")
                print(auto_passwd,"is your password")
                login_fun()
                break
            else: print("Wrong input please try again")
        except Exception as error:
            print(error)
            print("An unexpected error occured please check the inputs and try again")

 #################################################       

def admin_fun():
    while True:
        print("\t \t \t \t Admin\t")
        try:
            admin_code=input("Enter the admin code")
            if admin_code=="H":
                print("Access Granted")
                while True:
                    print("Press 1 : Auto Driver Settings ")
                    print("Press 2 : Customer  Settings")    
                    choice1=input("Enter Your Choice")
                    if choice1=='1':
                        while True:
                            print("Press 0 : View Database")
                            print("Press 9 : Delete a Record")  
                            ch=input("Enter the choice")
                            if ch=='0':
                                try:
                                    admin=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='project')
                                    admin_cur=admin.cursor()
                                except Exception as error2:
                                    print(error2)
                                    print("Something went wrong please try again")
                                    print("Please enusre that you have genuine access to software ")
                                    print("Auto exiting program")
                                    exit()                                     
                                admin_query="select * from auto_driver"
                                admin_cur.execute(admin_query)
                                x=admin_cur.fetchall()
                                for i in x:
                                    print(i)
                                admin.commit()
                                admin2()
                            elif ch=='9':
                                try:
                                    admin=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='project')
                                    admin_cur=admin.cursor()
                                except Exception as error3:
                                    print(error3)
                                    print("Something went wrong please try again")
                                    print("Please enusre that you have genuine access to software ")
                                    print("Auto exiting program")
                                    exit()          
                                dlt_A_id=input("Enter the id to be deleted")
                                admin_query="delete from auto_driver where driver_id='{}'".format(dlt_A_id)
                                admin_cur.execute(admin_query)
                                admin.commit()
                                print(dlt_A_id,"is deleted")
                                admin2()
                            else:
                                print("Wrong Input")
                                continue
                    elif choice1=='2':
                        while True:
                            print("Press 5 : View Database")
                            print("Press 6 : Delete a record")      
                            ch1=input("Enter the choice :")
                            if ch1=='5':
                                try:
                                    admin1=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='project')
                                    admin1_cur=admin1.cursor()
                                except Exception as error4:
                                    print(error4)
                                    print("Something went wrong please try again")
                                    print("Please enusre that you have genuine access to software ")
                                    print("Auto exiting program")
                                    exit()          
                                admin1_query="select * from customer"
                                admin1_cur.execute(admin1_query)
                                y=admin1_cur.fetchall()
                                for z in y:
                                    print(z)
                                admin1.commit()      
                                admin2()
                            elif ch1=='6':
                                try:
                                    admin1=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='project')
                                    admin1_cur=admin1.cursor()
                                except Exception as error5:
                                    print(error5)
                                    print("Something went wrong please try again")
                                    print("Please enusre that you have genuine access to software ")
                                    print("Auto exiting program")
                                    exit()          
                                dlt_C_id=input("Enter the id to be deleted")
                                admin1_query="delete from customer where cust_id='{}'".format(dlt_C_id)
                                admin1_cur.execute(admin1_query)
                                admin1.commit()
                                print(dlt_C_id,"is deleted")
                                admin2()
                            else:
                                print("Wrong Input Please Re-enter")
                                continue
                    else:
                        print("Wrong Input Please Re-enter")
                        continue
            else:
                    print("Access Denied")
                    print("Press 1 : Try again if you are an Admin")
                    print("Press Any other Key : Choose an alternative login option ")
                    ch=input("Enter your choice")                
                    if ch=="1":
                        continue
                    else:
                        main_menu()
                    break
        except Exception as error:
            print(error)
            print("An unexpected error occured please check the inputs and try again")

################################################

def admin2():
    while True:
        try:
            print("Press 0 :  Continue in Admin Page")
            print("Press 9 : Go back to Main Menu")
            choice=int(input("Enter your choice :"))
            if choice==0:
                admin_fun()
                break
            elif choice==9:
                main_menu()
                break
            else:
                print("Wrong input please try again")
                continue
        except Exception as error:
            print(error)
            print("An unexpected error occured please check the inputs and try again")
                    
        
#################################################

def main_menu():
    while True:
        try:
            print("Press 1 : New User")
            print("Press 2 : Already A User")
            print("Press 3 : Admin")
            print("Press 4 : Exit")
            print("Press 5 : Devloper info")
            choice=input("Enter Your Choice")
            if choice=="1":
                register()
                break
            elif choice=='2':
                login_fun()
                break
            elif choice=='3':
                admin_fun()
                break
            elif choice=='4':
                print("Press Any Key  : To Confrim Exit")
                print("Press 2 : To Not Exit")
                ch=input("Enter your Choice")
                if ch=='2':
                    main_menu()
                else:
                    print("Exiting......")
                    exit()
                    break
            elif choice=='5':
                developer_info()
                break
            else:
                print("Wrong Input Try Again")
                continue
        except Exception as error:
            print(error)
            print("An unexpected error occured please check the inputs and try again")
                    

################################################# 


def login_fun():
    try:
        print("\t \t \t \t Login Page\t")
        global L_idd
        L_idd=input("Enter your id: ")
        try:
            login=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='project')
            login_cur=login.cursor()
        except Exception as error5:
            print(error5)
            print("Something went wrong please try again")
            print("Please enusre that you have genuine access to software ")
            print("Auto exiting program")
            exit()     
        login_query= "select cust_id from customer"                                                            
        login_cur.execute(login_query)
        Lx_cust=login_cur.fetchall()
        flag=False
        for i in Lx_cust:
            if i[0]==str(L_idd):
                flag=True
                customer_fun()
                break
        if flag==False:
            try:
                login=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='project')
                login_cur=login.cursor()
            except Exception as error4:
                print(error4)
                print("Something went wrong please try again")
                print("Please enusre that you have genuine access to software ")
                print("Auto exiting program")
                exit()     
            login_query= "select driver_id from auto_driver"
            login_cur.execute(login_query)
            Lx_driver=login_cur.fetchall()
            for i in Lx_driver:
                if i[0]==str(L_idd):
                    auto_driver_fun()
                    flag=True
                    break
        if flag==False:
            print("Invalid id")
            print("Press 1 : Relogin")
            print("Press 2 : Main Menu")
            while True:
                L_ch=int(input("Enter your choice"))
                if L_ch==1:
                    login_fun()
                    break
                elif L_ch==2:
                    main_menu()
                    break
                else:
                    continue
    except Exception as error:
        print(error)
        print("An unexpected error occured please check the inputs and try again")
        login_fun()
                    

################################################# 

def auto_driver_fun():
    print("Logged in as Auto Driver")
    while True:
        try:
            print("Press 1 : Available")
            print("Press 2 : Not Available")
            print("Press 3 : Main Menu")
            print("Press 4 : Report A Customer")
            ch1=input("Enter your choice:")
            if ch1=="1":
                try:
                    auto_status=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='project')
                    auto_status_cur=auto_status.cursor()
                except Exception as error5:
                    print(error5)
                    print("Something went wrong please try again")
                    print("Please enusre that you have genuine access to software ")
                    print("Auto exiting program")
                    exit()     
                auto_status_cur.execute(auto_status_query)
                auto_status.commit()
                print("Now you are available to take passengers if not press 2 below")
                auto_driver_fun()
            elif ch1=="2":
                try:
                    auto_status=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='project')
                    auto_status_cur=auto_status.cursor()
                except Exception as error4:
                    print(error4)
                    print("Something went wrong please try again")
                    print("Please enusre that you have genuine access to software ")
                    print("Auto exiting program")
                    exit()     
                auto_status_query= "update auto_driver set availability_status='NA' where driver_id='{}'".format(L_idd)                                                           
                auto_status_cur.execute(auto_status_query)
                auto_status.commit()
                print("Now you are not available to take passengers if you are press 1 below")
                auto_driver_fun()
            elif ch1=="3":
                main_menu()
                break
            elif ch1=="4":
                print("Email us on contact.app@gmail.com with their name and mobile number with a short description")
                print("Continue with an other choice")
                auto_driver_fun()
            else:
                print("Wrong input Try Again")
                continue
        except Exception as error:
            print(error)
            print("An unexpected error occured please check the inputs and try again")
             
                    
#################################################

def customer_fun():
    print("Logged in as Customer")
    while True:
        try:
            print("Press 1 : View Available Autos")
            print("Press 2 : Main Menu")
            print("Press 3 : Report A Driver") 
            ch2=input("Enter your choice")
            if ch2=="1":
                pin=input("Enter your curent pincode")
                try:
                    customer_booking=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='project')
                    customer_booking_cur=customer_booking.cursor()
                except Exception as error4:
                    print(error4)
                    print("Something went wrong please try again")
                    print("Please enusre that you have genuine access to software ")
                    print("Auto exiting program")
                    exit()   
                customer_booking_query= "select driver_name, mobile_number, landmark from auto_driver where availability_status = 'A' and driver_pincode='{}'".format(pin)
                customer_booking_cur.execute(customer_booking_query)
                customer_booking_dtls=customer_booking_cur.fetchall()
                if len(customer_booking_dtls)==0:
                    print("No autos are available at the moment")
                else:
                    print("Available Autos")
                    for i in customer_booking_dtls:
                        print(i)
                print("Continue with an another choice")
                customer_fun()
            elif ch2=="2":
                main_menu()
                break
            elif ch2=='3':
                print("Email us on contact.app@gmail.com with their name and mobile number with a short description")
                print("Continue with an other choice")
                customer_fun()
            else :
                print("Wrong Input Please Try Again")
                continue
        except Exception as error:
             print(error)
             print("An unexpected error occured please check the inputs and try again")
             

#################################################

def developer_info():
    try:
        print(" credits to auoverse")
    except Exception as error4:
        print(error4)
        print("Something went wrong please try again")
        print("Please enusre that you have genuine access to software ")
        print("Auto exiting program")
        exit()   

################################################

print("\t \t \t \t AUTO_VERSE\t")
try:
    main_menu()
except Exception as error4:
    print(error4)
    print("Something went wrong please try again")
    print("Please enusre that you have genuine access to software ")
    print("Auto exiting program")
    exit()   
   
           
    
