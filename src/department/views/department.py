from flask_classful import FlaskView, route
from flask import request
from src.department.services.create_department_service import create_department_service

from ..services.list_all_departments_service import list_all_departments_service
from ... import app

class DepartmentView(FlaskView):
  @route('/', methods=['GET', 'POST'])
  def run(self):
    if(request.method=='POST'):
      data = request.get_json()
      name = data['name']
      new_department = create_department_service(name)
      return {"Message": "Departamento criado com sucesso!",
              "Departamento": {"id": new_department.id,
                              "name": new_department.name}}
    else:
      # return {"message": "oi"}
      departments = list_all_departments_service()
      return departments

  # @route('/', methods=['POST'])
  # def create_department(self):
  #   return {"message": "oi"}
    


DepartmentView.register(app, route_base='/departments/')