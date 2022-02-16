from flask import Flask, render_template

app=Flask(__name__)

@app.route("/info1")
def homepage1():
	return  render_template("salaryslips.html",name="Sophie",salary=2000)

app.run()