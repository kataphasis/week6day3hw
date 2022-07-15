from flask import jsonify, request, flash, redirect
from . import bp as app
from app.blueprints.main.models import Car
from app import db

@app.route("/cars", methods=["CAR"])
def car_update():
    # Retrieve form data from request
    themake = request.form['make']
    themodel = request.form['model']
    theyear = request.form['year']
    thecolor = request.form['color']
    theprice = request.form['price']
    

    # Instantiate new post
    new_post = Car(make=themake, model=themodel, year=theyear, color=thecolor, price=theprice)

    # Add new post to the database
    db.session.add(new_post)
    db.session.commit()

    flash('New car added successfully', 'success')

    # Once the post is added to the database, send the user back to the homepage
    return redirect("http://127.0.0.1:5000/")