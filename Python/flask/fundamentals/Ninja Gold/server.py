from flask import Flask, render_template, session, request, redirect
from datetime import datetime
import random

app = Flask(__name__)   
app.secret_key = 'ninja gold'

@app.route('/')          
def index():
    if "ninja_gold" not in session:
        session["ninja_gold"] = 0
    
    if "activities" not in session: 
        session["activities"] = []
        
        
    activities = session["activities"]
    return render_template("index.html",activities=activities)  

@app.route('/process_money', methods=["POST"])
def process_money():
    location = request.form["location"]
    activities = session["activities"]
    if location == "farm":
        earnedValue = random.randint(10,20)
    elif location == "cave":
        earnedValue = random.randint(5,10)
    elif location == "house":
        earnedValue = random.randint(2,5)
    elif location == "casino":
        earnedValue = random.randint(-50,50)
        
    
    activities.append({
            "activityName": location,
            "earnedValue": earnedValue,
            "date": datetime.now()  
        })
    session["ninja_gold"] += earnedValue   
    session["activities"] = activities       
    
    return redirect("/")

if __name__=="__main__":   
    app.run(debug=True, port=5100)    

