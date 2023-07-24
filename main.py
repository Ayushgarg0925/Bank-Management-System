import mysql.connector as c

con = c.connect(host='localhost',
                user='root',
                passwd='Ayushgarg@25',
                database='bms')
cursor = con.cursor()


def re():
    """
    this is user define function  (for show account information)
    """
    for row in records:
        print("    account_holder:- ", row[0])
        print("    address:- ", row[1])
        print("    mobile_no:- ", row[2])
        print("    email_id:- ", row[3])
        print("    gender:- ", row[4])
        print("    document:- ", row[5])
        print("    account_id:- ", row[6])
        print("    generate_pin:- ", row[7])
        print("\n")


def rc():
    """
    this is user define function (for deposit amount)
   """
    for row in records:
        print("date: ", row[0])
        print("account_id: ", row[1])
        print("amount: ", row[2])
        print("\n")


while True:

    print('''
*************************************
    WELCOME TO STATE BANK OF INDIA 
*************************************''')
    print('''
    Press. 1 Create New Account
    Press. 2 Already Registered Account 
    press. 3 Exit''')
    i = int(input("    Enter your choice --> "))
    print('*************************************')

    if i == 1:
        print("    Create Account")
        account_holder = input("Enter your name --> ")
        address = input("enter your address --> ")
        mobile_no = int(input("enter your mobile no --> "))
        email_id = input("enter your email id --> ")
        gender = input("Enter your gender --> ")
        print("1.Aadhar 2.PAN 3.Driving Licence")
        document = int(input("Enter your choice "))
        if document == 1:
            Aadhar = int(input("Enter your aadhar number --> "))
        elif document == 2:
            pan = int(input("Enter your pan number --> "))
        else:
            driving_licence = int(input("Enter your driving licence --> "))

        account_id = input("enter your account id --> ")
        generate_pin = int(input("Generate pin --> "))

        query = "insert into ca value('{}','{}','{}','{}','{}',{},{},{})".format(account_holder, address, mobile_no,
                                                                                 email_id, gender, document, account_id,
                                                                                 generate_pin)
        cursor.execute(query)
        con.commit()
        cursor.close()
        con.close()
        print("***** data enter successfully *****")

    elif i == 2:
        print('''
    Press. 1 Account Information
    Press. 2 Cash Deposit
    press. 3 Cash Withdrew
    Press. 4 Balance enquiry
    Press. 5 Update Information
    Press. 6 Close Account
    Press. 7 Exit 
*************************************    ''')
        i = int(input("        Press  "))
        if i == 1:
            account_id_search = int(input("Enter your account_id --> "))
            cursor = con.cursor()
            cursor.execute(
                "select * from ca where account_id='{}'".format(account_id_search))
            records = cursor.fetchall()
            print(len(records))
            re()
            cursor.close()

        elif i == 2:
            print("cash deposit")

            date1 = input("Enter today date")
            account_id_deposit = int(input("Enter your account_id"))
            amount = int(input("Enter amount"))

            query = "insert into dp value('{}',{},{})".format(date1, account_id_deposit, amount)
            cursor.execute(query)
            con.commit()
            print("cash deposit successfully")

        elif i == 3:
            print("Cash Withdrew")

            date1 = input("Enter today date")
            account_id_withdrew = int(input("Enter your account_id"))
            amount = int(input("Enter amount"))

            query = "insert into dp value('{}',{},{})".format(date1, account_id_withdrew, amount)
            cursor.execute(query)
            con.commit()
            print("Cash Withdrew Successfully")

        elif i == 4:
            print("Balance enquiry")
            account_id_search = int(input("Enter your account_id --> "))
            cursor = con.cursor()
            cursor.execute(
                "select * from dp where account_id='{}'".format(account_id_search))
            records = cursor.fetchall()

            print(len(records))
            rc()
            cursor.close()

        elif i == 5:
            account_id_search = int(input("Enter your account_id --> "))
            cursor = con.cursor()
            cursor.execute(
                "select * from ca where account_id='{}'".format(account_id_search))
            records = cursor.fetchall()
            print(len(records))
            re()
            print('*****Update information*****')
            mobile_no = int(input('enter your mobile no --> '))
            email_id = input('enter your email --> ')
            # salary=int(input('enter your salary'))
            query = "update ca set mobile_no= {}, email_id = '{}' where account_id={}".format(mobile_no, email_id,
                                                                                              account_id_search)
            cursor.execute(query)
            con.commit()
            print("data update successfully")

        elif i == 6:
            print('Close Account')
            account_holder = (input("enter name"))
            generate_pin = int(input("enter pin"))
            query = "delete from ca where account_holder= '{}' AND generate_pin={} ".format(account_holder,
                                                                                            generate_pin)
            cursor.execute(query)
            con.commit()
            print("data delete successfully")
        elif i == 7:
            print('exit')
            break

        else:
            print("Please Press Correct Number")

    elif i == 3:
        print("        For Exit")
        break
    else:
        print("Please Press Correct Number")
