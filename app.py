from flask import flask 

app = flask (__name__)

@app.route("/info")
def lwinfo()
	return "I AM LW FROM INDIA"
@app.route("/phone")
def lwphone():
	return "9823646434"
app.run(host="0.0.0.0")