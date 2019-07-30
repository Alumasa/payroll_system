# importing Flask class
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Development
#instantiating or creating an object of class Flask
app = Flask(__name__)
# this is a config parameter that shows where our database lives, we are at development
app.config.from_object(Development)
#app.config.from_object(Testing)

db = SQLAlchemy(app)
#to create tables in the database
from models.Employees import EmployeesModel
from models.Departments import DepartmentModel

@app.before_first_request
def create_tables():
    db.create_all()


# registering a route
@app.route('/')
# function to run when clients visit this route
def hello_world():
    return render_template('website.html')

# run Flask
#if __name__ == '__main__':
 #   app.run()

@app.route('/name')
def name():
    return 'Vanessa Alumasa'