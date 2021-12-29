from flask import Flask,render_template, request
import mysql.connector

app = Flask("__main__")

mydb = mysql.connector.connect(
    host = 'localhost',
    user='root',
    passwd = 'root',
    database= 'sys',
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()


@app.route('/adddoctor',methods = ['POST','GET'])
def AddDoctors():
    if request.method == 'POST':
        name = request.form['name']
        sql = "INSERT INTO  myDataBase (name) VALUES(%s)"
        val = (name)
        mycursor.execute(sql,val)

        return render_template("layout.html")
    else:
        return render_template("layout.html")


@app.route('/')
def index():
    return render_template("layout.html")

@app.route('/contactus')
def contactus():
    return render_template("contactus.html")


if __name__ == '__main__':
    app.run(debug=True)