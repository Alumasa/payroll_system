# importing the flask sqlalchemy object from app(main file)
from main import db
from models.Employees import EmployeesModel


class DepartmentModel(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    employees = db.relationship(EmployeesModel, backref='department')

    # created a new method
    def insert2DB(self):
        db.session.add(self)
        db.session.commit()

    #read
    #read more on classes-class method, instance method, static method
    @classmethod
    def fetch_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def fetch_by_id(cls, dept_id):
        return cls.query.filter_by(id=dept_id).first()

    @classmethod
    def fetch_all(cls):
        return cls.query.all()

    #bar-graphs
    @classmethod
    def fetch_total_payroll_by_id(cls, id):
        this_dept = cls.fetch_by_id(id)
        total_payroll = 0
        for each_employee in this_dept.employees:
            total_payroll += each_employee.basicSalary + each_employee.benefits
            return total_payroll



    #update
    @classmethod
    def update_by_id(cls, id, name=None):
        record = cls.fetch_by_id(id)

        if name:
            record.name = name

        db.session.commit()
        return True

    #delete
    @classmethod
    def delete_by_id(cls, id):
        record = cls.query.filter_by_id.first()
        db.session.delete(record)
        db.session.commit()
        return True