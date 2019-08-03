# importing Flask class
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import Development

# instantiating or creating an object of class Flask
app: Flask = Flask(__name__)
# this is a config parameter that shows where our database lives, we are at development
#app.config.from_object(Development)
# app.config.from_object(Testing)
app.config.from_object(Production)

db = SQLAlchemy(app)
# to create tables in the database
from models.Employees import EmployeesModel
from models.Departments import DepartmentModel

#TODO:Read flask-migrate
# this decorator will tell flask to run this function before any other route
@app.before_first_request
def create_tables():
    db.create_all()
    #db.drop_all()

@app.route('/employees/<int:dept_id>')
def employees(dept_id):
    departments = DepartmentModel.fetch_all()
    return render_template('employees.html', departments=departments)


# registering a route
@app.route('/')
def hello_world():
    departments = DepartmentModel.fetch_all()
    return render_template('website.html', departments=departments)


@app.route('/newDepartment', methods=['POST'])
# function to run when clients visit this route
def newDepartment():
    department_name = request.form['department']
    if DepartmentModel.fetch_by_name(department_name):
        # read more on bootstrap alerts with flash
        flash("Department " + department_name + " already exists.")  # now create the alerts with flash.
        return redirect(url_for('hello_world'))
    department = DepartmentModel(name=department_name)
    department.insert2DB()
    return redirect(url_for('hello_world'))


@app.route('/newEmployee', methods=['POST'])
# function to run when clients visit this route
def newEmployee():
    name_of_employee = request.form['name']
    department_id = request.form['department']


# run Flask
# if __name__ == '__main__':
#   app.run()

@app.route('/name')
def name():
    return 'Vanessa Alumasa'
