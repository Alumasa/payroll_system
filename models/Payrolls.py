from main import db
from models.Employees import EmployeesModel

class PayrollsModel(db.Model):
    __tablename__ = 'payrolls'
    id = db.Column(db.Integer, primary_key=True)
    gross_salary = db.Column(db.Float)
    personal_relief = db.Column(db.Float)
    taxable_income = db.Column(db.Float)
    overtime = db.Column(db.Float)
    loan_deducted = db.Column(db.Float)
    advance_pay = db.Column(db.Float)
    month = db.Column(db.String(20), nullable=False)
    PAYE = db.Column(db.Float)
    NSSF = db.Column(db.Float)
    NHIF = db.Column(db.Float)
    net_salary = db.Column(db.Float)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))

    def insert2DB(self):
        db.session.add(self)
        db.session.commit()

#save a payroll record inside a database
