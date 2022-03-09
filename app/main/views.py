from flask import render_template, request
from . import main
from ..models import User
from app import db

@main.route('/', methods=['GET', 'POST'])
def index():
  heading = 'This is TakeThou'

  username = request.args.get('username') # None

  if username:
    username = request.args.get('username')
    firstname = request.args.get('firstname')
    email = request.args.get('email')
    age = request.args.get('age')
    
    user = User(username= username, firstname=firstname, email=email, age=age)
    db.session.add(user)
    db.session.commit()
    print('*'*30)
    print('Saved')
    print('*'*30)

  
  allusers = User.query.all()
  print(allusers)


  return render_template('index.html', heading=heading, allusers=allusers)