from flask import Flask,render_template, request
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user='root',
    passwd = 'mysql',
    database= 'MyPythonDatabase'
)

mycursor = mydb.cursor()
app = Flask("__main__")

@app.route('/')
def index():
    return render_template("home.html")

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




if __name__ == '__main__':
    app.run(debug=True)