from flask import Flask, render_template, request

app = Flask(__name__)


cumulative_hours = 0
names_and_hours = {}



#Load page where the number of employees worked is logged.
#Should post data to a form where the names and hours are logged

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/form", methods=["POST"])
def form_fill():
    team_member_count = int(request.form.get("number_of_employees"))
    return render_template('form.html', team_member_count=team_member_count)
    

@app.route("/results", methods=["POST"])
def results():
    team_member_name = request.form.getlist("name[]")
    hours_worked = request.form.getlist("number_of_hours[]")
    return render_template("results.html", team_member_name = team_member_name, hours_worked = hours_worked)



    
if __name__ == "__main__":
    app.run(debug=True)