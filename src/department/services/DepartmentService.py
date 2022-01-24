from src.department.models.department import Department
from main import db
from flask import jsonify

class DepartmentService():
  def create(self, name):
    new_department = Department(name)
    db.session.add(new_department)
    db.session.commit()
    return new_department

  def list(self):
    departments = Department.query.all()
    departments_name_list = []
    for department in departments:
              departments_name_list.append(department.name)
    return jsonify({"departmens": departments_name_list})
