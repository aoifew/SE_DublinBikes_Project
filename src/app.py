# Import necessary packages
from flask import Flask, g, render_template, jsonify
import sqlite3

# Indicate that file is flask apps
app = Flask(__name__)

# Assign database
DATABASE = ('dublinbikes.sqlite')

def connect_to_database():
    '''Function to connect to database'''
    
    return sqlite3.connect(DATABASE)

def get_db():
    '''Function to get database contents'''
    
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

@app.teardown_appcontext
def close_connection(exception):
    '''Function to close database connection'''
    
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def main():
    '''Function to render .html file as webpage'''
    
    return render_template("index.html")

@app.route("/json")
def get_results():
    '''Function with specific SQL query for webpage'''
    
    # Create object to connect to database
    cur = get_db().cursor()
    # Query database
    for row in cur.execute("SELECT dublinbike_id, name, bike_stands, available_bikes, position_lat, position_long, available_bike_stands, status FROM dublinbikes WHERE dublinbike_id>251692 AND dublinbike_id<251794;"):
        # create dictionary for db results
        entries = [dict(dublinbike_id=row[0], name=row[1], bike_stands=row[2], available_bikes=row[3], position_lat=row[4], position_long=row[5], available_bike_stands=row[6], status=row[7]) for row in cur.fetchall()]
    # Convert to JSON format
    return jsonify(results=entries)

# Run
if __name__ == "__main__":
    app.run(debug=True)