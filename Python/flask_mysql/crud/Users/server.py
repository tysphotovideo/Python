from flask import Flask, render_template,redirect, request
# import the class from friend.py
from users import Users
app = Flask(__name__)
@app.route("/")
def index():
    return redirect('/users')
@app.route("/users")
def users():
    # call the get all classmethod to get all friends

    return render_template("index.html", users=Users.get_all())
@app.route("/users/new")
def newUser():
    # call the get all classmethod to get all friends

    return render_template("new_user.html")
@app.route("/users/create", methods=['POST'])
def create():
    # call the get all classmethod to get all friends
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


            
if __name__ == "__main__":
    app.run(debug=True, port=5100)

