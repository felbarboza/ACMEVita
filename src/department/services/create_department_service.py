from ..models.department import Department
from main import db

def create_department_service(name):
  new_department = Department(name)
  db.session.add(new_department)
  db.session.commit()
  return new_department