from flask import render_template,request,redirect,url_for
from . import main

#Views
@main.route("/")
@main.route("/home")
def index():

  '''
  View root page function that returns the index page and its data
  '''
  title = 'Break Time!!'


  return render_template('index.html')
