from flask import Flask, render_template, redirect
from flask_sqalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/fb-login', methods=["GET", "POST"])
def log():
    if request.method == "POST":
        login = request.form.get["login"]
        password = request.form.get["password"]
    else:
        return render_template("fblog.html")
