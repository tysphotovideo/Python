from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.users import Users

@app.route("/")
def index():
    return redirect('/users')
@app.route("/users")
def users():
    

    return render_template("index.html", users=Users.get_all())
@app.route("/users/new")
def newUser():
   

    return render_template("new_user.html")
@app.route("/users/create", methods=['POST'])
def create():
    
    print(request.form)
    Users.save(request.form)
    return redirect("/users")
@app.route("/users/update", methods=['POST'])
def update():
    
    Users.update(request.form)
    return redirect("/users")
@app.route('/users/delete/<int:id>')
def delete(id):
    data ={
        "id":id 
    }
    Users.delete(data)
    return redirect('/users')
@app.route('/users/<int:id>')
def user(id):
    data ={
        "id":id 
    }
    return render_template('/user.html',user=Users.getOne(data))
@app.route('/users/<int:id>/edit')
def edit(id):
    data ={
        "id":id 
    }
    
    return render_template('/update.html',user=Users.getOne(data))
