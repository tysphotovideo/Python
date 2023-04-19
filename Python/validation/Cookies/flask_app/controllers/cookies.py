from flask import Flask,render_template,redirect,request,session
from flask_app import app
from flask_app.models.cookie import Cookies

@app.route("/")
def index():
    return redirect('/cookies')
@app.route("/cookies")
def cookies():
    

    return render_template("index.html", cookies=Cookies.get_all())
@app.route("/cookies/new")
def newCookie():
   

    return render_template("new_order.html")
@app.route("/cookies/create", methods=['POST'])
def create():
    if not Cookies.validate_cookie(request.form):
        return redirect('/cookies/new')
    print(request.form)
    Cookies.save(request.form)
    return redirect("/cookies")
@app.route('/cookies/<int:id>/edit')
def edit(id):
    data={
        'id':id
    }
    
    return render_template('/update.html',cookie = Cookies.getOne(data))

@app.route("/cookies/update", methods=['POST'])
def update():
    if not Cookies.validate_cookie(request.form):
        return redirect(f"/cookies/{request.form['id']}/edit")
    Cookies.update(request.form)
    return redirect("/cookies")