from flask import Flask,render_template, request
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




@app.route('/')
def index():
    return render_template("layout.html")







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
      return render_template('viewdoctors.html',msg=data)

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
      return render_template('viewnurses.html',msg=data)




















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
    app.run(debug=True)