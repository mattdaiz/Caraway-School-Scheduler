#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#--------------------------------DB_SCRIPT.PY-----------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#
# THIS IS A LIBRARY THAT YOU CAN USE BY ADDING THE LINE
# import DB_Script.py
# TO THE TOP OF YOUR PYTHON FILE, GIVEN IT IS IN THE SAME DIRECTORY.
#
#-------------------------------------------------------------------------------
#FUNCTIONS IN THIS LIBRARY:
#-------------------------------------------------------------------------------
#test() - creates the tables, the DB, and adds the test data to the login table
#         for Raymond's testing
#addToUserTableTestData() - enters test data to the LOGIN table
#initDB() - initializes the database and creates all the main tables
#startDB() - creates the database file and initializes the cursor variable
#closeConnection() - closes the database
#mkEmptyMonthTable(month,year) - makes an empty month table given the name of
#                                the month and the year of the month
#createUserPassTable() - makes an empty "UserPass" table with the columns ID,
#                        username, password, and type
#createUsersTable() - makes an empty table with the columns ID, username,
#                     firstname, lastname, and facilitator-child
#createHoursTable() - creates an empty table with the columns ID, username, 
#                     facilitator child-num, needed-hours-week,
#                     total-hours-lifetime, total-hours-monthly, and 
#                     total-hours-weekly.
#checkValid(username,password) - returns account type iff valid, otherwise false
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# IMPORTS & GLOBAL VAR DECLARATIONS
#-------------------------------------------------------------------------------
import sqlite3 #Type "sqlite3.version" into python shell to ensure 
               #that sqlite3 working (no install necessary)
from datetime import datetime
from cryptography.fernet import Fernet

global DB
global cursor
global sec

# sec = key
sec_file = open("sec.txt","r")
sec = sec_file.readline()
sec = bytes(sec.encode('utf-8'))
f = Fernet(sec) #type: <cryptography.fernet.Fernet object>
sec_file.close()

#-------------------------------------------------------------------------------
# FUNCTIONS
#-------------------------------------------------------------------------------

#String -> String
def encrypt(thisString):
    encryptedString = f.encrypt(bytes(thisString.encode('utf-8')))
    encryptedString = str(encryptedString, 'utf-8')
    return encryptedString #type = <class 'string'>

#String -> String
def decrypt(encryptedString):
    encryptedBytes = bytes(encryptedString.encode('utf-8'))
    decryptedBytes = f.decrypt(encryptedBytes)
    decryptedString = str(decryptedBytes, 'utf-8')
    return decryptedString #type = <class 'string'>


#Purpose: To initialize the db, add some test data so that we can test that the
#         database is working, and then close the connection to the database.
#Parameters: None
#Return Value: None
#Side Effects: Data added to the DB for testing purposes
def test():
    initDB()
    addToUserTableTestData()
    closeConnection()
    return

#Purpose: To execute all of the functions to create the DB and populate it with
#         the empty tables with the appropriate columns
#Parameters: None
#Return Value: 0 (Placeholder int)
#Side effects: DataBase.db is created in dir data
def initDB():
    startDB()
   # months = ['January','February','March','April','May','June','July',\
   #           'August','September','October','November','December']
   # now = datetime.datetime.now()
   # mkEmptyMonthTable(months[(now.month)-1],now.year)
    createUserPassTable()
    createUsersTable()
    createHoursTable()
    return 0

#Purpose: To initialize the SQLite embedded DB
#Parameters: None
#Return Value: 0 (Placeholder int)
def startDB():
    global DB
    global cursor
    #DB = sqlite3.connect(':memory:') #Creates temporary database with RAM
    DB = sqlite3.connect('data/DataBase.db') #Creates file where SQLite DB is stored
    cursor = DB.cursor()
    return 0

#Purpose: To close the connection to the SQLite DB
#Parameters: None
#Return Value: 0 (Placeholder int)
def closeConnection():
    global DB
    global cursor
    DB.close()
    return 0

#-------------------------------------------------------------------------------
# TABLE CREATION FUNCTIONS
#-------------------------------------------------------------------------------

#Purpose: To create a new empty table representing a month in the SQLite DB
#Paramters: month: str value representing month name, e.g. "March"
#           year: int value representing the year of the month being created
#Return Value: 0 (Placeholder int)
def mkEmptyMonthTable(month,year):
    global DB
    global cursor
    with con:
        cursor = con.cursor()    
    leapYear=0 #Set leapYear to 0 (False) by default
    if(month=="February"):
        #Determine if this is a leap year and if so set leapYear to 1 (True)
        if( (year%4==0) and (year%100==0) and (year%400==0) ):
            leapYear=1
    # Case where month being added is 31 days long
    if(month=="January" or month=="March" or month=="May" or month=="July"\
       or month=="August" or month=="October" or month=="December"):
        cur.execute('''CREATE TABLE {tn}(ID INTEGER PRIMARY KEY,1  TEXT 2 TEXT\
        3 TEXT 4 TEXT 5 TEXT 6 TEXT 7 TEXT 8 TEXT 9 TEXT 10 TEXT 11 TEXT 12 TEXT\
        13 TEXT 14 TEXT 15 TEXT 16 TEXT 17 TEXT 18 TEXT 19 TEXT 20 TEXT 21 TEXT\
        22 TEXT 23 TEXT 24 TEXT 25 TEXT 26 TEXT 27 TEXT 28 TEXT 29 TEXT 30 TEXT\
        31 TEXT'''.format(tn=month))
    # Case where month being added is 30 days long
    if(month=="April" or month=="June" or month=="September" or month=="November"):
        cur.execute('''CREATE TABLE {tn}(ID INTEGER PRIMARY KEY, 1 TEXT 2 TEXT\
        3 TEXT 4 TEXT 5 TEXT 6 TEXT 7 TEXT 8 TEXT 9 TEXT 10 TEXT 11 TEXT 12 TEXT\
        13 TEXT 14 TEXT 15 TEXT 16 TEXT 17 TEXT 18 TEXT 19 TEXT 20 TEXT 21 TEXT\
        22 TEXT 23 TEXT 24 TEXT 25 TEXT 26 TEXT 27 TEXT 28 TEXT 29 TEXT 30 TEXT\
        '''.format(tn=month))
    # Pesky February case
    if(month=="February"):
        # If leap year, february has 29 days
        if(leapYear==1):
            cur.execute('''CREATE TABLE {tn}(ID INTEGER PRIMARY KEY, 1 TEXT 2 TEXT\
            3 TEXT 4 TEXT 5 TEXT 6 TEXT 7 TEXT 8 TEXT 9 TEXT 10 TEXT 11 TEXT 12 TEXT\
            13 TEXT 14 TEXT 15 TEXT 16 TEXT 17 TEXT 18 TEXT 19 TEXT 20 TEXT 21 TEXT\
            22 TEXT 23 TEXT 24 TEXT 25 TEXT 26 TEXT 27 TEXT 28 TEXT 29 TEXT'''.format(tn=month))
        # If not a leap year, february has 28 days
        elif(leapYear==0):
            cur.execute('''CREATE TABLE {tn}(ID INTEGER PRIMARY KEY, 1 TEXT 2 TEXT\
            3 TEXT 4 TEXT 5 TEXT 6 TEXT 7 TEXT 8 TEXT 9 TEXT 10 TEXT 11 TEXT 12 TEXT\
            13 TEXT 14 TEXT 15 TEXT 16 TEXT 17 TEXT 18 TEXT 19 TEXT 20 TEXT 21 TEXT\
            22 TEXT 23 TEXT 24 TEXT 25 TEXT 26 TEXT 27 TEXT 28 TEXT'''.format(tn=month))
    DB.commit()
    return 0

#Purpose: To Create the ID/Username/Password/Type relation table (LOGIN)
#Parameters: None
#Return Value: None
def createUserPassTable():
    global DB
    global cursor
    cursor.execute('''CREATE TABLE IF NOT EXISTS login (USERNAME TEXT PRIMARY KEY, \
    PASSWORD TEXT, TYPE TEXT)''')
    DB.commit()
    return 0

#Purpose: To Create the ID/Username/Firstname/LastName/Facilitator-Child table (USERS)
#Parameters: None
#Return Value: 0 (placeholder int)
def createUsersTable():
    global DB
    global cursor
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (ID INTEGER PRIMARY KEY, USERNAME TEXT, \
    FIRSTNAME TEXT, LASTNAME TEXT, FACILITATORCHILD TEXT)''')
    DB.commit()
    return 0

#Purpose: To create the ID/Username/Facilitator/Childnum/Neededhoursweek/Totalhourslifetime
#         Totalhoursmonthly/Totalhoursweekly table (HOURS)
#Parameters: None
#Return Value: 0 (placeholder int)
def createHoursTable():
    global DB
    global cursor
    cursor.execute('''CREATE TABLE IF NOT EXISTS hours (ID INTEGER PRIMARY KEY, USERNAME TEXT\
    FACILITATOR INTEGER, CHILDNUM INTEGER, NEEDEDHOURSWEEK INTEGER,TOTALHOURSLIFETIME \
    INTEGER, TOTALHOURSMONTHLY INTEGER, TOTALHOURSWEEKLY INTEGER)''')
    DB.commit()
    return 0

#-------------------------------------------------------------------------------
# END OF TABLE CREATION FUNCTIONS
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# DATA ENTRY FUNCTIONS
#-------------------------------------------------------------------------------

#Purpose: To insert an entry into the database (DO NOT USE FOR LOGIN TABLE!!!)
#Parameters: TBA
#Return Value: None
def insertField(tableName,colName,colValue):
    global DB
    global cursor
    cursor.execute('''INSERT INTO {tableName}({colName}) VALUES({colValue})'''\
                   .format(tableName=tableName,colName=colName,colValue=colValue))
    DB.commit()
    return 0

#Add username, password and type to login table
def addToUserTable(username, password, typeacct):
    try:
        global DB
        global cursor
        encrypted = encrypt(password)
        cursor.execute('''INSERT INTO login(USERNAME,PASSWORD,TYPE) VALUES (\
        ?,?,?)''',(username,encrypted,typeacct))
        DB.commit()
        return True;
    except sqlite3.IntegrityError:
        print('There was an error inserting into login table.')
    return False;

#Purpose: To insert a ID/Username/Password/Type entry to the LOGIN table
#Parameters:
#Return Value: None
def addToUserTableTestData():
    try:
        global DB
        global cursor
        cursor.execute('''INSERT INTO login(USERNAME,PASSWORD,TYPE) VALUES (\
        'user','gAAAAABaumbaw5LhkKKUwANZ_4J5pK6JddezLiV1wFwlmfqPQU0y7CSMCptvem2g4T2L33YCHWZOrmM8etRV3QlCg_tVgNh12w==','Admin')''')
        DB.commit()
    except sqlite3.IntegrityError:
        print('There was an error inserting into login table.')
    return

#-------------------------------------------------------------------------------
# DATA RETURN FUNCTIONS
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# OTHER FUNCTIONS
#-------------------------------------------------------------------------------

#Purpose:    To query the database and see if the username/password pair matches
#             a pair already in the database, and iff it is, returns the account
#             type, otherwise, returns null.
#Parameters:   username: string representing user entered username
#              password: string representing user entered password
#Return Value: None
def checkValid(username,password):
    global DB
    global cursor
    valid = False # Default is false
    cursor.execute("SELECT * FROM login")
    entries = cursor.fetchall()
    for entry in entries:
        decryptedTableEntry = decrypt(entry[1])
        if(entry[0]==username and decryptedTableEntry==password):
            return (entry[2]) # return account type
    return False


#takes uername and check if in the database
def checkValidUser(username):
    global DB
    global cursor
    valid = False # Default is false
    cursor.execute("SELECT * FROM login")
    entries = cursor.fetchall()
    for entry in entries:
        if(entry[0]==username):
            return True # return account type
    return False

#Purpose: To delete a table in the DB - this function is for reference, as a 
#         specific table name has to be used in order to drop the table.
#Parameters: str tableName - name of table to delete
#Return Value: 0 (Placeholder int)
def delTable(tableName):
    global DB
    global cursor
    cursor.execute('''DROP TABLE {td}'''.format(td=tableName))
    DB.commit()
    return 0


#Purpose: Search through login DB - Searches all accounts if no input is added
def searchAccount(username):
    global DB
    global cursor
    cursor.execute("SELECT * FROM login WHERE username LIKE ?", ('%'+username+'%',))
    entries = cursor.fetchall()
    return entries

#Purpose: Search through login DB - Searches all accounts if no input is added
def searchAccount_distinct(username):
    global DB
    global cursor
    cursor.execute("SELECT DISTINCT username FROM login WHERE NOT username='Admin'")
    entries = cursor.fetchall()
    return entries

#Purpose: Search through login DB - Searches all accounts if no input is added
def searchAccount_FamilyOnly(username):
    global DB
    global cursor
    cursor.execute("SELECT DISTINCT username FROM login WHERE Type='Family'")
    entries = cursor.fetchall()
    return entries

#Purpose: Search through login DB - Searches all accounts if no input is added
def searchAccount_Facilitator(username):
    global DB
    global cursor
    cursor.execute("SELECT * FROM users WHERE username LIKE ?", ('%'+username+'%',))
    entries = cursor.fetchall()
    return entries

#Purpose: Search through login DB - Searches for only faciliator types, no child. return 0 if nothing
def searchAccount_OnlyFacilitator(username):
    global DB
    global cursor
    cursor.execute("SELECT * FROM users WHERE FACILITATORCHILD='Facilitator' and username LIKE ?", ('%'+username+'%',))
    entries = cursor.fetchall()
    if entries:
        return entries
    return 0

#Purpose: Search and return scheduling data base, only return Username, firstname and lastname. return 0 if nothing
def searchSchedule(year,month,day,room,shift):
    global DB
    global cursor
    cursor.execute("SELECT USERNAME, FIRSTNAME, LASTNAME, SLOT FROM room WHERE YEAR = ? and MONTH = ? and DAY = ? and COLOR = ? and SHIFT = ?", (year,month,day,room,shift))
    entries = cursor.fetchone()
    if entries:
        return entries
    return 0

#Purpose: Search and return scheduling data base, only return Username, firstname and lastname. return 0 if nothing
def searchScheduleDonate(year,month,username):
    global DB
    global cursor
    cursor.execute("SELECT FIRSTNAME, LASTNAME, YEAR, MONTH, DAY, SHIFT, COLOR, SLOT FROM room WHERE YEAR = ? and MONTH = ? and USERNAME = ?", (year,month,username))
    entries = cursor.fetchall()
    return entries
   
#returns username of scheduled tiem
def checkUsernameSchedule(year,month,day,room,shift):
    global DB
    global cursor
    cursor.execute("SELECT USERNAME FROM room WHERE YEAR = ? and MONTH = ? and DAY = ? and COLOR = ? and SHIFT = ?", (year,month,day,room,shift))
    entries = cursor.fetchone()
    for entry in entries:
        return (entry) # return account type
    return 0

#Purpose: remove entry from room table
def deleteFromSchedule(year,month,day,room,shift):
    global DB
    global cursor
    cursor.execute("DELETE FROM room WHERE YEAR=? and MONTH=? and DAY=? and COLOR=? and SHIFT=?", (year,month,day,room,shift))
    DB.commit()
    return 0

def donateshift(year,month,day,room,shift,slot,username):
    global DB
    global cursor
    cursor.execute("UPDATE room SET USERNAME=? WHERE YEAR=? and MONTH=? and DAY=? and SHIFT=? and COLOR=? and SLOT=?", (username,year,month,day,shift,room,slot))
    DB.commit()
    return 0

def deleteAccountLogin(username):
    global DB
    global cursor
    cursor.execute("DELETE FROM login WHERE USERNAME=?", (username,))
    DB.commit()
    return 0

def deleteAccountUser(uid):
    global DB
    global cursor
    cursor.execute("DELETE FROM users WHERE ID=?", (uid,))
    DB.commit()
    return 0

def deleteAccountAssociatedUsers(username):
    global DB
    global cursor
    cursor.execute("DELETE FROM users WHERE USERNAME=?", (username,))
    DB.commit()
    return 0

def deleteAccountAssociatedUsersSchedule(username):
    global DB
    global cursor
    cursor.execute("DELETE FROM room WHERE USERNAME=?", (username,))
    DB.commit()
    return 0

#Add username, name and facilitatorchild to users table
def addToUsersTable(username,firstname,lastname,facilitatorchild):
    global DB
    global cursor
    cursor.execute('''INSERT INTO users(USERNAME,FIRSTNAME,LASTNAME,FACILITATORCHILD) VALUES (\
    ?,?,?,?)''',(username,firstname,lastname,facilitatorchild))
    DB.commit()
    return 0

#Add to room table
def addToRoomTable(username,firstname,lastname,year,month,day,shift,color):
    global DB
    global cursor
    cursor.execute('''INSERT INTO room(USERNAME,FIRSTNAME,LASTNAME,YEAR,MONTH,DAY,SHIFT,COLOR) VALUES (\
    ?,?,?,?,?,?,?,?)''',(username,firstname,lastname,year,month,day,shift,color))
    DB.commit()
    return 0

def countChild(username):
    global DB
    global cursor
    cursor.execute('''SELECT count(USERNAME) FROM users WHERE username = ? and FACILITATORCHILD = 'Child' ''', (username,))
    entries = cursor.fetchall()
    if entries:
        return entries[0][0]
    return 0    

def getCurrentHours(username, year, month):
    global DB
    global cursor
    cursor.execute('''SELECT IFNULL(SUM(hours),0)
    FROM 
    (SELECT USERNAME,MONTH,YEAR,
    CASE 
    WHEN SHIFT = 'Lunch' THEN 2
    WHEN SHIFT = 'Morning' THEN 3
    WHEN SHIFT = 'Afternoon' THEN 3 END as hours FROM room) as Q1
    WHERE Q1.USERNAME = ? and Q1.MONTH = ? and Q1.YEAR = ?''', (username, month, year))
    entries = cursor.fetchall()
    if entries:
        return entries[0][0]
    return 0

def editAccountLogin(password, accountType, username):
    global DB
    global cursor
    encryptedpass = encrypt(password)
    cursor.execute('''UPDATE login SET PASSWORD=?, TYPE=? WHERE USERNAME=?''', (encryptedpass, accountType, username))
    DB.commit()
    return 0

def editAccountUser(firstname, lastname, accountType, userid):
    global DB
    global cursor
    cursor.execute('''UPDATE users SET FIRSTNAME=?, LASTNAME=?, FACILITATORCHILD=? WHERE ID=?''', (firstname, lastname, accountType, userid))
    DB.commit()
    return 0

#returns the monthly hours for each room for each month. Lunch hours are double (2 hours) and mornings and afternoons are 3 hour
def getRoomHours(color, month, year):
    global DB
    global cursor
    cursor.execute('''SELECT IFNULL(SUM(hours),0)
    FROM 
    (SELECT MONTH,YEAR,COLOR,
    CASE 
    WHEN SHIFT = 'Lunch' THEN 2
    WHEN SHIFT = 'Morning' THEN 3
    WHEN SHIFT = 'Afternoon' THEN 3 END as hours FROM room) as Q1
    WHERE Q1.COLOR = ? and Q1.MONTH = ? and Q1.YEAR = ?''', (color, month, year))
    entries = cursor.fetchall()
    return entries[0][0] 

# Returns the amount of hours in a given month/year according to the usertype 
def getRoomHoursUser(color, month, year, user):
    global DB
    global cursor
    cursor.execute('''SELECT distinct 2*count(USERNAME) FROM room WHERE room.COLOR = ? and room.MONTH = ? and room.YEAR = ? and room.USERNAME = ?''', (color, month, year, user))
    return cursor.fetchone()[0]

# Uses system time to derive the current year
def getCurrentYear():
    current = datetime.now()
    adjustedYear = current.year 
    return adjustedYear

# returns the upcoming shifts for the next week
def upcomingShifts(username,year,month,day):
    global DB
    global cursor    
    cursor.execute("select SHIFT, COLOR, MONTH, DAY, YEAR from room where USERNAME = ? and MONTH = ? and YEAR = ? and DAY between ? and ?", (username,month,year,day, day+7))
    entries = cursor.fetchall()
    if entries:
        return entries
    return 0    
#-------------------------------------------------------------------------------
# The new functions for scheduling
#-------------------------------------------------------------------------------

def searchScheduleSlotAvailability(year,month,day,room,shift,slot):
    global DB
    global cursor
    cursor.execute("SELECT USERNAME, FIRSTNAME, LASTNAME, SLOT FROM room WHERE YEAR = ? and MONTH = ? and DAY = ? and COLOR = ? and SHIFT = ? and SLOT = ?", (year,month,day,room,shift,slot))
    entries = cursor.fetchall()
    if entries:
        return entries
    return 0

def searchScheduleAllSlots(year,month,day,room,shift):
    global DB
    global cursor
    cursor.execute("SELECT USERNAME, FIRSTNAME, LASTNAME, SLOT FROM room WHERE YEAR = ? and MONTH = ? and DAY = ? and COLOR = ? and SHIFT = ?", (year,month,day,room,shift))
    entries = cursor.fetchall()
    if entries:
        return entries
    return 0

#Add to room table
def addToRoomTableSlot(username,firstname,lastname,year,month,day,shift,color,slot):
    global DB
    global cursor
    cursor.execute('''INSERT INTO room(USERNAME,FIRSTNAME,LASTNAME,YEAR,MONTH,DAY,SHIFT,COLOR,SLOT) VALUES (\
    ?,?,?,?,?,?,?,?,?)''',(username,firstname,lastname,year,month,day,shift,color,slot))
    DB.commit()
    return 0

#Purpose: remove entry from room table
def deleteFromScheduleSlot(year,month,day,room,shift,slot):
    global DB
    global cursor
    cursor.execute("DELETE FROM room WHERE YEAR=? and MONTH=? and DAY=? and COLOR=? and SHIFT=? and SLOT=?", (year,month,day,room,shift,slot))
    DB.commit()
    return 0

#returns username of scheduled tiem
def checkUsernameScheduleSlot(year,month,day,room,shift,slot):
    global DB
    global cursor
    cursor.execute("SELECT USERNAME FROM room WHERE YEAR = ? and MONTH = ? and DAY = ? and COLOR = ? and SHIFT = ? and SLOT = ?", (year,month,day,room,shift,slot))
    entries = cursor.fetchone()
    for entry in entries:
        return (entry) # return account type
    return 0