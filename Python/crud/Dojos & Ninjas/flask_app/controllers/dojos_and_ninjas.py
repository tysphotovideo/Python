from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.dojos import Dojos
from flask_app.models.ninjas import Ninjas
from flask_app.models import dojos, ninjas


@app.route("/")
def index():
    return redirect('/dojos')
@app.route("/dojos")
def dojo():
   dojos = Dojos.get_all()
   return render_template("new_dojo.html",all_dojos = dojos)
@app.route("/ninjas")
def ninja():
    

    return render_template("index.html", dojos= Dojos.get_all())
@app.route("/ninjas/new")
def newNinja():
   

    return render_template("new_ninja.html", dojos= Dojos.get_all())
@app.route("/dojos/new")
def newDojo():
   

    return render_template("new_dojo.html")
@app.route("/ninjas/create", methods=['POST'])
def create():
    
    print(request.form)
    Ninjas.save(request.form)
    return redirect("/dojos")
@app.route("/ninjas/update", methods=['POST'])
def update():
    
    Ninjas.update(request.form)
    return redirect("/ninjas")
@app.route('/ninjas/delete/<int:id>')
def delete(id):
    data ={
        "id":id 
    }
    Ninjas.delete(data)
    return redirect('/ninjas')
@app.route('/ninjas/<int:id>')
def ninjas(id):
    data ={
        "id":id 
    }
    return render_template('/ninja.html',ninja=Ninjas.getOne(data))
@app.route('/ninjas/<int:id>/edit')
def edit(id):
    data ={
        "id":id 
    }
    
    return render_template('/update_ninja.html',ninja=Ninjas.getOne(data))
@app.route("/dojos/create", methods=['POST'])
def createDojo():
    
    print(request.form)
    Dojos.save(request.form)
    return redirect("/dojos")
@app.route("/dojos/update", methods=['POST'])
def updateDojo():
    
    Dojos.update(request.form)
    return redirect("/dojos")
@app.route('/dojos/delete/<int:id>')
def deleteDojo(id):
    data ={
        "id":id 
    }
    Dojos.delete(data)
    return redirect('/dojos')
@app.route('/dojos/<int:id>')
def d(id):
    data ={
        "id":id 
    }
    return render_template('/dojos.html',dojo=Dojos.get_one_with_ninjas(data))
@app.route('/dojos/<int:id>/edit')
def editDojo(id):
    data ={
        "id":id 
    }
    
    return render_template('/update_dojo.html',dojos=Dojos.get_one_with_ninjas(data))
