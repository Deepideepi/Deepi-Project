
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="19Uma43*",
    database="covid_db"
) 
print("*************CORONA RECOVERY CENTER**********************")
symptom=["1-fever","2-cough","3-bodypain"] 
for i in symptom: 
    print(i) 
def data(symptoms): 
    if symptoms==1: 
        print("please take the corona test") 
        corona_test=input("Enter your corona test report Positive or Negative:").lower().strip() 
        if corona_test=="positive": 
            print("yes you are affect in corona") 
            name=input("Enter Your Name:")
            district=input("Enter Your District:")
            phone=int(input("Enter Your Phone Number:"))
            address=input("Enter Your Address:")
            print("1 dose")
            print("2 dose")
            print("Booster dose")
            vaccine=input("Enter Your Vaccination Status in Above List:").lower().strip()
            print("please vaccinate the booster dose") 
            print("please donot spread the disease")
            print("please admit the hospital") 
            hospital=input("You are admit the hospital OK or Not:").lower().strip()
            if hospital=="ok":
                print("Check the levels of oxygen in your blood")
                print("Give you a CT scan")
                print("Listen to your lungs") 
                print("Donot share anyone your things") 
                print("******PLEASE TAKE THE ANOTHER CORONA TEST*******")
                result=input("please enter your result Positive or Negative:")
                if result=="positive": 
                    print("please admit extra 15days in hospital")
                    Name=name
                    District=district
                    Phone_Number=phone
                    Address=address
                    Vaccine_Status=vaccine
                    val=(name,district,phone,address,vaccine)
                    sql="insert into patient_details(Name,District,Phone_Number,Address,Vaccine_Status) values (%s,%s,%s,%s,%s)"
                    mycursor = mydb.cursor()
                    mycursor.execute(sql,val)
                    mydb.commit() 
                    def insert(Name,District,Phone_Number,Address,Vaccine_Status):
                        res=mydb.cursor()
                        sql="insert into patient_details(Name,District,Phone_Number,Address,Vaccine_Status) values (%s,%s,%s,%s,%s)"
                        patient_details=(Name,District,Phone_Number,Address,Vaccine_Status)
                        res.execute(sql,patient_details)
                        mydb.commit()
                        print("Data Insert Successfully")
                    def update(Name,District,Phone_Number,Address,Vaccine_Status):
                        res=mydb.cursor()
                        sql="update  patient_details set Name=%s,District=%s,Phone_Number=%s,Address=%s,Vaccine_Status=%s"
                        patient_details=(Name,District,Phone_Number,Address,Vaccine_Status)
                        res.execute(sql,patient_details)
                        mydb.commit()
                        print("Data Update Successfully")
                    def select():
                        res=mydb.cursor()
                        sql="select Name,District,Phone_Number,Address,Vaccine_Status from patient_details"
                        res.execute(sql)
                        result=res.fetchmany()
                        print(result)
                        print("Data Selected Successfully")
                    def delete(Name):
                        res=mydb.cursor()
                        sql="delete from  patient_details where Name=%s"
                        patient_details=(Name,)
                        res.execute(sql,patient_details)
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
                            Name=input("Enter your Name:")
                            District=input("Enter your District:")
                            Phone_Number=input("Enter your Phone Number:")
                            Address=input("Enter your Address:")
                            Vaccine_Status=input("Enter Your Vacccine Status:")
                            insert(Name,District,Phone_Number,Address,Vaccine_Status)
                        elif Choice==2:
                            Name=input("Enter your Name:")
                            District=input("Enter your District:")
                            Phone_Number=input("Enter your Phone Number:")
                            Address=input("Enter your Address:")
                            Vaccine_Status=input("Enter Your Vacccine Status:")
                            update(Name,District,Phone_Number,Address,Vaccine_Status)
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
                    print("you are cured")
                    print("please follow the corona rules")
                    Name=name
                    District=district
                    Phone_Number=phone
                    Address=address
                    Vaccine_Status=vaccine
                    val=(name,district,phone,address,vaccine)
                    sql="insert into patient_details(Name,District,Phone_Number,Address,Vaccine_Status) values (%s,%s,%s,%s,%s)"
                    mycursor = mydb.cursor()
                    mycursor.execute(sql,val)
                    mydb.commit() 
                    def insert(Name,District,Phone_Number,Address,Vaccine_Status):
                        res=mydb.cursor()
                        sql="insert into patient_details(Name,District,Phone_Number,Address,Vaccine_Status) values (%s,%s,%s,%s,%s)"
                        patient_details=(Name,District,Phone_Number,Address,Vaccine_Status)
                        res.execute(sql,patient_details)
                        mydb.commit()
                        print("Data Insert Successfully")
                    def update(Name,District,Phone_Number,Address,Vaccine_Status):
                        res=mydb.cursor()
                        sql="update  patient_details set Name=%s,District=%s,Phone_Number=%s,Address=%s,Vaccine_Status=%s"
                        patient_details=(Name,District,Phone_Number,Address,Vaccine_Status)
                        res.execute(sql,patient_details)
                        mydb.commit()
                        print("Data Update Successfully")
                    def select():
                        res=mydb.cursor()
                        sql="select Name,District,Phone_Number,Address,Vaccine_Status from patient_details"
                        res.execute(sql)
                        result=res.fetchmany()
                        print(result)
                        print("Data Selected Successfully")
                    def delete(Name):
                        res=mydb.cursor()
                        sql="delete from  patient_details where Name=%s"
                        patient_details=(Name,)
                        res.execute(sql,patient_details)
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
                            Name=input("Enter your Name:")
                            District=input("Enter your District:")
                            Phone_Number=input("Enter your Phone Number:")
                            Address=input("Enter your Address:")
                            Vaccine_Status=input("Enter Your Vacccine Status:")
                            insert(Name,District,Phone_Number,Address,Vaccine_Status)
                        elif Choice==2:
                            Name=input("Enter your Name:")
                            District=input("Enter your District:")
                            Phone_Number=input("Enter your Phone Number:")
                            Address=input("Enter your Address:")
                            Vaccine_Status=input("Enter Your Vacccine Status:")
                            update(Name,District,Phone_Number,Address,Vaccine_Status)
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
                print("please admit the hospital ")
        else:
            print("its normal")
    elif symptoms==2:
        print("Its normal symptom")
        print("please follow the corona rules")
        print("please vaccinate the vaccination") 
    elif symptoms==3: 
        print("Its normal symptom")
        print("please follow the corona rules")
        print("please vaccinate the vaccination") 
    else: 
        print("No problem")
patient=int(input("Enter your symptoms:")) 
data(patient)      


