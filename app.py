from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

CSV_FILE = 'add_users.csv'
CSV_HEADER = ['EventID','EventName','Location','Description','ContactInfo']



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addevent')
def add_user():
    return render_template('addevent.html')

@app.route('/submitEvent', methods=['POST'])
def submit():
    form_data = request.form.to_dict() #This puts all the data from post into a dictionary
    print(form_data)
    with open('add_users.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, CSV_HEADER)
        writer.writerow(form_data)
   
    return f"<h1>Information: <br>Entered Event"# = {form_data.} <br>Password = {password} <br>First Name = {first_name} <br>Last Name = {last_name} <br>Email = {email}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
