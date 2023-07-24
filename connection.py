import mysql.connector as c
con = c.connect(host='localhost',
                user='root',
                passwd='Ayushgarg@25')
cursor = con.cursor()
if con.is_connected():
    print("connect successfully")
else:
    print('fail')

