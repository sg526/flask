from flask import Flask, render_template

app=Flask(__name__)

@app.route("/info1")
def homepage1():
	return  render_template("information.html", na="Sophie", addr="Swindon", color="red")

@app.route("/info2")
def homepage2():
	return  render_template("information.html", na="James", addr="London", color="blue")

@app.route("/info3")
def homepage3():
	return  render_template("information.html", na="Smith", addr="Glasgow", color="green")

app.run()