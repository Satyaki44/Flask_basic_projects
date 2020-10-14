import flask
import sqlite3
from flask import Flask,redirect,url_for,render_template,request
app = Flask(__name__)





@app.route("/")
def home():
    return "Welcome to the home Page!!"

@app.route('/login',methods = ["POST","GET"])
def login():
    while True:
        if request.method =="POST":
            user=request.form["nm"]
        
            connection=sqlite3.connect("test.db")
            c=connection.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS customers (
            name1 text,
            name2 text,
            name3 text
            )""")
            
            c.execute("INSERT INTO test VALUES ('{n}')".format(n=user))
            connection.commit()
            connection.close()

            return redirect(url_for("user",usr=user))
        elif request.method == "GET":
            return render_template("form.html")

@app.route("/<usr>")
def user(usr):
    return f"<h2>{usr}</h2>"
app.run(debug=True)