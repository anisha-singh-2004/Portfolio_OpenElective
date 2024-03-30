from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///hhh.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Travel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placeVisited = db.Column(db.String(100),nullable=False)
    duration = db.Column(db.String(100),nullable=False)
    purpose = db.Column(db.String(100))
    travelExpenses = db.Column(db.String(100))


    def __repr__(self)->str:
        return f"Travel('{self.placeVisited}', '{self.duration}', '{self.purpose}', '{self.travelExpenses}')"
    
with app.app_context():
    db.create_all()
    
@app.route('/submit', methods=[ 'GET','POST'])
def pro():
    if request.method == 'POST':
        place_visited = request.form['placeVisited']
        duration = request.form['duration']
        purpose = request.form['purpose']
        travel_expenses = request.form['travelExpenses']
        
        new_travel = Travel(placeVisited=place_visited, duration=duration, purpose=purpose, travelExpenses=travel_expenses)
        db.session.add(new_travel)
        db.session.commit()
        
        return render_template('saved.html')
    return render_template('profile.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route("/about_me")
def about():
    return render_template("about_me.html")

@app.route("/about_me/project")
def project():
    return render_template("project.html")
        
@app.route('/profile/display_travels')
def display_travels():
    travels = Travel.query.all()  
    return render_template('display_travels.html', travels=travels)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/email_phone_number")
def phml():
    return render_template("phml.html")

@app.route("/resume")
def res():
    return render_template("resume.html")

if __name__ == "__main__":
    app.run(debug=True, port=7000)
