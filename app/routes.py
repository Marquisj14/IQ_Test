from app import app
from flask import render_template, request
from app.models import model, formopener
# from model import questions

@app.route('/')
@app.route('/index')
def index():
    
    return render_template("index.html")

@app.route('/questions' , methods = ['GET' , 'POST'])
def template():
    return render_template("template.html", questions = model.questions)
    
        # TODO: write code...
@app.route('/results' , methods = ['GET' , 'POST'])
def results():
    score = 0
    message=""
    
    userdata=dict(request.form)
    print(userdata)
    widow=userdata["widow"]
    print(widow)
    bat=userdata["bat"]
    print(bat)
    forest=userdata["forest"]
    print (forest)
    july=userdata["july"]
    print(july)
    race=userdata["race"]
    print(race)
    bicycles=userdata["bicycles"]
    print(bicycles)
    height=userdata["height"]
    print(height)
    family=userdata["family"]
    print(family)
    math=userdata["math"]
    print(math)
    days=userdata["days"]
    print(days)
    
    if widow== "No":
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
        score+=10
        
    if family=="Bob":
        score+=10
        
    if math=="70":
        score+=20
        
    if days=="12":
        score+=10
    
     
    if score>= 130 :
        message= "Extremely high! What a genious! Aren't you proud of yourself?"
        
    elif score >= 120:
        message="Very high! Outstanding Performance! "
        
    elif score >= 100:
        message="High average! You're very talented! "
        
    elif score >= 90:
         message="Average! Wanna try again?"
        
    elif score >= 80:
        message="Low average. I think you're doing okay! Don't give up! "
        
    elif score >= 70:
        message="Very Low. I believe you'll do good next time. Don't worry!"
        
    elif score >= 69 :
        message="Extremely low. Keep trying to get a better score! Good luck!"
    
    return render_template('results.html', score=score, message=message)
    