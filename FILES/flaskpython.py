from flask import Flask,flash, render_template, request, redirect, url_for

from datetime import datetime

#Import DB_Script.py in order to use its functions to interface with the 
#Database.DB SQLlite file
import DB_Script as DB

# app = Flask(__name__)
# @app.route("/")

# TO INSTALL FLASK:
# $ pip install Flask

# IF YOU DON'T HAVE PIP, run the file distribute_setup in this folder to install
# easy_install on your system, then cd into C:/ with command prompt and execute
# easy_install pip. Then execute the command pip install Flask and you're good 
# to go!

# Flask example call to run on localhost:
# $ FLASK_APP=hello.py flask run
# * Running on http://localhost:5000/

app = Flask(__name__)

#for flashing message
app.secret_key = 'some_secret'

#global vars declaration
global login
global adjustedYear

#very first page that loads
@app.route('/')
def index():
    return redirect(url_for("login"))

# this is for when you are at a page, and press logout
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

# Main page. Will communicate with Login page and get Username and Password. Depending on type will load page.
@app.route('/main', methods=['GET', 'POST'])
def mainpage():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        global login
        login = username
        typeacct = DB.checkValid(username,password)
        if typeacct == "Admin":
            return render_template('adminpage.html')  # edited
        elif typeacct == "Board Member":
            return render_template('boardpage.html')
        elif typeacct == "Teacher":
            return render_template('teacherpage.html')
        elif typeacct == "Family":
            return redirect(url_for('familyhome'))
        elif typeacct == False:
            flash('Incorrect user or password')
            return redirect(url_for("login"))

# Board schedule view
@app.route('/board-schedule-view', methods=['GET', 'POST'])
def boardscheduleview():
    if request.method == 'POST':
        global login
        #grab the year, month, day, room
        year = request.form.get('Year')
        month = request.form.get('Month')
        day = request.form.get('Day')
        room = request.form.get('Room')

        #check for any shifts already scheduled on those above variables
        morning = DB.searchScheduleAllSlots(year,month,day,room,"Morning")
        morning_list = ["Available", "Available", "Available"] 
        if (morning):
            for person in morning:
                morning_list[person[3]] = (person[1] + " " + person[2])
        
        lunch = DB.searchScheduleAllSlots(year,month,day,room,"Lunch")
        lunch_list = ["Available", "Available", "Available"] 
        if (lunch):
            for person in lunch:
                lunch_list[person[3]] = (person[1] + " " + person[2])
        
        afternoon = DB.searchScheduleAllSlots(year,month,day,room,"Afternoon")
        afternoon_list = ["Available", "Available", "Available"] 
        if (afternoon):
            for person in afternoon:
                afternoon_list[person[3]] = (person[1] + " " + person[2])
        
        #Displays page after Add/Remove button clicked
        print("Rendered")
        return render_template('board-schedule-view.html', year=year, month=month, day=day, room=room, username=login,
                               actualMorning=morning_list, 
                               actualLunch=lunch_list, 
                               actualAfternoon=afternoon_list)

# Teacher schedule view
@app.route('/teacher-schedule-view', methods=['GET', 'POST'])
def teacherscheduleview():
    if request.method == 'POST':
        global login
        #grab the year, month, day, room
        year = request.form.get('Year')
        month = request.form.get('Month')
        day = request.form.get('Day')
        room = request.form.get('Room')

        #check for any shifts already scheduled on those above variables
        morning = DB.searchScheduleAllSlots(year,month,day,room,"Morning")
        morning_list = ["Available", "Available", "Available"] 
        if (morning):
            for person in morning:
                morning_list[person[3]] = (person[1] + " " + person[2])
        
        lunch = DB.searchScheduleAllSlots(year,month,day,room,"Lunch")
        lunch_list = ["Available", "Available", "Available"] 
        if (lunch):
            for person in lunch:
                lunch_list[person[3]] = (person[1] + " " + person[2])
        
        afternoon = DB.searchScheduleAllSlots(year,month,day,room,"Afternoon")
        afternoon_list = ["Available", "Available", "Available"] 
        if (afternoon):
            for person in afternoon:
                afternoon_list[person[3]] = (person[1] + " " + person[2])
        
        #Displays page after Add/Remove button clicked
        print("Rendered")
        return render_template('teacher-schedule-view.html', year=year, month=month, day=day, room=room, username=login,
                               actualMorning=morning_list, 
                               actualLunch=lunch_list, 
                               actualAfternoon=afternoon_list)
    

# Family schedule add remove
@app.route('/family-schedule-add', methods=['GET', 'POST'])
def familyscheduleadd():
    if request.method == 'POST':
        global login
        searchlogin = login
        #grab the year, month, day, room
        year = request.form.get('Year')
        month = request.form.get('Month')
        day = request.form.get('Day')
        room = request.form.get('Room')
        
        #---------------------------------------Morning-------------------------------------------------------------------
        #add morning shift, need username field and firstname,lastname field typed in
        if request.form.get('button') == 'addmorning_shift0':
            if request.form["button"] == "addmorning_shift0" and request.form["username_fill"]:
                print("added")
                searchlogin = request.form['username_fill']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                shift = "Morning"
                test = DB.searchScheduleSlotAvailability(year,month,day,room,shift,0)
                if test == 0:
                    bool = DB.addToRoomTableSlot(searchlogin,firstname,lastname,year,month,day,shift,room,0)
                else:
                    flash('Shift not available')
            else:
                if request.form["morningshift0"] != "Available":
                    flash('Shift not available')
                elif request.form["morningshift0"] == "Available":
                    flash('Facilitator Input Required')
        #remove morning shift
        if request.form.get('button') == 'removemorning_shift0':
            if request.form["button"] == "removemorning_shift0" and request.form["morningshift0"] != "Available":
                test = DB.checkUsernameScheduleSlot(year,month,day,room,"Morning",0)
                if test == login:
                    DB.deleteFromScheduleSlot(year,month,day,room,"Morning",0)
                else:
                    flash('Not Authorized to Delete')                
            else:
                flash('No Facilitator Assigned')
        
        #add morning shift, need username field and firstname,lastname field typed in
        if request.form.get('button') == 'addmorning_shift1':
            if request.form["button"] == "addmorning_shift1" and request.form["username_fill"]:
                print("added")
                searchlogin = request.form['username_fill']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                shift = "Morning"
                test = DB.searchScheduleSlotAvailability(year,month,day,room,shift,1)
                if test == 0:
                    bool = DB.addToRoomTableSlot(searchlogin,firstname,lastname,year,month,day,shift,room,1)
                else:
                    flash('Shift not available')
            else:
                if request.form["morningshift1"] != "Available":
                    flash('Shift not available')
                elif request.form["morningshift1"] == "Available":
                    flash('Facilitator Input Required')
        #remove morning shift
        if request.form.get('button') == 'removemorning_shift1':
            if request.form["button"] == "removemorning_shift1" and request.form["morningshift1"] != "Available":
                test = DB.checkUsernameScheduleSlot(year,month,day,room,"Morning",1)
                if test == login:
                    DB.deleteFromScheduleSlot(year,month,day,room,"Morning",1)
                else:
                    flash('Not Authorized to Delete')      
            else:
                flash('No Facilitator Assigned')      
                
        #add morning shift, need username field and firstname,lastname field typed in
        if request.form.get('button') == 'addmorning_shift2':
            if request.form["button"] == "addmorning_shift2" and request.form["username_fill"]:
                print("added")
                searchlogin = request.form['username_fill']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                shift = "Morning"
                test = DB.searchScheduleSlotAvailability(year,month,day,room,shift,2)
                if test == 0:
                    bool = DB.addToRoomTableSlot(searchlogin,firstname,lastname,year,month,day,shift,room,2)
                else:
                    flash('Shift not available')
            else:
                if request.form["morningshift2"] != "Available":
                    flash('Shift not available')
                elif request.form["morningshift2"] == "Available":
                    flash('Facilitator Input Required')
        #remove morning shift
        if request.form.get('button') == 'removemorning_shift2':
            if request.form["button"] == "removemorning_shift2" and request.form["morningshift2"] != "Available":
                test = DB.checkUsernameScheduleSlot(year,month,day,room,"Morning",2)
                if test == login:
                    DB.deleteFromScheduleSlot(year,month,day,room,"Morning",2)
                else:
                    flash('Not Authorized to Delete')      
            else:
                flash('No Facilitator Assigned')          
                
        #------------------------------------------Lunch---------------------------------------------------------
        #add lunch shift
        if request.form.get('button') == 'addlunch_shift0':
            if request.form["button"] == "addlunch_shift0" and request.form["username_fill"]:
                searchlogin = request.form['username_fill']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                shift = "Lunch"
                test = DB.searchScheduleSlotAvailability(year,month,day,room,shift,0)
                if test == 0:
                    bool = DB.addToRoomTableSlot(searchlogin,firstname,lastname,year,month,day,shift,room,0)
                else:
                    flash('Shift not available')
            else:
                if request.form["lunchshift0"] != "Available":
                    flash('Shift not available')
                elif request.form["lunchshift0"] == "Available":
                    flash('Facilitator Input Required')                
        #remove lunch shift
        if request.form.get('button') == 'removelunch_shift0':
            if request.form["button"] == "removelunch_shift0" and request.form["lunchshift0"] != "Available":
                test = DB.checkUsernameScheduleSlot(year,month,day,room,"Lunch",0)
                if test == login:
                    DB.deleteFromScheduleSlot(year,month,day,room,"Lunch",0)
                else:
                    flash('Not Authorized to Delete')      
            else:
                flash('No Facilitator Assigned')
                
        #add lunch shift
        if request.form.get('button') == 'addlunch_shift1':
            if request.form["button"] == "addlunch_shift1" and request.form["username_fill"]:
                searchlogin = request.form['username_fill']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                shift = "Lunch"
                test = DB.searchScheduleSlotAvailability(year,month,day,room,shift,1)
                if test == 0:
                    bool = DB.addToRoomTableSlot(searchlogin,firstname,lastname,year,month,day,shift,room,1)
                else:
                    flash('Shift not available')
            else:
                if request.form["lunchshift1"] != "Available":
                    flash('Shift not available')
                elif request.form["lunchshift1"] == "Available":
                    flash('Facilitator Input Required')                
        #remove lunch shift
        if request.form.get('button') == 'removelunch_shift1':
            if request.form["button"] == "removelunch_shift1" and request.form["lunchshift1"] != "Available":
                test = DB.checkUsernameScheduleSlot(year,month,day,room,"Lunch",1)
                if test == login:
                    DB.deleteFromScheduleSlot(year,month,day,room,"Lunch",1)
                else:
                    flash('Not Authorized to Delete')    
            else:
                flash('No Facilitator Assigned')    
                    
        #add lunch shift
        if request.form.get('button') == 'addlunch_shift2':
            if request.form["button"] == "addlunch_shift2" and request.form["username_fill"]:
                searchlogin = request.form['username_fill']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                shift = "Lunch"
                test = DB.searchScheduleSlotAvailability(year,month,day,room,shift,2)
                if test == 0:
                    bool = DB.addToRoomTableSlot(searchlogin,firstname,lastname,year,month,day,shift,room,2)
                else:
                    flash('Shift not available')
            else:
                if request.form["lunchshift2"] != "Available":
                    flash('Shift not available')
                elif request.form["lunchshift2"] == "Available":
                    flash('Facilitator Input Required')                
        #remove lunch shift
        if request.form.get('button') == 'removelunch_shift2':
            if request.form["button"] == "removelunch_shift2" and request.form["lunchshift2"] != "Available":
                test = DB.checkUsernameScheduleSlot(year,month,day,room,"Lunch",2)
                if test == login:
                    DB.deleteFromScheduleSlot(year,month,day,room,"Lunch",2)
                else:
                    flash('Not Authorized to Delete')    
            else:
                flash('No Facilitator Assigned')            
                
        #------------------------------------------Afternoon---------------------------------------------------------        
        #add afternoon shift
        if request.form.get('button') == 'addafternoon_shift0':
            if request.form["button"] == "addafternoon_shift0" and request.form["username_fill"]:
                searchlogin = request.form['username_fill']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                shift = "Afternoon"
                test = DB.searchScheduleSlotAvailability(year,month,day,room,shift,0)
                if test == 0:
                    bool = DB.addToRoomTableSlot(searchlogin,firstname,lastname,year,month,day,shift,room,0)
                else:
                    flash('Shift not available')
            else:
                if request.form["afternoonshift0"] != "Available":
                    flash('Shift not available')
                elif request.form["afternoonshift0"] == "Available":
                    flash('Facilitator Input Required')
        #remove afternoon shift
        if request.form.get('button') == 'removeafternoon_shift0':
            if request.form["button"] == "removeafternoon_shift0" and request.form["afternoonshift0"] != "Available":
                test = DB.checkUsernameScheduleSlot(year,month,day,room,"Afternoon",0)
                if test == login:
                    DB.deleteFromScheduleSlot(year,month,day,room,"Afternoon",0)
                else:
                    flash('Not Authorized to Delete')    
            else:
                flash('No Facilitator Assigned')     
                
        #add afternoon shift
        if request.form.get('button') == 'addafternoon_shift1':
            if request.form["button"] == "addafternoon_shift1" and request.form["username_fill"]:
                searchlogin = request.form['username_fill']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                shift = "Afternoon"
                test = DB.searchScheduleSlotAvailability(year,month,day,room,shift,1)
                if test == 0:
                    bool = DB.addToRoomTableSlot(searchlogin,firstname,lastname,year,month,day,shift,room,1)
                else:
                    flash('Shift not available')
            else:
                if request.form["afternoonshift1"] != "Available":
                    flash('Shift not available')
                elif request.form["afternoonshift1"] == "Available":
                    flash('Facilitator Input Required')
        #remove afternoon shift
        if request.form.get('button') == 'removeafternoon_shift1':
            if request.form["button"] == "removeafternoon_shift1" and request.form["afternoonshift1"] != "Available":
                test = DB.checkUsernameScheduleSlot(year,month,day,room,"Afternoon",1)
                if test == login:
                    DB.deleteFromScheduleSlot(year,month,day,room,"Afternoon",1)
                else:
                    flash('Not Authorized to Delete')
            else:
                flash('No Facilitator Assigned')  
                        
        #add afternoon shift
        if request.form.get('button') == 'addafternoon_shift2':
            if request.form["button"] == "addafternoon_shift2" and request.form["username_fill"]:
                searchlogin = request.form['username_fill']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                shift = "Afternoon"
                test = DB.searchScheduleSlotAvailability(year,month,day,room,shift,2)
                if test == 0:
                    bool = DB.addToRoomTableSlot(searchlogin,firstname,lastname,year,month,day,shift,room,2)
                else:
                    flash('Shift not available')
            else:
                if request.form["afternoonshift2"] != "Available":
                    flash('Shift not available')
                elif request.form["afternoonshift2"] == "Available":
                    flash('Facilitator Input Required')
        #remove afternoon shift
        if request.form.get('button') == 'removeafternoon_shift2':
            if request.form["button"] == "removeafternoon_shift2" and request.form["afternoonshift2"] != "Available":
                test = DB.checkUsernameScheduleSlot(year,month,day,room,"Afternoon",2)
                if test == login:
                    DB.deleteFromScheduleSlot(year,month,day,room,"Afternoon",2)
                else:
                    flash('Not Authorized to Delete')
            else:
                flash('No Facilitator Assigned')                          

        #check for any shifts already scheduled on those above variables
        morning = DB.searchScheduleAllSlots(year,month,day,room,"Morning")
        morning_list = ["Available", "Available", "Available"] 
        if (morning):
            for person in morning:
                morning_list[person[3]] = (person[1] + " " + person[2])
        
        lunch = DB.searchScheduleAllSlots(year,month,day,room,"Lunch")
        lunch_list = ["Available", "Available", "Available"] 
        if (lunch):
            for person in lunch:
                lunch_list[person[3]] = (person[1] + " " + person[2])
        
        afternoon = DB.searchScheduleAllSlots(year,month,day,room,"Afternoon")
        afternoon_list = ["Available", "Available", "Available"] 
        if (afternoon):
            for person in afternoon:
                afternoon_list[person[3]] = (person[1] + " " + person[2])
        
        #Displays page after Add/Remove button clicked
        acc = DB.searchAccount_OnlyFacilitator(login)
        print("Rendered")
        return render_template('family-schedule-addremove.html', year=year, month=month, day=day, room=room, username=login, accounts=acc,
                               actualMorning=morning_list, 
                               actualLunch=lunch_list, 
                               actualAfternoon=afternoon_list)

# Admin schedule add remove
@app.route('/admin-schedule-add', methods=['GET', 'POST'])
def adminscheduleadd():
    if request.method == 'POST':
        global login
        #grab the year, month, day, room
        year = request.form.get('Year')
        month = request.form.get('Month')
        day = request.form.get('Day')
        room = request.form.get('Room')
        
        #---------------------------------------Morning-------------------------------------------------------------------
        #add morning shift, need username field and firstname,lastname field typed in
        if request.form.get('button') == 'addmorning_shift0':
            if request.form["button"] == "addmorning_shift0" and request.form["username_fill"]:
                print("added")
                searchlogin = request.form['username_fill']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                shift = "Morning"
                test = DB.searchScheduleSlotAvailability(year,month,day,room,shift,0)
                if test == 0:
                    bool = DB.addToRoomTableSlot(searchlogin,firstname,lastname,year,month,day,shift,room,0)
                else:
                    flash('Shift not available')
            else:
                if request.form["morningshift0"] != "Available":
                    flash('Shift not available')
                elif request.form["morningshift0"] == "Available":
                    flash('Facilitator Input Required')
        #remove morning shift
        if request.form.get('button') == 'removemorning_shift0':
            if request.form["button"] == "removemorning_shift0" and request.form["morningshift0"] != "Available":
                DB.deleteFromScheduleSlot(year,month,day,room,"Morning",0)
            else:
                flash('No Facilitator Assigned')
        
        #add morning shift, need username field and firstname,lastname field typed in
        if request.form.get('button') == 'addmorning_shift1':
            if request.form["button"] == "addmorning_shift1" and request.form["username_fill"]:
                print("added")
                searchlogin = request.form['username_fill']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                shift = "Morning"
                test = DB.searchScheduleSlotAvailability(year,month,day,room,shift,1)
                if test == 0:
                    bool = DB.addToRoomTableSlot(searchlogin,firstname,lastname,year,month,day,shift,room,1)
                else:
                    flash('Shift not available')
            else:
                if request.form["morningshift1"] != "Available":
                    flash('Shift not available')
                elif request.form["morningshift1"] == "Available":
                    flash('Facilitator Input Required')
        #remove morning shift
        if request.form.get('button') == 'removemorning_shift1':
            if request.form["button"] == "removemorning_shift1" and request.form["morningshift1"] != "Available":
                DB.deleteFromScheduleSlot(year,month,day,room,"Morning",1)
            else:
                flash('No Facilitator Assigned')      
                
        #add morning shift, need username field and firstname,lastname field typed in
        if request.form.get('button') == 'addmorning_shift2':
            if request.form["button"] == "addmorning_shift2" and request.form["username_fill"]:
                print("added")
                searchlogin = request.form['username_fill']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                shift = "Morning"
                test = DB.searchScheduleSlotAvailability(year,month,day,room,shift,2)
                if test == 0:
                    bool = DB.addToRoomTableSlot(searchlogin,firstname,lastname,year,month,day,shift,room,2)
                else:
                    flash('Shift not available')
            else:
                if request.form["morningshift2"] != "Available":
                    flash('Shift not available')
                elif request.form["morningshift2"] == "Available":
                    flash('Facilitator Input Required')
        #remove morning shift
        if request.form.get('button') == 'removemorning_shift2':
            if request.form["button"] == "removemorning_shift2" and request.form["morningshift2"] != "Available":
                DB.deleteFromScheduleSlot(year,month,day,room,"Morning",2)
            else:
                flash('No Facilitator Assigned')          
                
        #------------------------------------------Lunch---------------------------------------------------------
        #add lunch shift
        if request.form.get('button') == 'addlunch_shift0':
            if request.form["button"] == "addlunch_shift0" and request.form["username_fill"]:
                searchlogin = request.form['username_fill']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                shift = "Lunch"
                test = DB.searchScheduleSlotAvailability(year,month,day,room,shift,0)
                if test == 0:
                    bool = DB.addToRoomTableSlot(searchlogin,firstname,lastname,year,month,day,shift,room,0)
                else:
                    flash('Shift not available')
            else:
                if request.form["lunchshift0"] != "Available":
                    flash('Shift not available')
                elif request.form["lunchshift0"] == "Available":
                    flash('Facilitator Input Required')                
        #remove lunch shift
        if request.form.get('button') == 'removelunch_shift0':
            if request.form["button"] == "removelunch_shift0" and request.form["lunchshift0"] != "Available":
                DB.deleteFromScheduleSlot(year,month,day,room,"Lunch",0)
            else:
                flash('No Facilitator Assigned')
                
        #add lunch shift
        if request.form.get('button') == 'addlunch_shift1':
            if request.form["button"] == "addlunch_shift1" and request.form["username_fill"]:
                searchlogin = request.form['username_fill']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                shift = "Lunch"
                test = DB.searchScheduleSlotAvailability(year,month,day,room,shift,1)
                if test == 0:
                    bool = DB.addToRoomTableSlot(searchlogin,firstname,lastname,year,month,day,shift,room,1)
                else:
                    flash('Shift not available')
            else:
                if request.form["lunchshift1"] != "Available":
                    flash('Shift not available')
                elif request.form["lunchshift1"] == "Available":
                    flash('Facilitator Input Required')                
        #remove lunch shift
        if request.form.get('button') == 'removelunch_shift1':
            if request.form["button"] == "removelunch_shift1" and request.form["lunchshift1"] != "Available":
                DB.deleteFromScheduleSlot(year,month,day,room,"Lunch",1)
            else:
                flash('No Facilitator Assigned')    
                    
        #add lunch shift
        if request.form.get('button') == 'addlunch_shift2':
            if request.form["button"] == "addlunch_shift2" and request.form["username_fill"]:
                searchlogin = request.form['username_fill']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                shift = "Lunch"
                test = DB.searchScheduleSlotAvailability(year,month,day,room,shift,2)
                if test == 0:
                    bool = DB.addToRoomTableSlot(searchlogin,firstname,lastname,year,month,day,shift,room,2)
                else:
                    flash('Shift not available')
            else:
                if request.form["lunchshift2"] != "Available":
                    flash('Shift not available')
                elif request.form["lunchshift2"] == "Available":
                    flash('Facilitator Input Required')                
        #remove lunch shift
        if request.form.get('button') == 'removelunch_shift2':
            if request.form["button"] == "removelunch_shift2" and request.form["lunchshift2"] != "Available":
                DB.deleteFromScheduleSlot(year,month,day,room,"Lunch",2)
            else:
                flash('No Facilitator Assigned')            
                
        #------------------------------------------Afternoon---------------------------------------------------------        
        #add afternoon shift
        if request.form.get('button') == 'addafternoon_shift0':
            if request.form["button"] == "addafternoon_shift0" and request.form["username_fill"]:
                searchlogin = request.form['username_fill']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                shift = "Afternoon"
                test = DB.searchScheduleSlotAvailability(year,month,day,room,shift,0)
                if test == 0:
                    bool = DB.addToRoomTableSlot(searchlogin,firstname,lastname,year,month,day,shift,room,0)
                else:
                    flash('Shift not available')
            else:
                if request.form["afternoonshift0"] != "Available":
                    flash('Shift not available')
                elif request.form["afternoonshift0"] == "Available":
                    flash('Facilitator Input Required')
        #remove afternoon shift
        if request.form.get('button') == 'removeafternoon_shift0':
            if request.form["button"] == "removeafternoon_shift0" and request.form["afternoonshift0"] != "Available":
                DB.deleteFromScheduleSlot(year,month,day,room,"Afternoon",0)
            else:
                flash('No Facilitator Assigned')     
                
        #add afternoon shift
        if request.form.get('button') == 'addafternoon_shift1':
            if request.form["button"] == "addafternoon_shift1" and request.form["username_fill"]:
                searchlogin = request.form['username_fill']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                shift = "Afternoon"
                test = DB.searchScheduleSlotAvailability(year,month,day,room,shift,1)
                if test == 0:
                    bool = DB.addToRoomTableSlot(searchlogin,firstname,lastname,year,month,day,shift,room,1)
                else:
                    flash('Shift not available')
            else:
                if request.form["afternoonshift1"] != "Available":
                    flash('Shift not available')
                elif request.form["afternoonshift1"] == "Available":
                    flash('Facilitator Input Required')
        #remove afternoon shift
        if request.form.get('button') == 'removeafternoon_shift1':
            if request.form["button"] == "removeafternoon_shift1" and request.form["afternoonshift1"] != "Available":
                DB.deleteFromScheduleSlot(year,month,day,room,"Afternoon",1)
            else:
                flash('No Facilitator Assigned')  
                        
        #add afternoon shift
        if request.form.get('button') == 'addafternoon_shift2':
            if request.form["button"] == "addafternoon_shift2" and request.form["username_fill"]:
                searchlogin = request.form['username_fill']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                shift = "Afternoon"
                test = DB.searchScheduleSlotAvailability(year,month,day,room,shift,2)
                if test == 0:
                    bool = DB.addToRoomTableSlot(searchlogin,firstname,lastname,year,month,day,shift,room,2)
                else:
                    flash('Shift not available')
            else:
                if request.form["afternoonshift2"] != "Available":
                    flash('Shift not available')
                elif request.form["afternoonshift2"] == "Available":
                    flash('Facilitator Input Required')
        #remove afternoon shift
        if request.form.get('button') == 'removeafternoon_shift2':
            if request.form["button"] == "removeafternoon_shift2" and request.form["afternoonshift2"] != "Available":
                DB.deleteFromScheduleSlot(year,month,day,room,"Afternoon",2)
            else:
                flash('No Facilitator Assigned')                          

        #check for any shifts already scheduled on those above variables
        morning = DB.searchScheduleAllSlots(year,month,day,room,"Morning")
        morning_list = ["Available", "Available", "Available"] 
        if (morning):
            for person in morning:
                morning_list[person[3]] = (person[1] + " " + person[2])
        
        lunch = DB.searchScheduleAllSlots(year,month,day,room,"Lunch")
        lunch_list = ["Available", "Available", "Available"] 
        if (lunch):
            for person in lunch:
                lunch_list[person[3]] = (person[1] + " " + person[2])
        
        afternoon = DB.searchScheduleAllSlots(year,month,day,room,"Afternoon")
        afternoon_list = ["Available", "Available", "Available"] 
        if (afternoon):
            for person in afternoon:
                afternoon_list[person[3]] = (person[1] + " " + person[2])
    
        #search for users, populates the display on the bottom of page with facilitators.
        if request.form.get('button') == 'search':
            if request.form["button"] == "search":
                username = request.form["searchlogin"]
                acc = DB.searchAccount_OnlyFacilitator(username)
                return render_template('admin-schedule-addremove.html', year=year, month=month, day=day, room=room, username=login, accounts=acc, 
                                       actualMorning=morning_list,
                                       actualLunch=lunch_list,
                                       actualAfternoon=afternoon_list)
        
        #Displays page after Add/Remove button clicked
        print("Rendered")
        return render_template('admin-schedule-addremove.html', year=year, month=month, day=day, room=room, username=login,
                               actualMorning=morning_list, 
                               actualLunch=lunch_list, 
                               actualAfternoon=afternoon_list)


# Admin Create Account
@app.route('/admin-createaccount', methods=['GET', 'POST'])
def admincreateaccount():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        type = request.form['type']
        bool = DB.addToUserTable(username,password,type)
        print(bool)
        if bool == True:
            flash('Account created')
        else:
            flash('Account create failed')
    return render_template('admin-createaccount.html',)


# Admin Create Account
@app.route('/admin-createaccount-Facilitator', methods=['GET', 'POST'])
def admincreateaccount_facilitator():
    if request.method == 'POST':
        username = request.form["username_drop"]
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        accountType = request.form["type"]
        DB.addToUsersTable(username, firstname, lastname, accountType)
        print(username)
        if (accountType == "Facilitator"):
            flash('Successfully added facilitator')
        elif (accountType == "Child"):
            flash('Successfully added child')
    acc = DB.searchAccount_FamilyOnly("")
    return render_template('admin-createaccount-Facilitator.html', accounts = acc)


# Admin Edit Account - (Editing Login) 
@app.route('/admin-editaccount', methods=['GET', 'POST'])
def admineditaccount():
    if request.method == "POST":
        username = request.form['username']
        acc = DB.searchAccount(username)
        return render_template('admin-editaccount.html', accounts = acc)
    elif request.method == "GET":
        acc = DB.searchAccount("")
        newacc = []
        for entry in acc:
            lst = list(entry)
            lst[1] = DB.decrypt(lst[1]) 
            entry = tuple(lst)
            newacc.append(entry)
        return render_template('admin-editaccount.html', accounts = newacc)
  
    
# Admin Edit Account - Facilitator - Search
@app.route('/admin-editaccount-Facilitator', methods=['GET', 'POST'])
def admin_editaccount_Facilitator():
    if request.method == "POST":
        if request.form["button"] == "search":
            username = request.form['username']
            acc = DB.searchAccount_Facilitator(username)
            return render_template('admin-editaccount-Facilitator.html', accounts = acc)
        elif request.form["button"] == "edit":
            username = request.form["edit_username"]
            acc = DB.searchAccount_Facilitator(username)
            return redirect(url_for("admin_editaccount_Facilitator_edit", username=username))
    elif request.method == "GET":
        acc = DB.searchAccount_Facilitator("")
        return render_template('admin-editaccount-Facilitator.html', accounts = acc)
 
 
# Admin Edit Account - Facilitator - Edit
@app.route('/admin-editaccount-Facilitator-edit', methods=['GET', 'POST'])
def admin_editaccount_Facilitator_edit():
    if request.method == "POST":
        username_send = ""
        if request.form['my_id'] == "editUser":
            print(request.form['my_id'])
            if request.form['confirm'] == 'save':
                print("Edited")
                userid= request.form['id']
                username = request.form['username']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                accountType = request.form['accountType']
                DB.editAccountUser(firstname, lastname, accountType, userid)
                username_send = username
                
            elif request.form['confirm'] == 'delete':
                username_send = request.form['username']
                userid = request.form['id']            
                DB.deleteAccountUser(userid)
                
        elif request.form['my_id'] == "addUser":
            if request.form['confirm'] == 'add':
                username = request.form['username']
                firstname = request.form['firstname']
                lastname = request.form['lastname']
                accountType = request.form['accountType']        
                valid = DB.checkValidUser(username)
                if valid == True:
                    bool = DB.addToUsersTable(username, firstname, lastname, accountType)
                else:
                    print("Invalid Username")
                username_send = username 
        return redirect(url_for("admin_editaccount_Facilitator_edit", username=username_send))
    
    elif request.method == "GET":
        username = request.args.get("username")
        acc = DB.searchAccount_Facilitator(username)
        return render_template('admin-editaccount-Facilitator-edit.html', username=username, accounts=acc)   
 
 
# Admin Edit Account (Updated Page that shows after edit has been made)
@app.route('/admin-editaccount-delete', methods=['GET', 'POST'])
def admineditaccountdelete():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        accountType = request.form['accountType']
        if request.form['confirm'] == 'save':
            DB.editAccountLogin(password, accountType, username)
        elif request.form['confirm'] == 'delete':
            DB.deleteAccountLogin(username)
            DB.deleteAccountAssociatedUsers(username)
            DB.deleteAccountAssociatedUsersSchedule(username)
    acc = DB.searchAccount("")
    newacc = []
    for entry in acc:
        lst = list(entry)
        lst[1] = DB.decrypt(lst[1]) 
        entry = tuple(lst)
        newacc.append(entry)    
    return render_template('admin-editaccount.html', accounts = newacc)

# Admin Home
@app.route('/adminpage', methods=['GET', 'POST'])
def adminhome():
    return render_template('adminpage.html')

#Statistics page for user 'Admin'
@app.route('/admin-statistics', methods=['GET', 'POST'])
def adminstatistics(chartID = 'chart_ID', chart_type = 'column', chart_height = 600):
    redHours = []
    blueHours = []
    greenHours = []
    greyHours = []
    purpleHours = []
    global adjustedYear
    
    # Changing between years
    if request.method == "POST":
        if request.form.get('button') == 'prev_year':
            if request.form["button"] == "prev_year":
                adjustedYear = adjustedYear - 1
        elif request.form.get('button') == 'next_year':
            if request.form["button"] == "next_year":
                adjustedYear = adjustedYear + 1
        elif request.form.get('button') == 'current_year':
            if request.form["button"] == "current_year":
                adjustedYear = DB.getCurrentYear()
    if request.method == "GET":
        adjustedYear = DB.getCurrentYear()
        
    # adds all the monthly hours for each month into the corresponding room list
    for i in range(1,13):
        redHours.append(DB.getRoomHours('Red', i, adjustedYear)) 
        blueHours.append(DB.getRoomHours('Blue', i, adjustedYear)) 
        greenHours.append(DB.getRoomHours('Green', i, adjustedYear)) 
        greyHours.append(DB.getRoomHours('Grey', i, adjustedYear)) 
        purpleHours.append(DB.getRoomHours('Purple', i, adjustedYear))
    # highcharts variables and data
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Red', "data": [redHours[0],redHours[1],redHours[2],redHours[3],redHours[4],redHours[5],redHours[6],redHours[7],redHours[8],redHours[9],redHours[10],redHours[11]], "color": 'red'}, 
              {"name": 'Blue', "data": [blueHours[0],blueHours[1],blueHours[2],blueHours[3],blueHours[4],blueHours[5],blueHours[6],blueHours[7],blueHours[8],blueHours[9],blueHours[10],blueHours[11]], "color": 'blue'},
              {"name": 'Grey', "data": [greyHours[0],greyHours[1],greyHours[2],greyHours[3],greyHours[4],greyHours[5],greyHours[6],greyHours[7],greyHours[8],greyHours[9],greyHours[10],greyHours[11]], "color": 'grey'},
              {"name": 'Purple', "data": [purpleHours[0],purpleHours[1],purpleHours[2],purpleHours[3],purpleHours[4],purpleHours[5],purpleHours[6],purpleHours[7],purpleHours[8],purpleHours[9],purpleHours[10],purpleHours[11]], "color": 'purple'},
              {"name": 'Green', "data": [greenHours[0],greenHours[1],greenHours[2],greenHours[3],greenHours[4],greenHours[5],greenHours[6],greenHours[7],greenHours[8],greenHours[9],greenHours[10],greenHours[11]], "color": 'green'}]
    title = {"text": 'Monthly Hours - ' + str(adjustedYear)}
    xAxis = {"categories": ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']}
    yAxis = {"title": {"text": 'Time (hours)'}}
    return render_template('admin-statistics.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)

# Admin Schedule
@app.route('/admin-schedule', methods=['GET', 'POST'])
def adminschedule():
    return render_template('admin-schedule.html')

# Board Home
@app.route('/boardpage', methods=['GET', 'POST'])
def boardhome():
    return render_template('boardpage.html')

# Board Schedule
@app.route('/board-schedule', methods=['GET', 'POST'])
def boardschedule():
    return render_template('board-schedule.html')

# Board Statistics
@app.route('/board-statistics', methods=['GET', 'POST'])
def boardstatistics(chartID = 'chart_ID', chart_type = 'column', chart_height = 600):
    redHours = []
    blueHours = []
    greenHours = []
    greyHours = []
    purpleHours = []
    global adjustedYear
    global login
    # Changing between years
    if request.method == "POST":
        if request.form.get('button') == 'prev_year':
            if request.form["button"] == "prev_year":
                adjustedYear = adjustedYear - 1
        elif request.form.get('button') == 'next_year':
            if request.form["button"] == "next_year":
                adjustedYear = adjustedYear + 1
        elif request.form.get('button') == 'current_year':
            if request.form["button"] == "current_year":
                adjustedYear = DB.getCurrentYear()
    if request.method == "GET":
        adjustedYear = DB.getCurrentYear() 
                
    # adds all the monthly hours for each month into the corresponding room list
    for i in range(1,13):
        redHours.append(DB.getRoomHours('Red', i, adjustedYear))
        blueHours.append(DB.getRoomHours('Blue', i, adjustedYear))
        greenHours.append(DB.getRoomHours('Green', i, adjustedYear)) 
        greyHours.append(DB.getRoomHours('Grey', i, adjustedYear)) 
        purpleHours.append(DB.getRoomHours('Purple', i, adjustedYear))
    # highcharts variables and data
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Red', "data": [redHours[0],redHours[1],redHours[2],redHours[3],redHours[4],redHours[5],redHours[6],redHours[7],redHours[8],redHours[9],redHours[10],redHours[11]], "color": 'red'}, 
              {"name": 'Blue', "data": [blueHours[0],blueHours[1],blueHours[2],blueHours[3],blueHours[4],blueHours[5],blueHours[6],blueHours[7],blueHours[8],blueHours[9],blueHours[10],blueHours[11]], "color": 'blue'},
              {"name": 'Grey', "data": [greyHours[0],greyHours[1],greyHours[2],greyHours[3],greyHours[4],greyHours[5],greyHours[6],greyHours[7],greyHours[8],greyHours[9],greyHours[10],greyHours[11]], "color": 'grey'},
              {"name": 'Purple', "data": [purpleHours[0],purpleHours[1],purpleHours[2],purpleHours[3],purpleHours[4],purpleHours[5],purpleHours[6],purpleHours[7],purpleHours[8],purpleHours[9],purpleHours[10],purpleHours[11]], "color": 'purple'},
              {"name": 'Green', "data": [greenHours[0],greenHours[1],greenHours[2],greenHours[3],greenHours[4],greenHours[5],greenHours[6],greenHours[7],greenHours[8],greenHours[9],greenHours[10],greenHours[11]], "color": 'green'}]
    title = {"text": 'Monthly Hours - ' + str(adjustedYear)}
    xAxis = {"categories": ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']}
    yAxis = {"title": {"text": 'Time (hours)'}}
    return render_template('board-statistics.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)    

# Teacher Home
@app.route('/teacherpage', methods=['GET', 'POST'])
def teacherhome():
    return render_template('teacherpage.html')

# Teacher schedules
@app.route('/teacher-schedules', methods=['GET', 'POST'])
def teacherschedules():
    return render_template('teacher-schedules.html')

# Teacher Statistics
@app.route('/teacher-statistics', methods=['GET', 'POST'])
def teacherstatistics(chartID = 'chart_ID', chart_type = 'column', chart_height = 600):
    redHours = []
    blueHours = []
    greenHours = []
    greyHours = []
    purpleHours = []
    global adjustedYear
    global login
    # Changing between years
    if request.method == "POST":
        if request.form.get('button') == 'prev_year':
            if request.form["button"] == "prev_year":
                adjustedYear = adjustedYear - 1
        elif request.form.get('button') == 'next_year':
            if request.form["button"] == "next_year":
                adjustedYear = adjustedYear + 1
        elif request.form.get('button') == 'current_year':
            if request.form["button"] == "current_year":
                adjustedYear = DB.getCurrentYear()
    if request.method == "GET":
        adjustedYear = DB.getCurrentYear() 
                
    # adds all the monthly hours for each month into the corresponding room list
    for i in range(1,13):
        redHours.append(DB.getRoomHours('Red', i, adjustedYear)) 
        blueHours.append(DB.getRoomHours('Blue', i, adjustedYear)) 
        greenHours.append(DB.getRoomHours('Green', i, adjustedYear)) 
        greyHours.append(DB.getRoomHours('Grey', i, adjustedYear)) 
        purpleHours.append(DB.getRoomHours('Purple', i, adjustedYear))
    # highcharts variables and data
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Red', "data": [redHours[0],redHours[1],redHours[2],redHours[3],redHours[4],redHours[5],redHours[6],redHours[7],redHours[8],redHours[9],redHours[10],redHours[11]], "color": 'red'}, 
              {"name": 'Blue', "data": [blueHours[0],blueHours[1],blueHours[2],blueHours[3],blueHours[4],blueHours[5],blueHours[6],blueHours[7],blueHours[8],blueHours[9],blueHours[10],blueHours[11]], "color": 'blue'},
              {"name": 'Grey', "data": [greyHours[0],greyHours[1],greyHours[2],greyHours[3],greyHours[4],greyHours[5],greyHours[6],greyHours[7],greyHours[8],greyHours[9],greyHours[10],greyHours[11]], "color": 'grey'},
              {"name": 'Purple', "data": [purpleHours[0],purpleHours[1],purpleHours[2],purpleHours[3],purpleHours[4],purpleHours[5],purpleHours[6],purpleHours[7],purpleHours[8],purpleHours[9],purpleHours[10],purpleHours[11]], "color": 'purple'},
              {"name": 'Green', "data": [greenHours[0],greenHours[1],greenHours[2],greenHours[3],greenHours[4],greenHours[5],greenHours[6],greenHours[7],greenHours[8],greenHours[9],greenHours[10],greenHours[11]], "color": 'green'}]
    title = {"text": 'Monthly Hours - ' + str(adjustedYear)}
    xAxis = {"categories": ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']}
    yAxis = {"title": {"text": 'Time (hours)'}}
    return render_template('teacher-statistics.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)

# Family Home
@app.route('/familypage', methods=['GET', 'POST'])
def familyhome():
    global login
    month = datetime.now().month
    year = datetime.now().year
    day = datetime.now().day
    numChild = DB.countChild(login)
    currentHours = DB.getCurrentHours(login, year, month)
    # 5 hours per week times 4 weeks per month
    if int(numChild) >= 2:
        neededMonthlyHours = 20
    # 2.5 hours per week times 4 weeks per month
    else:
        neededMonthlyHours = 10
    
    upcoming = DB.upcomingShifts(login, year, month, day)
    
    return render_template('familypage.html', login = login, numChild = numChild, neededMonthlyHours = neededMonthlyHours, 
                           currentHours = currentHours, upcoming = upcoming)

# Family Donate Hours
@app.route('/family-donate', methods=['GET', 'POST'])
def familydonate():
    global login;
    month = datetime.now().month
    year = datetime.now().year    
    if request.method == "POST":
        if request.form.get('confirm') == 'yes':
            if request.form["confirm"] == "yes":
                username = request.form["username_drop"]
                firstname = request.form["FirstName"]
                lastname = request.form["LastName"]
                day = request.form["Day"]
                room = request.form["Room"]
                shift = request.form["Shift"]
                slot = request.form["Slot"]
                DB.donateshift(year,month,day,room,shift,slot,username)
    family = DB.searchAccount_FamilyOnly("")
    acc = DB.searchScheduleDonate(year,month,login)
    return render_template('family-donate.html', family=family, accounts=acc)

# Family Account Info
@app.route('/family-accountinfo', methods=['GET', 'POST'])
def familyaccountinfo():
    global login;
    acc = DB.searchAccount_Facilitator(login)
    return render_template('family-accountinfo.html', accounts=acc)

# Family Schedule
@app.route('/family-schedule', methods=['GET', 'POST'])
def familyschedule():
    return render_template('family-schedule.html')

# Family Statistics
@app.route('/family-statistics', methods=['GET', 'POST'])
def familystatistics(chartID = 'chart_ID', chart_type = 'column', chart_height = 600):
    redHours = []
    blueHours = []
    greenHours = []
    greyHours = []
    purpleHours = []
    global adjustedYear
    global login
    # Changing between years
    if request.method == "POST":
        if request.form.get('button') == 'prev_year':
            if request.form["button"] == "prev_year":
                adjustedYear = adjustedYear - 1
        elif request.form.get('button') == 'next_year':
            if request.form["button"] == "next_year":
                adjustedYear = adjustedYear + 1
        elif request.form.get('button') == 'current_year':
            if request.form["button"] == "current_year":
                adjustedYear = DB.getCurrentYear()
    if request.method == "GET":
        adjustedYear = DB.getCurrentYear() 
                
    # adds all the monthly hours for each month into the corresponding room list
    for i in range(1,13):
        redHours.append(DB.getRoomHoursUser('Red', i, adjustedYear, login)) 
        blueHours.append(DB.getRoomHoursUser('Blue', i, adjustedYear, login)) 
        greenHours.append(DB.getRoomHoursUser('Green', i, adjustedYear, login)) 
        greyHours.append(DB.getRoomHoursUser('Grey', i, adjustedYear, login)) 
        purpleHours.append(DB.getRoomHoursUser('Purple', i, adjustedYear, login))
    # highcharts variables and data
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'Red', "data": [redHours[0],redHours[1],redHours[2],redHours[3],redHours[4],redHours[5],redHours[6],redHours[7],redHours[8],redHours[9],redHours[10],redHours[11]], "color": 'red'}, 
              {"name": 'Blue', "data": [blueHours[0],blueHours[1],blueHours[2],blueHours[3],blueHours[4],blueHours[5],blueHours[6],blueHours[7],blueHours[8],blueHours[9],blueHours[10],blueHours[11]], "color": 'blue'},
              {"name": 'Grey', "data": [greyHours[0],greyHours[1],greyHours[2],greyHours[3],greyHours[4],greyHours[5],greyHours[6],greyHours[7],greyHours[8],greyHours[9],greyHours[10],greyHours[11]], "color": 'grey'},
              {"name": 'Purple', "data": [purpleHours[0],purpleHours[1],purpleHours[2],purpleHours[3],purpleHours[4],purpleHours[5],purpleHours[6],purpleHours[7],purpleHours[8],purpleHours[9],purpleHours[10],purpleHours[11]], "color": 'purple'},
              {"name": 'Green', "data": [greenHours[0],greenHours[1],greenHours[2],greenHours[3],greenHours[4],greenHours[5],greenHours[6],greenHours[7],greenHours[8],greenHours[9],greenHours[10],greenHours[11]], "color": 'green'}]
    title = {"text": 'Monthly Hours - ' + str(adjustedYear)}
    xAxis = {"categories": ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']}
    yAxis = {"title": {"text": 'Time (hours)'}}
    return render_template('family-statistics.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)

if __name__ == "__main__":
    DB.initDB()
    app.run()