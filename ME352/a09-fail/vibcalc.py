from flask import Flask, render_template, url_for, request
from forms import Inputs

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
@app.route("/home", methods = ['GET', 'POST'])
def home():
	form = Inputs()
	return render_template("home.html", form=form)

@app.route("/about")
def about():
	return render_template("about.html")

if __name__ == '__main__':
	app.run(debug = True)