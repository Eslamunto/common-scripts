import mysql.connector
from mysql.connector import errorcode

print("start program...")

# update USERNAME, PASSWORD, HOSTNAME and DATABASE NAME

try:
    cnx = mysql.connector.connect(user='USERNAME', password='PASSWORD',
                                  host='HOSTNAME',
                                  database='DATABASENAME')
    cursor = cnx.cursor()


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

# UPDATE CSV FILE NAME AND DESTINATION
lines = [line.rstrip('\n') for line in open('CSV FILE NAME')]  # init connection to mysql
for line in lines:
    print("starting to enter a new officer...")
    x = line.split(",")
    # Just an example from a non-real table. Should update tablename and fields to be filled
    add_officer = ("INSERT INTO TABLE_NAME "
                    "(military_number, name, rank, sector) "
                    "VALUES (%s, %s, %s, %s)")

    data_officer = (x[4], x[2], x[3], x[1])

    # Insert new employee
    cursor.execute(add_officer, data_officer)

    # Make sure data is committed to the database
    cnx.commit()
    print("new officer added successfully...")

cursor.close()
cnx.close()

print("program ended...")
