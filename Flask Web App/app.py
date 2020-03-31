from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("layout.html")

@app.route("/two")
def two():
	return render_template("two.html")


@app.route("/three")
def three():
	return render_template("three.html")



if __name__ == "__main__":
	app.run(debug=True) # debug=True | allows you to leave the server up and running as you make changes to the site