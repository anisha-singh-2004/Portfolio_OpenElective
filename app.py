#from template import index
#from static import info
from flask import Flask, render_template,request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('travel_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS travel (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    placeVisited TEXT,
                    duration TEXT,
                    purpose TEXT,
                    travelExpenses TEXT
                )''')
    conn.commit()
    conn.close()

# Initialize the database when the application starts
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    place_visited = request.form['placeVisited']
    duration = request.form['duration']
    purpose = request.form['purpose']
    travel_expenses = request.form['travelExpenses']
    
    conn = sqlite3.connect('travel_data.db')
    c = conn.cursor()
    c.execute('''INSERT INTO travel (placeVisited, duration, purpose, travelExpenses)
                 VALUES (?, ?, ?, ?)''', (place_visited, duration, purpose, travel_expenses))
    conn.commit()
    conn.close()
    
    return 'Data saved successfully.'


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/about_me")
def about():
    return render_template("about_me.html")

@app.route("/about_me/project")
def project():
    return render_template("project.html")
        

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/email_phone_number")
def phml():
    return render_template("phml.html")

@app.route("/resume")
def res():
    return render_template("resume.html")

@app.route("/profile")
def pro():
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(debug=True, port=7000)
