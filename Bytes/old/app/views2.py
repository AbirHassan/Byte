from flask import render_template
from app import app

@app.route('/search')

def search():
    return render_template("search.html")
