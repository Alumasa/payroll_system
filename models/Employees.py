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
    #read on keyword/default functions
    #update
    @classmethod
    def update_by_id(cls, id, name=None, gender=None, kraPin=None, email=None, nationalId=None, basicSalary=None, departmentId=None, benefits=None):
        record = cls.fetch_by_id(id=id)

        if name:
            record.name = name

        if gender:
            record.gender = gender

        if kraPin:
            record.kraPin = kraPin

        if email:
            record.email = email

        if nationalId:
            record.nationalId = nationalId

        if basicSalary:
            record.basicSalary = basicSalary

        if departmentId:
            record.departmentId = departmentId

        if benefits:
            record.benefits = benefits

        db.session.commit()
        return True

    #delete
    @classmethod
    def delete_by_id(cls,id):
        record = cls.query.filter_by(id=id)
        record.delete()
        db.session.commit()
        return True