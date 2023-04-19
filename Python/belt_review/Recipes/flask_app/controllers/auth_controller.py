from flask import session, request, render_template, redirect, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models import artist
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)



@app.route("/register", methods=["GET"])
def register_form():
    return render_template("auth/register.html")


@app.route("/register", methods=["POST"])
def create_user():

    if not User.validate_user(request.form):
        return redirect('/register')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id

    return redirect('/dashboard')

@app.route('/login', methods=['GET'])
def login_form():
    return render_template("auth/login.html")


@app.route('/login', methods=['POST'])
def login_authenticate():
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/login")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/login')
    
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")
@app.route("/logout")
def logout():
    session.clear()
    return redirect('/login')

@app.route('/dashboard', methods= ['GET'])
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    return redirect('/recipes')