import mysql.connector 
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="19Uma43*",
    database="onlineticket_db"
)
print("***********************WELCOME TO ONLINE BOOKING CENTER************************")
print("Log in using your credentials Username and Password")
try:
    username=input("Enter your Username:").lower().strip()
    password=int(input("Enter your password:"))
    print("LOGIN SUCCESSFULLY")
except ValueError:
            print("LOGIN SUCCESSFULLY")
Vehicles=["1-Bus","2-Train","3-Flight"]
for i in Vehicles:
    print(i)
def data(Vehicles):
    if Vehicles=="1":
        print("~~~WELCOME TO BUS TICKET BOOKING AND RESERVATION~~~")
        vehicle=input("Enter your Vehicle Name:")
        Name=input("Enter your Name:")
        gender=input("Enter your gender:")
        try:
            age=int(input("Enter your age:"))
        except ValueError:
            print("Plese enter the number only")
        From=input("Enter your Travelling From:")
        To=input("Enter your Travelling To:")
        Date=input("Enter your Journey Date:")
        Bus_Type=["ac bus","non-ac bus","sleeper seater bus","smart bus","deluxe bus","luxury bus"]
        for i in Bus_Type:
            print(i)
        def data(Bus_Type):
            if Bus_Type=="ac bus":
                print("AC buses make sure that your jouney is comfortable and cozy")
            elif Bus_Type=="non-aC bus":
                print("you are looking for cheaper option")
                print("Wouldn't be travelling on longer distance")
            elif Bus_Type=="sleeper seater bus":
                print("When you tired and are looking to rest while travelling")
            elif Bus_Type=="smart bus":
                print("If you're worried about the long interval breaks during and long journey")
                print("This bus comes inbuilt toilets that are practical to use")
            elif Bus_Type=="deluxe bus":
                print("Enjoy luxury road journeys on budget")
            elif Bus_Type=="luxury bus":
                print("If the best luxury on wheels is what your heart wants")
        choice=input("Enter your Bus Type in above list:").lower().strip()
        data(choice)
        Amount=input("Enter your Initial Amount:")
        amount=input("can you pay the fully amount before travel:")
        if amount=="yes":
            print("thankyou your ticket is confirm")
            print("please pay the full amount before you start the journey")
            print("If the OTP is coming,Your ticket is confirmed ")
            import random
            print(random.randint(1000,9999))
            print("your ticket is booked")
            print("~~~~FREE CANCELLATION AND RESCHEDULING OF BUS TICKETS~~~~") 
            cancel=input("Can you cancel the bus tickets?:")
            if cancel=="yes":
                print("Reschedule bus booking to a future date by simply paying the difference price,if applicable")
            else:
                print("Thankyou for this conformation **ENJOY YOUR JOURNEY**")
                Paasenger_Name=Name
                Traveeling_From=From
                Travelling_To=To
                Vehicle=choice
                Initial_Amount=Amount
                val=(Name,From,To,choice,Amount)
                sql="insert into Details(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount) values (%s,%s,%s,%s,%s)"
                mycursor = mydb.cursor()
                mycursor.execute(sql,val)
                mydb.commit()
                def insert(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount):
                    res=mydb.cursor()
                    sql="insert into details(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount) values (%s,%s,%s,%s,%s)"
                    details=(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount)
                    res.execute(sql,details)
                    mydb.commit()
                    print("Data Insert Successfully")
                def update(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount):
                    res=mydb.cursor()
                    sql="update details set Passenger_Name=%s,Traveeling_From=%s,Travelling_To=%s,Vehicle=%s,Initial_Amount=%s"
                    details=(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount)
                    res.execute(sql,details)
                    mydb.commit()
                    print("Data Update Successfully")
                def select():
                    res=mydb.cursor()
                    sql="select Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount from details"
                    res.execute(sql)
                    result=res.fetchall()
                    print(result)
                    print("Data Selected Successfully")
                def delete(Passenger_Name):
                    res=mydb.cursor()
                    sql="delete from details where Passenger_Name=%s"
                    details=(Passenger_Name,)
                    res.execute(sql,details)
                    mydb.commit()
                    print("Data Delete Successfully")
                while True:
                    print("1.Insert Data")
                    print("2.Update Data")
                    print("3.select data")
                    print("4 Delete data")
                    print("5.Quit")
                    Choice=int(input("Enter your choice:"))
                    if Choice==1:
                        Passenger_Name=input("Enter your name:")
                        Traveeling_From=input("From Place:")
                        Travelling_To=input("To Place:")
                        Vehicle=input("Enter your Vehicle:")
                        Initial_Amount=input("Enter your Initial Amount:")
                        insert(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount)
                    elif Choice==2:
                        Passenger_Name=input("Enter your name:")
                        Traveeling_From=input("From Place:")
                        Travelling_To=input("To Place:")
                        Vehicle=input("Enter your Vehicle:")
                        Initial_Amount=input("Enter your Initial Amount:")
                        update(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount)
                    elif Choice==3:
                        select()
                    elif Choice==4:
                        Passenger_Name=input("Enter the Name to delete:")
                        delete(Passenger_Name)
                    elif Choice==5:
                        quit()
                    else:
                        print("invalid selection.please try again")
        
        
        else:
            print("Please pay the full amount and after get the OTP")
            
    elif Vehicles=="2":
        print("~~~WELCOME TO TRAIN TICKET BOOKING AND RESERVATION~~~")
        vehicles=input("Enter your Vechile Name:")
        passenger_Name=input("Enter your Name:")
        gender=input("Enter your gender:")
        try:
            age=int(input("Enter your age:"))
        except ValueError:
            print("Plese enter the number only")
        Travelling_From=input("Travelling From:")
        Traveeling_To=input("Travelling To:")
        Date=input("Enter your Journey Date:")
        Amount=input("Enter your Initial Amount:")
        amount=input("can you pay the fully amount before travel:")
        if amount=="yes":
            print("thankyou your ticket is confirm")
            print("please pay the full amount before you start the journey")
            print("If the OTP is coming,Your ticket is confirmed ")
            import random
            print(random.randint(1000,9999))
            print("your ticket is booked")
            print("~~~~FREE CANCELLATION AND RESCHEDULING OF TRAIN TICKETS~~~~") 
            print("Confirmed e-Tickets bookings can be cancelled up to 4 hours before the scheduled departure")
            print("RAC and Waitlisted e-Tickets can be cancelled up to 30 Minutes before the scheduled departure")
            cancel=input("Can you cancel the Train tickets?:")
            if cancel=="yes":
                print("Reschedule bus booking to a future date by simply paying the difference price,if applicable")
                print("You ticket will get canceled successfully")
            else:
                print("Thankyou for this conformation **ENJOY YOUR JOURNEY**")
                Paasenger_Name=passenger_Name
                Traveeling_From=Travelling_From
                Travelling_To=Traveeling_To
                Vehicle=vehicles
                Initial_Amount=Amount
                val=(passenger_Name,Travelling_From,Traveeling_To,vehicles,Amount)
                sql="insert into Details(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount) values (%s,%s,%s,%s,%s)"
                mycursor = mydb.cursor()
                mycursor.execute(sql,val)
                mydb.commit()
                def insert(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount):
                    res=mydb.cursor()
                    sql="insert into details(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount) values (%s,%s,%s,%s,%s)"
                    details=(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount)
                    res.execute(sql,details)
                    mydb.commit()
                    print("Data Insert Successfully")
                def update(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount):
                    res=mydb.cursor()
                    sql="update details set Passenger_Name=%s,Traveeling_From=%s,Travelling_To=%s,Vehicle=%s,Initial_Amount=%s"
                    details=(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount)
                    res.execute(sql,details)
                    mydb.commit()
                    print("Data Update Successfully")
                def select():
                    res=mydb.cursor()
                    sql="select Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount from details"
                    res.execute(sql)
                    result=res.fetchall()
                    print(result)
                    print("Data Selected Successfully")
                def delete(Passenger_Name):
                    res=mydb.cursor()
                    sql="delete from details where Passenger_Name=%s"
                    details=(Passenger_Name,)
                    res.execute(sql,details)
                    mydb.commit()
                    print("Data Delete Successfully")
                while True:
                    print("1.Insert Data")
                    print("2.Update Data")
                    print("3.select data")
                    print("4 Delete data")
                    print("5.Quit")
                    Choice=int(input("Enter your choice:"))
                    if Choice==1:
                        Passenger_Name=input("Enter your name:")
                        Traveeling_From=input("From Place:")
                        Travelling_To=input("To Place:")
                        Vehicle=input("Enter your Vehicle:")
                        Initial_Amount=input("Enter your Initial Amount:")
                        insert(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount)
                    elif Choice==2:
                        Passenger_Name=input("Enter your name:")
                        Traveeling_From=input("From Place:")
                        Travelling_To=input("To Place:")
                        Vehicle=input("Enter your Vehicle:")
                        Initial_Amount=input("Enter your Initial Amount:")
                        update(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount)
                    elif Choice==3:
                        select()
                    elif Choice==4:
                        Passenger_Name=input("Enter the Name to delete:")
                        delete(Passenger_Name)
                    elif Choice==5:
                        quit()
                    else:
                        print("invalid selection.please try again")
        
        else:
            print("Please pay the full amount and after get the OTP")         
    elif Vehicles=="3":
        print("~~~WELCOME TO FLIGHT TICKET BOOKING AND RESERVATION~~~")
        VEHICLE=input("Enter your Vechile Name:")
        passenger_name=input("Enter your Name:")
        gender=input("Enter your gender:")
        try:
            age=int(input("Enter your age:"))
        except ValueError:
            print("Plese enter the number only")
        travelling_from=input("Travelling From:")
        travelling_to=input("Travelling To:")
        Date=input("Enter your Journey Date:")
        amnt=input("Enter your Initial Amount:")
        amount=input("can you pay the fully amount before travel:")
        if amount=="yes":
            print("thankyou your ticket is confirm")
            print("please pay the full amount before you start the journey")
            print("If the OTP is coming,Your ticket is confirmed ")
            import random
            print(random.randint(1000,9999))
            print("your ticket is booked")
            print("~~~~FREE CANCELLATION AND RESCHEDULING OF FLIGHT TICKETS~~~~") 
            print("Confirmed e-Tickets bookings can be cancelled up to 4 hours before the scheduled departure")
            print("RAC and Waitlisted e-Tickets can be cancelled up to 30 Minutes before the scheduled departure")
            cancel=input("Can you cancel the Flight tickets?:")
            if cancel=="yes":
                print("Reschedule bus booking to a future date by simply paying the difference price,if applicable")
                print("You ticket will get canceled successfully")
            else:
                print("~~~~TICKET CHECKING PROCESS~~~~")
                ticket_check=input("Enter your Ticket Status valid or not:").lower().strip()
                if ticket_check=="valid":
                    print("````````````````WELCOME TO AIRPORT```````````````````")
                    corona_check=input("Enter your Corona Status Positive or Negative:").lower().strip()
                    if corona_check=="negative":
                        print("you are allowed in the airport")
                        passport=input("Enter Your Passport Status valid or not:").lower().strip()
                        visa=input("Enter your Visa Status valid or not:").lower().strip()
                        photo=input("Enter your Current Photo valid or not:").lower().strip()
                        thumb_impression=input("Enter your Thumb Impression valid or not:").lower().strip()
                        if passport=="valid" and visa=="valid" and photo=="valid" and thumb_impression=="valid":
                            print("You are go to Bag Checking Section")
                            bag_weight=int(input("Enter your Bag Weight:"))
                            if bag_weight<=20:
                                print("Your Bag Weight is correct in weight")
                                boarding_pass=input("Enter your Boarding Pass Status valid or not:").lower().strip()
                                if boarding_pass=="valid":
                                    print("You are Eligible for Travel")
                                    Paasenger_Name=passenger_name
                                    Traveeling_From=travelling_from
                                    Travelling_To=travelling_to
                                    Vehicle=VEHICLE
                                    Initial_Amount=amnt
                                    val=(passenger_name,travelling_from,travelling_to,VEHICLE,amnt)
                                    sql="insert into Details(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount) values (%s,%s,%s,%s,%s)"
                                    mycursor = mydb.cursor()
                                    mycursor.execute(sql,val)
                                    mydb.commit()
                                    def insert(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount):
                                        res=mydb.cursor()
                                        sql="insert into details(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount) values (%s,%s,%s,%s,%s)"
                                        details=(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount)
                                        res.execute(sql,details)
                                        mydb.commit()
                                        print("Data Insert Successfully")
                                    def update(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount):
                                        res=mydb.cursor()
                                        sql="update details set Passenger_Name=%s,Traveeling_From=%s,Travelling_To=%s,Vehicle=%s,Initial_Amount=%s"
                                        details=(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount)
                                        res.execute(sql,details)
                                        mydb.commit()
                                        print("Data Update Successfully")
                                    def select():
                                        res=mydb.cursor()
                                        sql="select Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount from details"
                                        res.execute(sql)
                                        result=res.fetchall()
                                        print(result)
                                        print("Data Selected Successfully")
                                    def delete(Passenger_Name):
                                        res=mydb.cursor()
                                        sql="delete from details where Passenger_Name=%s"
                                        details=(Passenger_Name,)
                                        res.execute(sql,details)
                                        mydb.commit()
                                        print("Data Delete Successfully")
                                    while True:
                                        print("1.Insert Data")
                                        print("2.Update Data")
                                        print("3.select data")
                                        print("4 Delete data")
                                        print("5.Quit")
                                        Choice=int(input("Enter your choice:"))
                                        if Choice==1:
                                            Passenger_Name=input("Enter your name:")
                                            Traveeling_From=input("From Place:")
                                            Travelling_To=input("To Place:")
                                            Vehicle=input("Enter your Vehicle:")
                                            Initial_Amount=input("Enter your Initial Amount:")
                                            insert(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount)
                                        elif Choice==2:
                                            Passenger_Name=input("Enter your name:")
                                            Traveeling_From=input("From Place:")
                                            Travelling_To=input("To Place:")
                                            Vehicle=input("Enter your Vehicle:")
                                            Initial_Amount=input("Enter your Initial Amount:")
                                            update(Passenger_Name,Traveeling_From,Travelling_To,Vehicle,Initial_Amount)
                                        elif Choice==3:
                                            select()
                                        elif Choice==4:
                                            Passenger_Name=input("Enter the Name to delete:")
                                            delete(Passenger_Name)
                                        elif Choice==5:
                                            quit()
                                        else:
                                            print("invalid selection.please try again")      
                                else:
                                    print("Sorry you can't allowed")
                            else:
                                print("Please reduce your weight otherwise you will pay extra amount per kg")
                        else:
                            print("Please Check you passport or visa or idcard or corona status or thumb impression")
                    else:
                        print("Sorry you can't allowed you")
                else:
                  print("please check your Tickets")  
    else:
        print("Sorry.Invalid Selection!!")
Choice=input("Enter the Number in Above List:").lower().strip()
data(Choice)