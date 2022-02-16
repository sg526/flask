from flask import Flask

app=Flask(__name__)

@app.route("/")
def homepage():
	return  """
			<html>
			<center> <h1> Welcome to my homepage </h1> </center>
			We are the only building society in the United Kingdom
			<br>
			<br>
			<a href="http://localhost:5000/Team"> Who we are </a>
			<br>
			<a href="http://localhost:5000/Services"> Our Services </a> <br>
			</html>
			"""
			
@app.route("/Team")
def message():
	return """
			<html>
			<h2> <center> Our team are as follows: </center> </h2>
			<br>
			<a href="http://localhost:5000"> Home </a>
			<br>
			<ul>
				<li> Sophie Green </li>
				<li> Lee Duffy </li>
				<li> George Webster </li>
			</ul>
			</html>
			"""

@app.route("/Services")
def boom():
	return 	"""
			<html>
			<h2> <center> We provide the following services: </center> </h2>
			<br>
			<a href="http://localhost:5000"> Home </a>
			<br>
			<ul>
				<li> Open Account </li>
				<li> Close Account </li>
				<li> Mortages </li>
				<li> Make a deposit </li>
				<li> Make a withdrawal </li>
				<li> Make a compliant </li>
			</ul>
			</html>
			"""

app.run()