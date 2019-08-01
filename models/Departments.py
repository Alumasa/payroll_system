# importing the flask sqlalchemy object from app(main file)
from app import db
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
    def fetch_all(cls):
        return cls.query.all()