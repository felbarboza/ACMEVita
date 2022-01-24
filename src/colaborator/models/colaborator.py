from src.department.models.department import Department
from src import db

class Colaborator(db.Model):
  __tablename__="colaborators"
  id=db.Column(db.Integer, primary_key=True)
  full_name = db.Column(db.String(255), nullable=False)
  department_id = db.Column(db.Integer, db.ForeignKey(Department.id), nullable=False)
  dependents_number = db.Column(db.Integer, nullable=False)
 
  
  def __init__(self, full_name, department_id, dependents):
    self.full_name=full_name
    self.department_id=department_id
    if(type(dependents)==int):
      self.dependents_number = dependents
    