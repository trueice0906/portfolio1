from flask import Flask,render_template,redirect
from flask import request
import csv

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')

def write_to_csv(data):
    with open('database.csv',newline='',mode='a') as database:
        name=data['name']
        email=data['email']
        subject=data['subject']
        message=data['message']
        csv.writer = csv.writer(database,delimiter=',',quotechar='_',quoting=csv.QUOTE_MINIMAL)
        csv.writer.writerow([name,email,subject,message])

@app.route('/submit_form',methods=["POST","GET"])
def submit_form():
    if request.method == "POST":
        try:
            data=request.form.to_dict()
            write_to_csv(data)
            return redirect('/#contact')

        except:
            return "did not save to database"

    else:
        return "Something went wrong.try again."