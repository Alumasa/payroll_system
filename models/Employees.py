from main import db

class EmployeesModel(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    gender = db.Column(db.String(10), nullable=False)
    kraPin = db.Column(db.String(12), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    nationalId = db.Column(db.String(50), unique=True, nullable=False)
    departmentId = db.Column(db.Integer, db.ForeignKey('departments.id'))
    basicSalary = db.Column(db.Float)
    benefits = db.Column(db.Float)

    def insert2DB(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def fetch_by_id(cls, id):
        return cls.query.filter_by(id=id).first()