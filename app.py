from flask import Flask, render_template, redirect, session, url_for, request, jsonify, flash, url_for, abort 
from surveys import surveys


app = Flask(__name__)
app.config["SECRET_KEY"] = "abc123"

RESPONSES_KEY = "responses"


@app.route("/")
def start_page():
    session[RESPONSES_KEY] = []
    return render_template("start_page.html")

# accepts a number as a parameter that coincides with a question and passes it to template
# saves survey questions in a variable passes it to template
@app.route("/questions/<int:nums>")
def questions(nums):

    

    param = nums
    print(nums)
    q1 = [q.question for q in surveys["satisfaction"].questions][0]
    q2 = [q.question for q in surveys["satisfaction"].questions][1]
    q3 = [q.question for q in surveys["satisfaction"].questions][2]
    q4 = [q.question for q in surveys["satisfaction"].questions][3]
        
    return render_template("questions.html", param=param, q1=q1,q2=q2,q3=q3,q4=q4)


# receives answers from forms and saves responses
@app.route("/answers", methods = ["POST"])
def answers():

    choice = request.form["choice"]
    responses = session.get(RESPONSES_KEY,[])
    responses.append(choice)
    session[RESPONSES_KEY] = responses
    print(responses)
    
    if (len(responses) == len(surveys["satisfaction"].questions)):
        
        return render_template("/end.html")

    else:
        return redirect(f"/questions/{len(responses)}")
    
 
    

