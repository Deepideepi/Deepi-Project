import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="19Uma43*",
    database="atm_machine_db" 
)
print("*****************WELCOME TO ATM MACHINE******************")
atm_id="B1233200"
option=["1.Deposit Cash","2.Withdrawal Cash","3.Exit"]
for i in option:
    print(i)
def data(option):
    if option==1:
        print("Please Insert Your Card")
        customer_name=input("Enter Your Name:")
        try:
            pin=int(input("Enter Your PIN Number:"))
            print(f"Your Name is  {customer_name}")
            print(f"Your PIN Number is {pin}")
            check=input("Please Confirm above details if they are Correct or Incorect?:").lower().strip()
            if check=="correct":
                print("Please Wait")
                print("I am Depositing the case Deposit/Cheque through ATM.Accept the following the Amount and other contents are verified by the Bank will be conclusive.Binding on me for all purposes and I shall not raise any dispute in respect of the said Transactor")
                condition=input("Should You Agree the above condion YES or NO:").lower().strip()
                if condition=="yes":
                    print("Please select the Next option")
                    type=input("Enter Your Account Type SAVING or CURRENT:").lower().strip()
                    deposit_amnt=int(input("Enter Your Deposit Amount:"))
                    print("The Cash in out box is opened")
                    print("Please Put the Amount in Cash in out box")
                    print("Please deposit the cash in Rs.100,Rs.500,Rs.2000 Denominators only")
                    print("Please do not deposit more than 200 Notes at the time")
                    confirm=input("The above condition Yes or No:").lower().strip()
                    if confirm=="yes":
                        print("Your Cash is being Verified")
                        print("Bad notes are detected")
                        print("Your transaction will be proceed with Good notes")
                        conformation=input("Please confirm the Transaction Amount Deposit or Cancel?:").lower().strip()
                        if conformation=="deposit":
                            print("Your Transaction Completed Successfully")
                            print("Please take the receipt")
                            print("***********************************************")
                            import datetime
                            now=datetime.datetime.now()
                            print("Current date and time:")
                            print(now.strftime("%d-%m-%Y/t %H:%M:%S"))
                            print(f"ATM-ID: {atm_id}")
                            print(f"Name: {customer_name}")
                            print(f"PIN Number: {pin}")
                            print(f"Deposit Amount: {deposit_amnt}")
                            print("~~~~~~~~~~THANK YOU,PLEASE VISIT AGAIN~~~~~~~~~~")
                            Name=customer_name
                            PIN=pin
                            Deposit_Amount=deposit_amnt
                            Account_Type=type
                            val=(customer_name,pin,deposit_amnt,type)
                            sql="insert into deposit_details(Name,PIN,Deposit_Amount,Account_Type) values (%s,%s,%s,%s)"
                            mycursor = mydb.cursor()
                            mycursor.execute(sql,val)
                            mydb.commit()   
                            def insert(Name,PIN,Deposit_Amount,Account_Type):
                                res=mydb.cursor()
                                sql="insert into deposit_details(Name,PIN,Deposit_Amount,Account_Type) values (%s,%s,%s,%s)"
                                Deposit_details=(Name,PIN,Deposit_Amount,Account_Type)
                                res.execute(sql,Deposit_details)
                                mydb.commit()
                                print("Data Insert Successfully")
                            def update(Name,PIN,Deposit_Amount,Account_Type):
                                res=mydb.cursor()
                                sql="update  deposit_details set Name=%s,PIN=%s,Deposit_Amount=%s,Account_Type=%s"
                                deposit_details=(Name,PIN,Deposit_Amount,Account_Type)
                                res.execute(sql,deposit_details)
                                mydb.commit()
                                print("Data Update Successfully")
                            def select():
                                res=mydb.cursor()
                                sql="select Name,PIN,Deposit_Amount,Account_Type from deposit_details"
                                res.execute(sql)
                                result=res.fetchmany()
                                print(result)
                                print("Data Select Successfully")
                            def delete(Name):
                                res=mydb.cursor()
                                sql="delete from  deposit_details where Name=%s"
                                deposit_details=(Name,)
                                res.execute(sql,deposit_details)
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
                                    Name=input("Enter your name:")
                                    PIN=input("Enter your pin:")
                                    Deposit_Amount=input("Enter your Deposit Amount:")
                                    Account_Type=input("Enter your Account Type:")
                                    insert(Name,PIN,Deposit_Amount,Account_Type)
                                elif Choice==2:
                                    Name=input("Enter your name:")
                                    PIN=input("Enter your pin:")
                                    Deposit_Amount=input("Enter your deposit Amount:")
                                    Account_Type=input("Enter your Account Type:")
                                    update(Name,PIN,Deposit_Amount,Account_Type) 
                                elif Choice==3:
                                    select()
                                elif Choice==4:
                                    Name=input("Enter the Name to delete:")
                                    delete(Name)
                                elif Choice==5:
                                    quit()
                                else:
                                    print("invalid selection.please try again")
                        elif conformation=="cancel":
                            print("Sorry Your Transaction is Cancelled!")
                        else:
                            print("Invalid Option")               
                    else:
                        print("Sorry Invalid Option")          
                
                else:
                    print("Option Invalid")
            else:
                print("please Re-enter the Details")
        except ValueError:
            print(" Please enter the number only") 
    elif option==2:
        print("Please Insert Your Card")
        Customer_Name=input("Enter Your Name:")
        try:
            Pin=int(input("Enter Your PIN Number:"))
            print(f"Your Name is  {Customer_Name}")
            print(f"Your PIN Number is {Pin}")
            check=input("Please Confirm above details if they are Correct or Incorect?:").lower().strip()
            if check=="correct":
                print("Please Wait")
                print("Make sure that you do not enter a withdrawal amount more than the balance in your account")
                condition=input("Should You Agree the above condion YES or NO:").lower().strip()
                if condition=="yes":
                    print("Please select the Next option")
                    Type=input("Enter Your Account Type SAVING or CURRENT:").lower().strip()
                    Withdrawal_amnt=int(input("Enter Your Withdrawal Amount:"))
                    print("Please take the cash")
                    print("Please take the receipt")
                    print("***********************************************")
                    import datetime
                    now=datetime.datetime.now()
                    print("Current date and time:")
                    print(now.strftime("%d-%m-%Y/t %H:%M:%S"))
                    print(f"ATM-ID: {atm_id}")
                    print(f"Name: {Customer_Name}")
                    print(f"PIN Number: {Pin}")
                    print(f"Deposit Amount: {Withdrawal_amnt}")
                    print("~~~~~~~~~~THANK YOU,PLEASE VISIT AGAIN~~~~~~~~~~")
                    Name=Customer_Name
                    PIN=Pin
                    Deposit_Amount=Withdrawal_amnt
                    Account_Type=Type
                    val=(Customer_Name,Pin,Withdrawal_amnt,Type)
                    sql="insert into deposit_details(Name,PIN,Deposit_Amount,Account_Type) values (%s,%s,%s,%s)"
                    mycursor = mydb.cursor()
                    mycursor.execute(sql,val)
                    mydb.commit() 
                    def insert(Name,PIN,Withdrawal_Amount,Account_Type):
                        res=mydb.cursor()
                        sql="insert into withdrawal_details(Name,PIN,Withdrawal_Amount,Account_Type) values (%s,%s,%s,%s)"
                        Withdrawal_details=(Name,PIN,Withdrawal_Amount,Account_Type)
                        res.execute(sql,Withdrawal_details)
                        mydb.commit()
                        print("Data Insert Successfully")
                    def update(Name,PIN,Withdrawal_Amount,Account_Type):
                        res=mydb.cursor()
                        sql="update  withdrawal_details set Name=%s,PIN=%s,Withdrawal_Amount=%s,Account_Type=%s"
                        withdrawal_details=(Name,PIN,Withdrawal_Amount,Account_Type)
                        res.execute(sql,withdrawal_details)
                        mydb.commit()
                        print("Data Update Successfully")
                    def select():
                        res=mydb.cursor()
                        sql="select Name,PIN,Withdrawal_Amount,Account_Type from withdrawal_details"
                        res.execute(sql)
                        result=res.fetchmany()
                        print(result)
                        print("Data Select Successfully")
                    def delete(Name):
                        res=mydb.cursor()
                        sql="delete from  withdrawal_details where Name=%s"
                        withdrawal_details=(Name,)
                        res.execute(sql,withdrawal_details)
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
                            Name=input("Enter your name:")
                            PIN=input("Enter your pin:")
                            Withdrawal_Amount=input("Enter your Withdrawal Amount:")
                            Account_Type=input("Enter your Account Type:")
                            insert(Name,PIN,Withdrawal_Amount,Account_Type)
                        elif Choice==2:
                            Name=input("Enter your name:")
                            PIN=input("Enter your pin:")
                            Withdrawal_Amount=input("Enter your withdrawal Amount:")
                            Account_Type=input("Enter your Account Type:")
                            update(Name,PIN,Withdrawal_Amount,Account_Type) 
                        elif Choice==3:
                            select()
                        elif Choice==4:
                            Name=input("Enter the Name to delete:")
                            delete(Name)
                        elif Choice==5:
                            quit()
                        else:
                            print("invalid selection.please try again") 
                else:
                    print("Please Re-enter the Details")   
        except:
            print("Please enter the number only")
    elif option==3:
        print("Exit")
    else:
        print("Sorry Invalid Option")
n=int(input("Enter Your Choice in Only Number:"))
data(n)








