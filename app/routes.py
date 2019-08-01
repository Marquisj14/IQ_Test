from app import app
from flask import render_template, request
from app.models import model, formopener
# from model import questions

@app.route('/')
@app.route('/index')
def index():
    
    return render_template("index.html")

@app.route('/questions')

def template():
    return render_template("template.html", questions = model.questions)
    
        # TODO: write code...
@app.route('/results' , methods = ['GET' , 'POST'])
def results():
    score = 50
    message=""
    
    userdata=dict(request.form)
    print (userdata)
    widow=userdata["widow"]
    print (widow)
    bat=userdata["bat"]
    print (bat)
    forest=userdata["forest"]
    print (forest)
    july=userdata["july"]
    print (july)
    race=userdata["race"]
    print(race)
    bicycles=userdata["bicycles"]
    print(bicycles)
    height=userdata["height"]
    print(height)
    family=userdata["family"]
    print(family)
    Math=userdata["Math"]
    print(Math)
    Days=userdata["Days"]
    print(Days)
    
    if widow== "no":
        score+=10
        
    if bat== "5 cents":
        score+=20
        
    if forest== "Leaf":
        score+= 10
        
    if july== "Yes":
        score+=10
    
    if race=="2nd":
        score+=10
        
    if bicycles=="4 people":
        score+=20
            
    if height=="It is impossible to tell whether Bill or Peter is taller":
        score+=15
        
    if family=="Bob":
        score+=10
        
    if Math=="70":
        score+=20
        
    if Days=="12":
        score+=10
    
     
    if score>= 130 :
        message= "Extremely high!What a genious!Aren't you proud of yourself?"
        
    elif score >= 120:
        message="very high! outstanding performance "
        
    elif score >= 100:
        message="High average! You're very talented! ?"
        
    elif score >= 90:
         message="Average!You're doing a good job"
        
    elif score >= 80:
        message="Low average. "
        
    elif score >= 70:
        message="very low"
        
    elif score >= 69 :
        message="Extremely low. "
    
    return render_template('results.html', score=score, message=message)
    