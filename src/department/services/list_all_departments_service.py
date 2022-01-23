from ..models.department import Department
from flask import jsonify

def list_all_departments_service():
  departments = Department.query.all()
  departments_name_list = []
  for department in departments:
            departments_name_list.append(department.name)
  return jsonify({"departmens": departments_name_list})