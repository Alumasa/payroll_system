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
#this decorator will tell flask to run this function before any other route
@app.before_first_request
def create_tables():
    db.create_all()


# registering a route
"""@app.route('/newDepartment', methods=['POST'])
# function to run when clients visit this route
def newDepartment():
    pass
@app.route('/newEmployee', methods=['POST'])
# function to run when clients visit this route
def newEmployee():
    pass
    #return render_template('website.html')"""

# run Flask
#if __name__ == '__main__':
 #   app.run()

@app.route('/name')
def name():
    return 'Vanessa Alumasa'