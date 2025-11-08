from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

CSV_FILE = 'events.csv'
CSV_HEADER = ['EventID','Category','Date','Price''EventName','Location','Description','ContactInfo']



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addevent')
def add_event():
    return render_template('addevent.html')

@app.route('/submitEvent', methods=['POST'])
def submitEvent():
    form_data = request.form.to_dict() #This puts all the data from post into a dictionary
    print(form_data)
    with open('events.csv', 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, CSV_HEADER)
        writer.writerow(form_data)
   
    return f"<h1>Information: <br>Entered Event"# = {form_data.} <br>Password = {password} <br>First Name = {first_name} <br>Last Name = {last_name} <br>Email = {email}</h1>"

@app.route('/events/<category_name>')
def display_events():
    
    events = []
    try:
        with open("events.csv", 'r', newline='', encoding='utf-8') as csvfile:
            # Use DictReader to read rows as dictionaries, making them easier to handle
            reader = csv.DictReader(csvfile)
            events = list(reader)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        # Pass an empty list on failure
        events = []

    # headers is passed to the template for dynamic column names
    return render_template('eventviewtest.html', events=events, headers=CSV_HEADER)

if __name__ == '__main__':
    app.run(debug=True)
