#!/bin/python3

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) # methods=["GET"] defualt
def index():
	if request.method == "GET":
		return render_template("index.html")
	if request.method == "POST": # submitting a form uses POST
		return render_template("greet.html", name=request.form.get("name", "name Submission missing"))

#@app.route("/greet", methods=["POST"])
#def greet():
#	return render_template("greet.html", name=request.form.get("name", "defualt"))
	#render_template(request.form, is asking for name in greet.html)
	#render_template(request.args, is asking for name in address bar)

if __name__ == "__main__":
	app.run()
