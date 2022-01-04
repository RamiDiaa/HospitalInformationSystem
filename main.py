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




@app.route('/',methods = ['POST', 'GET'])
def home():
    return render_template("home.html")
@app.route('/viewdoctor')
def viewdoctors():
      mycursor.execute("SELECT * FROM DOCTORS")
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
      mycursor.execute("SELECT * FROM EQUIPMENT")
      row_headers=[x[0] for x in mycursor.description]
      myresult = mycursor.fetchall()
      data={
         'message':"data retrieved",
         'rec':myresult,
         'header':row_headers
      }
      return render_template('viewequipment.html',msg=data)

@app.route('/viewnurses')
def viewnurses():
      mycursor.execute("SELECT * FROM NURSES")
      row_headers=[x[0] for x in mycursor.description]
      myresult = mycursor.fetchall()
      data={
         'message':"data retrieved",
         'rec':myresult,
         'header':row_headers
      }
      return render_template('viewnurse.html',msg=data)


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
      print(Fname,Lname,address,age,phone,gender,DSSN,RNum)
      sql = "INSERT INTO doctors (Fname,Lname,address,age,phone,gender,DSSN,RNum) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
      val = (Fname,Lname,address,age,phone,gender,DSSN,RNum)
      mycursor.execute(sql,val)
      mydb.commit()
      return render_template('home.html')
   else:
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
      sql = "INSERT INTO Equipment (code,manufacturer,Ename,Emodel,PSSN) VALUES (%s, %s, %s, %s, %s)"
      val = (code,manufacturer,Ename,Emodel,PSSN)
      mycursor.execute(sql, val)
      mydb.commit()
      return render_template('home.html')
   else:
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
      sql = "INSERT INTO Dependent (Dname,relationship,age,phone,gender,PSSN) VALUES (%s, %s, %s, %s, %s, %s)"
      val = (Dname,relationship,age,phone,gender,PSSN)
      mycursor.execute(sql, val)
      mydb.commit()
      return render_template('home.html')
   else:
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
        sql = "INSERT INTO patient (PAT_FNAME, PAT_LNAME, PAT_SSN, PAT_AGE, PAT_PHONE, PAT_DISEASE, PAT_MEDICINE, PAT_ADDRESS,PATIENT_GENDER,NOROOM,SSN_DOCTOR,SSN_NURSE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)"
        val = (pfname, plname,pssn , page, pphone, pdisease, med, address,gender,rno,Docssn,Nurssn)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template('home.html')
    else:
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
        sql = "INSERT INTO nurse (NUR_SSN, NUR_FNAME, NUR_LNAME, NUR_AGE, NUR_PHONE, NUR_ADDRESS, NUR_GENDER, NUR_SALARY,NUR_CARE_R,NURSE_SUPERVISOR) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s)"
        val = (nssn,nfname, nlname, nage, nphone, naddress, ngender, nsalary,nroom,ndoc)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template('home.html')
    else:
        return render_template('addnurse.html')
@app.route('/addroom', methods=['POST', 'GET'])
def addroom():

    if request.method == "POST":  # check if there is post data
        rnumber = request.form['room Number']
        rname = request.form['room Name']
        rfnumber = request.form['floor Number']
        sql = "INSERT INTO room (ROOM_NUMBER, ROOM_NAME, FLOOR_NUMBER) VALUES (%s, %s, %s)"
        val = (rnumber,rname, rfnumber)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template('home.html')
    else:
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
    app.run(debug = True)