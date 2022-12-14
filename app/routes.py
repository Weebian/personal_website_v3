from flask import render_template, url_for, flash, redirect
from app import app
from sqlalchemy.ext.automap import automap_base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template(
        'index.html',
        title='Home'
    )

@app.route('/experience')
def experience():
    return render_template(
        'index.html',
        title='Home'
    )

@app.route('/education')
def education():
    return render_template(
        'index.html',
        title='Home'
    )

@app.route('/project')
def project():
    return render_template(
        'index.html',
        title='Home'
    )

@app.route('/tech')
def tech():
    return render_template(
        'index.html',
        title='Home'
    )

@app.route('/contact')
def contact():
    return render_template(
        'index.html',
        title='Home'
    )

@app.route('/resume')
def resume():
    return render_template(
        'index.html',
        title='Home'
    )