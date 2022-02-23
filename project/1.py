from flask import Flask, render_template, request, redirect
import mysql.connector

app=Flask(__name__)

db=mysql.connector.connect(host="localhost",
							user="root",
							password="root",
							database="mis2"
							)
mycursor=db.cursor()

@app.route("/")
def homepage():
	mycursor.execute("Select * from personal")
	records=mycursor.fetchall();
	return render_template("homepage.html",data=records)

@app.route("/department/<dept>")
def departmentlist(dept):
	mycursor.execute("Select * from personal where department='"+dept+"'")
	records=mycursor.fetchall();

@app.route("/newrecord")
def newrecord():
	return render_template("inputform.html")

@app.route("/saverecord", methods=["post"])
def saverecord():
	name=request.form["na"]
	dept=request.form["dept"]
	mycursor.execute("insert into personal(name, department) values('{0}','{1}')".format(name,dept))
	db.commit()
	return redirect("/")

@app.route("/details/<empno>")
def details(empno):
	mycursor.execute("Select * from personal where empno="+empno)
	personalrecord=mycursor.fetchall();
	mycursor.execute("Select * from accoints where empno="+empno)
	salaryrecords=mycursor.fetchall();
	return render_template("details.html",personal=personalrecord,accoints=salaryrecords)

app.run(debug=True)