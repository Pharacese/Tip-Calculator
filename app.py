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
    hour_total = 0
    
    ind_tips = []
    #Here i need to do math
    # Pool = (Tips/Total hours of all servers) * Hour per server
    # Loop through the hours to add them together to get the total num of hours
    # Divide the tip pool by that
    # Multipy that value by each hour to get the amount received for each server
    for emp in hours_worked:
        hour_total += int(emp)
    
    tip_division = int(tips_to_split)/hour_total

    for emp in hours_worked:
        ind_tips.append(round(tip_division * int(emp)))
    
    print(hours_worked)

    hours_tips = zip(hours_worked,ind_tips)


    return render_template("results.html",tips_to_split = tips_to_split, hours_worked = hours_worked, hour_total = hour_total, tip_division = tip_division, ind_tips = ind_tips, hours_tips = hours_tips )



    
if __name__ == "__main__":
    app.run(debug=True)