from flask import Flask,render_template, request, url_for
import mysql.connector

app = Flask("__main__")

mydb = mysql.connector.connect(
    host = 'localhost',
    user='root',
    passwd = 'root',
    database= 'icuroom',
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

username =""
role=""
userssn = 0

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == "POST":
        user_name = request.form['username']
        password = request.form['password']


        global username
        global role
        global userssn
        username =""
        role=""
        userssn = 0

        if user_name == "admin" and password == "admin":
            role = "admin"
            username = user_name
            return render_template("home.html")


        mycursor.execute("SELECT dssn FROM doctor WHERE username=%s AND  password=%s ", (user_name, password,))
        result = mycursor.fetchall()
        if result:
            userssn = result[0]
            role = "doctor"
            username = user_name
            return render_template("home.html")

        mycursor.execute("SELECT nur_ssn FROM nurse WHERE username=%s AND  password=%s ", (user_name, password,))
        result = mycursor.fetchall()
        if result:
            userssn = result[0]
            role = "nurse"
            username = user_name
            return render_template("home.html")

        mycursor.execute("SELECT pat_ssn FROM patient WHERE username=%s AND  password=%s ", (user_name, password,))
        result = mycursor.fetchall()
        if result:
            userssn = result[0]
            role = "patient"
            username = user_name
            return render_template("home.html")

    return render_template("login.html")

    return render_template("home.html")


    return render_template('login.html')


@app.route('/signup',methods = ['POST', 'GET'])
def signup():
    if request.method == "POST":
        role = request.form['role']
        if role == "doctor":
            return render_template("signupdoctor.html")

    return render_template("signup.html")



@app.route('/signupdoctor',methods = ['POST', 'GET'])
def signupdoctor():
   if request.method == 'POST':
      Fname = request.form['Fname']
      Lname = request.form['Lname']
      address = request.form['address']
      age = request.form['age']
      salary = request.form['salary']
      phone = request.form['phone']
      gender = request.form['gender']
      DSSN = request.form['DSSN']
      RNum = request.form['RNum']
      Username = request.form['Username']
      Password = request.form['Password']
      print(Fname,Lname,address,age,salary,phone,gender,DSSN,RNum,Username,Password)
      sql = "INSERT INTO doctor (Fname,Lname,address,age,salary,phone,gender,DSSN,RNum,Username,Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
      val = (Fname,Lname,address,age,salary,phone,gender,DSSN,RNum,Username,Password)
      mycursor.execute(sql,val)
      mydb.commit()
      return render_template('home.html')
   else:
        return render_template('signupdoctor.html')


@app.route('/Signupnurse',methods = ['POST', 'GET'])
def Signupnurse():
   if request.method == 'POST':
      Fname = request.form['Fname']
      Lname = request.form['Lname']
      address = request.form['address']
      age = request.form['age']
      salary = request.form['salary']
      CareRoom = request.form['CareRoom']
      phone = request.form['phone']
      gender = request.form['gender']
      DSSN = request.form['DSSN']
      NSSN = request.form['NSSN']
      Username = request.form['Username']
      Password = request.form['Password']
      print(Fname,Lname,address,age,salary,CareRoom,phone,gender,DSSN,NSSN,Username,Password)
      sql = "INSERT INTO Signupnurse (Fname,Lname,address,age,salary,CareRoom,phone,gender,DSSN,NSSN,Username,Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
      val = (Fname,Lname,address,age,salary,CareRoom,phone,gender,DSSN,NSSN,Username,Password)
      mycursor.execute(sql,val)
      mydb.commit()
      return render_template('home.html')
   else:
        return render_template('Signupnurse.html')
@app.route('/Signuppatient',methods = ['POST', 'GET'])
def Signuppatient():
   if request.method == 'POST':
      Fname = request.form['Fname']
      Lname = request.form['Lname']
      address = request.form['address']
      age = request.form['age']
      salary = request.form['salary']
      phone = request.form['phone']
      gender = request.form['gender']
      DSSN = request.form['DSSN']
      PSSN = request.form['PSSN']
      NSSN = request.form['NSSN']
      RNum = request.form['RNum']
      Medicine = request.form['Medicine']
      Disease = request.form['Disease']
      Username = request.form['Username']
      Password = request.form['Password']
      print(Fname,Lname,address,age,salary,phone,gender,DSSN,PSSN,RNum,NSSN,Medicine,Disease,Username,Password)
      sql = "INSERT INTO Signuppatient (Fname,Lname,address,age,salary,phone,gender,DSSN,PSSN,RNum,NSSN,Medicine,Disease,Username,Password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
      val = (Fname,Lname,address,age,salary,phone,gender,DSSN,PSSN,RNum,NSSN,Medicine,Disease,Username,Password)
      mycursor.execute(sql,val)
      mydb.commit()
      return render_template('layout.html')
   else:
        return render_template('Signuppatient.html')






@app.route('/',methods = ['POST', 'GET'])
def home():
    if role == "":
        return render_template('login.html')
    return render_template("home.html")


@app.route('/viewdoctor')
def viewdoctor():
    if role != "admin" and role != "doctor" and role != "nurse" and role != "patient":
        return render_template('login.html')

    if (role == "admin"):
        mycursor.execute("SELECT * FROM DOCTOR")

    elif (role == "doctor"):
        mycursor.execute(
            "SELECT DOC_FNAME,DOC_LNAME,DOC_ADDRESS,DOC_GENDER,DOC_AGE,DOC_PHONE,DOC_SALARY,ROOM_NUMBER FROM doctor where DOC_SSN= %s " % (
            userssn))

    elif (role == "nurse"):
        mycursor.execute(
            "SELECT DOC_FNAME,DOC_LNAME,DOC_GENDER,DOC_PHONE,ROOM_NUMBER FROM doctor JOIN nurse on DOC_SSN=NUR_DOC_SSN where NUR_SSN= %s " % (
            userssn)) # join add

    elif (role == "patient"):
        mycursor.execute(
            "SELECT DOC_FNAME,DOC_LNAME,DOC_GENDER,DOC_PHONE,ROOM_NUMBER FROM doctor JOIN patient on DOC_SSN=PAT_DOC_SSN where PAT_SSN= %s " % (
            userssn)) #DOC_SSN changed to PAT_SSN

    row_headers = [x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    data = {
        'message': "data retrieved",
        'rec': myresult,
        'header': row_headers
    }
    return render_template('viewdoctor.html', msg=data)


@app.route('/viewnurse')
def viewnurse():
    if role != "admin" and role != "doctor" and role != "nurse" and role != "patient":
        return render_template('login.html')

    if (role == "admin"):
        mycursor.execute("SELECT * FROM NURSE")

    elif (role == "doctor"):
        mycursor.execute(
            "SELECT NUR_FNAME,NUR_LNAME,NUR_ADRESS,NUR_GENDER,NUR_PHONE,NUR_CARE_R FROM nurse where NUR_DOC_SSN= %s " % (
            userssn)) # ,NUR_AGE,NUR_SALARY removed

    elif (role == "nurse"):
        mycursor.execute(
            "SELECT NUR_FNAME,NUR_LNAME,NUR_ADRESS,NUR_GENDER,NUR_AGE,NUR_PHONE,NUR_SALARY,NUR_CARE_R FROM doctor JOIN nurse on DOC_SSN=NUR_DOC_SSN where NUR_SSN= %s " % (
            userssn)) # no need for join here

    elif (role == "patient"):
        mycursor.execute(
            "SELECT NUR_FNAME,NUR_LNAME,NUR_GENDER,NUR_PHONE,NUR_CARE_R FROM nurse JOIN patient on NUR_SSN = PAT_NUR_SSN where PAT_SSN= %s " % (
            userssn))
    row_headers = [x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    data = {
        'message': "data retrieved",
        'rec': myresult,
        'header': row_headers
    }
    return render_template('viewnurse.html', msg=data)


@app.route('/viewequipment')
def viewequpment():
    if role != "admin" and role != "doctor" and role != "nurse" and role != "patient":
        return render_template('login.html')

    if (role == "admin"):
        mycursor.execute("SELECT * FROM EQUIPMENT")

    elif (role == "doctor"):
        mycursor.execute(
            "SELECT EQ_CODE,EQ_MANUFACTURER,EQ_NAME,EQ_MODEL FROM equipment JOIN patient on EQ_PAT_SSN = PAT_SSN JOIN doctor on PAT_DOC_SSN=DOC_SSN where DOC_SSN= %s " % (
            userssn)) #EQ_CODE = EQ_PAT_SSN changed to EQ_PAT_SSN = PAT_SSN // EQ_CODE changed to DOC_SSN
    elif (role == "nurse"):
        mycursor.execute(
            "SELECT EQ_CODE,EQ_MANUFACTURER,EQ_NAME,EQ_MODEL FROM equipment JOIN patient on EQ_PAT_SSN = PAT_SSN JOIN nurse on PAT_NUR_SSN=NUR_SSN where NUR_SSN= %s " % (
            userssn))#EQ_CODE = EQ_PAT_SSN changed to EQ_PAT_SSN = PAT_SSN // EQ_CODE changed to NUR_SSN

    elif (role == "patient"):
        mycursor.execute(
            "SELECT EQ_CODE,EQ_MANUFACTURER,EQ_NAME,EQ_MODEL FROM equipment JOIN patient on EQ_PAT_SSN=PAT_SSN where PAT_SSN= %s " % (
            userssn))#changed
    row_headers = [x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    data = {
        'message': "data retrieved",
        'rec': myresult,
        'header': row_headers
    }
    return render_template('viewequipment.html', msg=data)


@app.route('/viewpatient')
def viewpatient():
    if role != "admin" and role != "doctor" and role != "nurse" and role != "patient":
        return render_template('login.html')

    if (role == "admin"):
        mycursor.execute("SELECT * FROM PATIENT")

    elif (role == "doctor"):
        mycursor.execute(
            "SELECT PAT_FNAME,PAT_LNAME,PAT_DISEASE,PAT_GENDER,PAT_AGE,PAT_PHONE,PAT_MEDICINE FROM doctor JOIN patient on DOC_SSN=PAT_DOC_SSN where PAT_SSN= %s " % (
            userssn))

    elif (role == "nurse"):
        mycursor.execute(
            "SELECT PAR_FNAME,PAR_LNAME,PAT_DISEASE,PAT_GENDER,PAT_AGE,PAT_PHONE,PAT_MEDICINE FROM nurse JOIN patient on NUR_SSN=PAT_NUR_SSN where PAT_SSN= %s " % (
            userssn))

    elif (role == "patient"):
        mycursor.execute(
            "SELECT PAT_FNAME,PAT_LNAME,PAT_DISEASE,PAT_GENDER, PAT_ADDRESS,PAT_AGE,PAT_PHONE,PAT_MEDICINE FROM patient where PAT_SSN= %s " % (
            userssn))
    row_headers = [x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    data = {
        'message': "data retrieved",
        'rec': myresult,
        'header': row_headers
    }
    return render_template('viewpatient.html', msg=data)


@app.route('/viewdependent')
def viewdependent():
    if role != "admin" and role != "patient":
        return render_template('login.html')

    if (role == "admin"):
        mycursor.execute("SELECT * FROM DEPENDENT")

    elif (role == "patient"):
        mycursor.execute(
            "SELECT DEP_NAME,DEP_RELATIONSHIP,DEP_AGE,DEP_PHONE,DEP_GENDER FROM patient JOIN dependent on PAT_SSN = DEP_PAT_SSN where DEP_SSN= %s " % (
            userssn)) ####
    row_headers = [x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    data = {
        'message': "data retrieved",
        'rec': myresult,
        'header': row_headers
    }
    return render_template('viewdependent.html', msg=data)


@app.route('/viewroom')
def viewroom():
    if role != "admin" and role != "doctor" and role != "nurse" and role != "patient":
        return render_template('login.html')

    if (role == "admin"):
        mycursor.execute("SELECT * FROM ROOM")

    elif (role == "doctor"):
        mycursor.execute(
            "SELECT R_NAME,R_NUMBER,FLOOR_NUMBER FROM doctor JOIN room on DOC_ROOM_NUMBER=R_NUMBER where DOC_SSN= %s " % (
            userssn))#R_NUMBER changed to DOC_SSN

    elif (role == "nurse"):
        mycursor.execute(
            "SELECT R_NAME,R_NUMBER,FLOOR_NUMBER FROM nurse JOIN room on NUR_ROOM_NUMBER=R_NUMBER where NUR_SSN= %s " % (
            userssn))#R_NUMBER changed to NUR_SSN

    elif (role == "patient"):
        mycursor.execute(
            "SELECT R_NAME,R_NUMBER,FLOOR_NUMBER FROM patient JOIN room on PAT_ROOM_NUMBER=R_NUMBER where PAT_SSN= %s " % (
            userssn))#R_NUMBER changed to PAT_SSN
    row_headers = [x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    data = {
        'message': "data retrieved",
        'rec': myresult,
        'header': row_headers
    }
    return render_template('viewroom.html', msg=data)


'''
@app.route('/viewdoctor')
def viewdoctors():
    if role != "admin" and role != "doctor" and role != "nurse":
        return render_template('login.html')

    if role == "doctor":
        mycursor.execute("SELECT FNAME,LNAME,PHONE,GENDER,RNum FROM doctor WHERE dssn=%s " %(userssn))
    elif role == "admin":
        mycursor.execute("SELECT * FROM DOCTORS")
    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    data={
     'message':"data retrieved",
     'rec':myresult,
     'header':row_headers
    }
    return render_template('viewdoctor.html',msg=data)

@app.route('/viewdoctor')
def viewdoctor():
   if role !="admin" and role !="doctor" and role !="nurse" and role !="patient":
      return render_template('login.html')

   if(role == "admin"):
      mycursor.execute("SELECT * FROM DOCTOR")

   elif(role == "doctor"):
      mycursor.execute("SELECT DOC_FNAME,DOC_LNAME,DOC_ADDRESS,DOC_GENDER,DOC_AGE,DOC_PHONE,DOC_SALARY,ROOM_NUMBER FROM doctor where DOC_SSN= %s " %(userssn) )

   elif(role == "nurse"):
      mycursor.execute("SELECT DOC_FNAME,DOC_LNAME,DOC_GENDER,DOC_PHONE,ROOM_NUMBER FROM doctor where NURSE_SUPERVISOR= %s " %(userssn) )

   elif(role == "patient"):
      mycursor.execute("SELECT DOC_FNAME,DOC_LNAME,DOC_GENDER,DOC_PHONE,ROOM_NUMBER FROM doctor JOIN patient on DOC_SSN=PAT_SSN where DOC_SSN= %s " %(userssn) )

   row_headers=[x[0] for x in mycursor.description]
   myresult = mycursor.fetchall()
   data={
      'message':"data retrieved",
      'rec':myresult,
      'header':row_headers
        }
   return render_template('viewdoctor.html',msg=data)

@app.route('/viewequipment')
def viewequipment():
    if role != "admin" and  role != "doctor" and role !="nurse":
        return render_template('login.html')
    mycursor.execute("SELECT * FROM EQUIPMENT")
    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    data={
     'message':"data retrieved",
     'rec':myresult,
     'header':row_headers
    }
    return render_template('viewequipment.html',msg=data)

@app.route('/viewnurse')
def viewnurse():


    if role != "admin" and role != "doctor" and role != "nurse":
        return render_template('login.html')

    if role == "admin":
        mycursor.execute("SELECT * FROM NURSE")
    elif role == "doctor":
        mycursor.execute("SELECT  nurse First Name,nurse Last Name,Phone,Gender,Care Room FROM nurse where NURSE_SUPERVISOR = %s " %(userssn))
    elif role == "nurse":
        mycursor.execute("SELECT  nurse First Name,nurse Last Name,Phone,Gender,Care Room FROM nurse where nur_ssn=%s"%(userssn))
    elif role == "patient":
        mycursor.execute("SELECT  nurse First Name,nurse Last Name,Phone,Gender,Care Room FROM nurse where nur_ssn=%s"%(userssn)) # to be changed


    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    data={
     'message':"data retrieved",
     'rec':myresult,
     'header':row_headers
    }
    return render_template('viewnurse.html',msg=data)
@app.route('/viewpatient')
def viewpatient():
    if role != "admin" and role != "patient" and role != "doctor" and role != "nurse":
        return render_template('login.html')

    if role == "patient":
        mycursor.execute("SELECT SSN,Disease,Medicine FROM patient")
    elif role == "admin" or role == "doctor" or role == "nurse":
        mycursor.execute("SELECT * FROM  patient")
    row_headers = [x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    data = {
        'message': "data retrieved",
        'rec': myresult,
        'header': row_headers
    }
    return render_template('viewpatient.html', msg=data)

@app.route('/viewdependent')
def viewdependent():
    if role != "admin":
        return render_template('login.html')
    mycursor.execute("SELECT * FROM DEPENDENT")
    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    data={
     'message':"data retrieved",
     'rec':myresult,
     'header':row_headers
    }
    return render_template('viewdependent.html',msg=data)

@app.route('/viewroom')
def viewroom():
    if role != "admin" and role != "nurse" and role != "patient" and role != "doctor":
        return render_template('login.html')


    mycursor.execute("SELECT * FROM ROOM")
    row_headers=[x[0] for x in mycursor.description]
    myresult = mycursor.fetchall()
    data={
     'message':"data retrieved",
     'rec':myresult,
     'header':row_headers
    }
    return render_template('viewroom.html',msg=data)

'''


####### add

@app.route('/adddoctor',methods = ['POST', 'GET'])
def adddoctor():
   if request.method == 'POST':
      Fname = request.form['Fname']
      Lname = request.form['Lname']
      address = request.form['address']
      age = request.form['age']
      phone = request.form['phone']
      gender = request.form['gender']
      DSSN = request.form['DSSN']
      RNum = request.form['RNum']
      salary = request.form['salary']
      print(Fname,Lname,address,age,phone,gender,DSSN,RNum)
      sql = "INSERT INTO doctor (DOC_Fname,DOC_Lname,DOC_address,DOC_age,DOC_phone,DOC_gender,DOC_SSN,DOC_ROOM_NUMBER,DOC_salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
      val = (Fname,Lname,address,age,phone,gender,DSSN,RNum,salary)
      mycursor.execute(sql,val)
      mydb.commit()
      return render_template('home.html')
   if role != "doctor" and role !="admin":
       return render_template('login.html')
   return render_template('adddoctor.html')
@app.route('/addequipment',methods = ['POST', 'GET'])
def addeqipment():
   if request.method == 'POST':
      code = request.form['code']
      manufacturer = request.form['manufacturer']
      Ename = request.form['Ename']
      Emodel = request.form['Emodel']
      PSSN = request.form['PSSN']
      print(code,manufacturer,Ename,Emodel,PSSN)
      sql = "INSERT INTO Equipment (EQ_code,EQ_manufacturer,EQ_name,EQ_model,EQ_PAT_SSN) VALUES (%s, %s, %s, %s, %s)"
      val = (code,manufacturer,Ename,Emodel,PSSN)
      mycursor.execute(sql, val)
      mydb.commit()
      return render_template('home.html')
   if role != "doctor" and role !="admin":
       return render_template('login.html')
   return render_template('addequipment.html')
@app.route('/adddependent',methods = ['POST', 'GET'])
def adddependent():
   if request.method == 'POST':
      Dname = request.form['Dname']
      PSSN = request.form['PSSN']
      relationship = request.form['relationship']
      age = request.form['age']
      phone = request.form['phone']
      gender = request.form['gender']
      print(Dname,relationship,age,phone,gender,PSSN)
      sql = "INSERT INTO Dependent (DEP_name,DEP_relationship,DEP_age,DEP_phone,DEP_gender,DEP_PAT_SSN) VALUES (%s, %s, %s, %s, %s, %s)"
      val = (Dname,relationship,age,phone,gender,PSSN)
      mycursor.execute(sql, val)
      mydb.commit()
      return render_template('home.html')
   if role != "doctor" and role !="admin":
        return render_template('login.html')
   return render_template('adddependent.html')

###

@app.route('/addpatient', methods=['POST', 'GET'])
def addpatient():

    if request.method == "POST":  # check if there is post data
        pfname = request.form['Patient First Name']
        plname = request.form['Patient Last Name']
        pssn = request.form['Pateint SSN']
        page = request.form['Patient Age']
        pphone = request.form['Patient Phone']
        pdisease = request.form['Patient Disease']
        med=request.form['Patient Medicine']
        address=request.form['Patient Address']
        gender=request.form['Patient Gender']
        rno = request.form['NORoom']
        Docssn = request.form['SSNDoctor']
        Nurssn = request.form['SSNNurse']
        sql = "INSERT INTO patient (PAT_FNAME, PAT_LNAME, PAT_SSN, PAT_AGE, PAT_PHONE, PAT_DISEASE, PAT_MEDICINE, PAT_ADDRESS,PAT_GENDER,PAT_ROOM_NUMBER,PAT_DOC_SSN,PAT_NUR_SSN) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)"
        val = (pfname, plname,pssn , page, pphone, pdisease, med, address,gender,rno,Docssn,Nurssn)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template('home.html')
    else:
        if role != "doctor" and role != "admin" and role != "nurse" and role != "patient":
            return render_template('login.html')
        return render_template('addpatient.html')
#start of addnurse
@app.route('/addnurse', methods=['POST', 'GET'])
def addnurse():

    if request.method == "POST":  # check if there is post data
        nfname = request.form['nurse First Name']
        nlname = request.form['nurse Last Name']
        nssn = request.form['nurse SSN']
        nage = request.form['nurse Age']
        nphone = request.form['nurse Phone']
        naddress=request.form['nurse Address']
        ngender=request.form['nurse Gender']
        nsalary=request.form['nurse Salary']
        nroom = request.form['nurse Care Room']
        ndoc = request.form['nurse Supervisor']
        sql = "INSERT INTO nurse (NUR_SSN, NUR_FNAME, NUR_LNAME, NUR_AGE, NUR_PHONE, NUR_ADDRESS, NUR_GENDER, NUR_SALARY,NUR_ROOM_NUMBER,NUR_DOC_SSN) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
        val = (nssn,nfname, nlname, nage, nphone, naddress, ngender, nsalary,nroom,ndoc)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template('home.html')
    else:
        if role != "doctor" and role != "admin" and role != "nurse":
            return render_template('login.html')
        return render_template('addnurse.html')
@app.route('/addroom', methods=['POST', 'GET'])
def addroom():

    if request.method == "POST":  # check if there is post data
        rnumber = request.form['room Number']
        rname = request.form['room Name']
        rfnumber = request.form['floor Number']
        sql = "INSERT INTO room (R_NUMBER, R_NAME, FLOOR_NUMBER) VALUES (%s, %s, %s)"
        val = (rnumber,rname, rfnumber)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template('home.html')
    else:
        if role != "nurse" and role != "admin":
            return render_template('login.html')
        return render_template('addroom.html')


######

@app.route('/contactus',methods = ['POST','GET'])
def contactus():
    if request.method == 'POST':

        email = request.form['email']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        role = request.form['role']
        ssn = request.form['ssn']
        complainttext = request.form['complainttext']

        sql = "insert into complaint (email,firstname,lastname,role,ssn,complainttext) values('%s','%s','%s','%s','%s','%s')" %(email,firstname,lastname,role,ssn,complainttext)
        #sql = "insert into rol (role) values ('%s');" %(role)
        #val=""
        mycursor.execute(sql)
        mydb.commit()
        print(mydb)
        return render_template("layout.html")
    else:
        return render_template("contactus.html")





if __name__ == '__main__':
    app.run()