from flask import render_template, request, redirect,session
from flask_app import app
from flask_app.models import sighting
from flask_app.models.user import User

@app.route("/sightings")
def get_all_sightings():
    data ={
        'id': session['user_id']
    }
    # dats ={
    #     'id': artist.Artist.get_one()
    # }
    all_sighting = sighting.Sighting.get_one_with_user(data)
    user = User.get_one(data)
    return render_template("sightings/sightings.html", sightings = all_sighting, user=user)

@app.route("/sightings/<int:sas_id>")
def view_artist(sas_id):
    data ={
        'id': session['user_id']
    }
    
   
    user = User.get_one(data)
    sight = sighting.Sighting.get_one(sas_id)
    sights = sighting.Sighting.get_one_with_user(data)
    return render_template("sightings/view_sightings.html", sight = sight, sights=sights, user=user)

@app.route("/sightings/new", methods=["GET"])
def create_artist_form():
    data ={
        'id': session['user_id']
    }
    user = User.get_one(data)
    return render_template("sightings/report_sighting.html",user=user )

@app.route("/sightings", methods=["POST"])
def create_sighting():
    if not sighting.Sighting.validate_sighting(request.form):
        return redirect('/sightings/new')
    sighting.Sighting.create_sighting(request.form)
    return redirect("/sightings")


@app.route("/sightings/<int:sas_id>/edit")
def edit_sighting(sas_id):
    
    data ={
        'id': session['user_id']
    }
    user = User.get_one(data)
    sight = sighting.Sighting.get_one(sas_id)
    return render_template("sightings/edit_sighting.html", sight=sight, user=user)

@app.route("/sightings/<int:sas_id>/update", methods=["POST"])
def update_sighting(sas_id):
    
    data = {
        "id": sas_id,
        "location": request.form["location"],
        "what": request.form["what"],
        "date": request.form["date"],
        "num_sas": request.form["num_sas"],
    }
    if not sighting.Sighting.validate_sighting(request.form):
        return redirect(f'/sightings/{sas_id}/edit')
    
    sighting.Sighting.update_sighting(data)
    return redirect("/sightings")


@app.route("/sightings/<int:sas_id>/delete")
def delete_sighting(sas_id):
    sighting.Sighting.delete_sighting(sas_id)
    return redirect("/sightings")