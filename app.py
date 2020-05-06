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
    
    emp_count = int(request.form.get("number_of_employees"))
    return render_template('form.html', emp_count= emp_count)
    

@app.route("/results", methods=["POST"])
def results():
    tips_to_split = request.form.get("tip_pool")
    hours_worked = request.form.getlist("number_of_hours")
    print(hours_worked)


    return render_template("results.html",tips_to_split = tips_to_split, hours_worked = hours_worked )



    
if __name__ == "__main__":
    app.run(debug=True)