# importing Flask class
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from resources.payroll_system import KRACalculator as Payroll
from config import Development

# instantiating or creating an object of class Flask
app = Flask(__name__)

#app.config.from_object(Production)
app.config.from_object(Development)


db = SQLAlchemy(app)
# to create tables in the database
from models.Employees import EmployeesModel
from models.Departments import DepartmentModel
from models.Payrolls import PayrollsModel

#TODO:Read flask-migrate
# this decorator will tell flask to run this function before any other route
@app.before_first_request
def create_tables():
    db.create_all()
    #db.drop_all()

@app.route('/employees/<int:dept_id>')
def employees(dept_id):
    this_department = DepartmentModel.fetch_by_id(dept_id)
    departments = DepartmentModel.fetch_all()
    return render_template('employees.html', this_department=this_department, departments=departments)


# registering a route
@app.route('/')
def hello_world():
    departments = DepartmentModel.fetch_all()
    return render_template('website.html', departments=departments)

@app.route('/generate_payroll/<int:id>', methods=['POST'])
def generate_payroll(id):
    this_employee = EmployeesModel.fetch_by_id(id)
    payroll = Payroll(this_employee.name, this_employee.basicSalary, this_employee.benefits)
    NHIF = payroll.NHIF
    NSSF = payroll.NSSF
    PAYE = payroll.PAYE
    net_salary = payroll.net_salary
    gross_salary = payroll.gross_salary
    personal_relief = payroll.personal_relief
    taxable_income = payroll.taxable_income
    month = request.form['month']
    payrolls = PayrollsModel(NHIF=NHIF, NSSF=NSSF, PAYE=PAYE, month=month, net_salary=net_salary, gross_salary=gross_salary, personal_relief=personal_relief, taxable_income=taxable_income, employee_id=id)
    payrolls.insert2DB()
    return redirect(url_for('hello_world'))


@app.route('/editEmployee/<int:id>', methods=['POST'])
def editEmployee(id):
    name_of_employee = request.form['name']
    department_id = int(request.form['department'])
    gender = request.form['gender']
    basic_salary = request.form['basic_salary']
    benefits = request.form['benefits']
    kra_pin = request.form['kra_pin']
    national_id = request.form['national_id']
    email = request.form['email']

    if gender == "na":
        gender = None
    if department_id == "0":
        department_id = None

    EmployeesModel.update_by_id(id=id, name=name_of_employee, departmentId=department_id,gender=gender, basicSalary=basic_salary, benefits=benefits, kraPin=kra_pin, email=email, nationalId=national_id)
    this_emp = EmployeesModel.fetch_by_id(id=id)
    this_dept = this_emp.department
    return redirect(url_for('employees', dept_id = this_dept.id))

@app.route('/deleteEmployee/<int:id>')
def deleteEmployee(id):
    this_emp = EmployeesModel.fetch_by_id(id=id)
    this_dept = this_emp.department
    EmployeesModel.delete_by_id(id)
    return redirect(url_for('employees', dept_id=this_dept.id))

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
    department_id = int(request.form['department'])
    gender = request.form['gender']
    basic_salary = request.form['basic_salary']
    benefits = request.form['benefits']
    kra_pin = request.form['kra_pin']
    national_id = request.form['national_id']
    email = request.form['email']
    emp = EmployeesModel(name=name_of_employee, gender=gender, kraPin=kra_pin, departmentId=department_id, basicSalary=basic_salary, benefits=benefits, nationalId=national_id, email=email)
    emp.insert2DB()
    return redirect(url_for('hello_world'))


@app.route('/payrolls/<int:emp_id>')
def payrolls(emp_id):
    employee = EmployeesModel.fetch_by_id(emp_id)
    return render_template('payrolls.html', employee=employee)

# run Flask
# if __name__ == '__main__':
#   app.run()

@app.route('/name')
def name():
    return 'Vanessa Alumasa'
