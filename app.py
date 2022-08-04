from flask import Flask, redirect, render_template,request, url_for,flash
import sqlite3
import db
app = Flask(__name__)
app.config['SECRET_KEY']='SK'
@app.route('/')
def index():
    return render_template('base.html')


@app.route('/signUp',methods=['POST','GET'])
def signUp():
    if request.method=="POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        repPassword = request.form['repPassword']
        connect = sqlite3.connect('Database.db')
        if password==repPassword:
            connect.execute(f"""INSERT INTO Users (Name,Email,Password) VALUES('{name}','{email}','{password}');""")
            connect.commit()
            db.close_db(connect) 
            return redirect(url_for('index'))
        else:
            flash("Password doesn't match!!")  
            return render_template('SignUp.html') 

        
    else:
        return render_template('SignUp.html')

@app.route('/signIn',methods=['POST','GET'])
def signIn():
    if request.method=='POST':

        email = request.form['email']
        password = request.form['password']
        connect = sqlite3.connect('Database.db')
        row=connect.execute(f"select Email,Password where email='{email}'")
        db.close_db(connect)
        if row != None:
            redirect(url_for('index'))
        else:
            return render_template('SignIn.html')
    else:
        return render_template('SignIn.html')