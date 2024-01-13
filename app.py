from flask import Flask,  render_template, request, jsonify
import sqlite3
import re

# Configure application
app = Flask(__name__)


# The home page.
@app.route('/')
def index():
    return render_template('index.html')

   

def createTableIfNotExists():
    with sqlite3.connect('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS tasks ( \
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                column TEXT NOT NULL,\
                title TEXT NOT NULL,\
                body TEXT NOT NULL);'
                )
        connection.commit()
    
    



  





