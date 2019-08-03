class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "some_secret"
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@127.0.0.1:5432/payroll_system'
    environment = 'Development'
    DEBUG = True


class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@127.0.0.1:5432/payroll_system'
    environment = 'Development'
    DEBUG = True

class Testing(Config):
    #SQLALCHEMY_DATABASE_URI = ''
    DEBUG = False

class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'postgres://yntawkyhuiplmp:dbfc0c40b23339d0c187d19e5a5ec4df2b9144821bfb464d62738659fc87f22a@ec2-54-221-215-228.compute-1.amazonaws.com:5432/d8rae8th2666rk'
    DEBUG = False
    environment = 'Production'