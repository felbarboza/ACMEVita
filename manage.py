from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.colaborator.models.colaborator import Colaborator
from src.department.models.department import Department
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://docker:docker@localhost:5432/docker'


db = SQLAlchemy(app)

    
class Department(db.Model):
  __tablename__="departments"
  id=db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)

class Colaborator(db.Model):
  __tablename__="colaborators"
  id=db.Column(db.Integer, primary_key=True)
  full_name = db.Column(db.String(255), nullable=False)
  department_id = db.Column(db.Integer, db.ForeignKey(Department.id), nullable=False)
  dependents_number = db.Column(db.Integer, nullable=False)
 
db.create_all()