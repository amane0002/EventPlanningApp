from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

# --- Configuration and Setup ---
# Corrected header based on events.csv structure
CSV_HEADER = ['EventID', 'Category', 'Date', 'Price', 'EventName', 'Location', 'Description', 'ContactInfo']
EVENT_FILE = 'events.csv' 

# Initialize CSV file if it doesn't exist to ensure the header is present
if not os.path.exists(EVENT_FILE):
    with open(EVENT_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(CSV_HEADER)

# --- Helper Function: Read Events from CSV ---
def get_events():
    """Reads all events from the CSV file."""
    events = []
    if os.path.exists(EVENT_FILE):
        try:
            with open(EVENT_FILE, 'r', newline='', encoding='utf-8') as csvfile:
                # DictReader reads each row as a dictionary
                reader = csv.DictReader(csvfile)
                events = list(reader)
        except Exception as e:
            print(f"Error reading CSV file: {e}")
    return events


@app.route('/')
def index():
    # This route renders the simple index.html
    return render_template('index.html')

@app.route('/addevent')
def add_event():
    # This route renders the add event form
    return render_template('addevent.html')

@app.route('/submitEvent', methods=['POST'])
def submitEvent():
    form_data = request.form.to_dict()

    # Create a dictionary that ensures all CSV_HEADER fields are present
    row_data = {key: form_data.get(key, '') for key in CSV_HEADER}

    try:
        with open(EVENT_FILE, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=CSV_HEADER)
            writer.writerow(row_data)
        
        # Redirect after POST to the new event finding page
        return redirect(url_for('find')) 
        
    except Exception as e:
        return f"<h1>Error writing to CSV: {e}</h1>"

# --- New Route to render find.html and show ALL events ---
@app.route('/find')
def find():
    # 1. Get all events
    events = get_events()
    
    # 2. Render find.html, passing data for initial display
    return render_template('findtemp.html', events=events, headers=CSV_HEADER)

if __name__ == '__main__':
    app.run(debug=True)