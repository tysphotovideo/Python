from flask import render_template, request, redirect,session
from flask_app import app
from flask_app.models import artist
from flask_app.models.user import User

@app.route("/recipes")
def get_all_artists():
    data ={
        'id': session['user_id']
    }
    # dats ={
    #     'id': artist.Artist.get_one()
    # }
    all_artists = artist.Artist.get_one_with_user(data)
    user = User.get_one(data)
    return render_template("artists/all_artists.html", artists = all_artists, user=user)

@app.route("/artists/<int:artist_id>")
def view_artist(artist_id):
    artist_record = artist.Artist.get_one(artist_id)
    return render_template("artists/view_artist.html", artist = artist_record)

@app.route("/artists/new", methods=["GET"])
def create_artist_form():
    data ={
        'id': session['user_id']
    }
    user = User.get_one(data)
    return render_template("artists/create_artist.html",user=user )

@app.route("/recipes", methods=["POST"])
def create_artist():
    if not artist.Artist.validate_recipe(request.form):
        return redirect('/artists/new')
    artist.Artist.create_artist(request.form)
    return redirect("/recipes")


@app.route("/artists/<int:artist_id>/edit")
def edit_artist(artist_id):
    data ={
        'id': session['user_id']
    }
    user = User.get_one(data)
    artist_record = artist.Artist.get_one(artist_id)
    return render_template("artists/edit_artist.html", artist=artist_record, user=user)

@app.route("/artists/<int:artist_id>/update", methods=["POST"])
def update_artist(artist_id):
    data = {
        "id": artist_id,
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "date_made": request.form["date_made"],
        "under": request.form["under"],
    }
    
    artist.Artist.update_artist(data)
    return redirect("/recipes")


@app.route("/artists/<int:artist_id>/delete")
def delete_artist(artist_id):
    artist.Artist.delete_artist(artist_id)
    return redirect("/recipes")