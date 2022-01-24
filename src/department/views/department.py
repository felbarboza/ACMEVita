from flask_classful import FlaskView, route
from flask import request

from src.department.services.DepartmentService import DepartmentService


class DepartmentView(FlaskView):
  @route('/', methods=['GET', 'POST'])
  def run(self):
    if(request.method=='POST'):
      data = request.get_json()
      name = data['name']
      service = DepartmentService()
      new_department = service.create(name)
      return {"Message": "Departamento criado com sucesso!",
              "Departamento": {"id": new_department.id,
                              "name": new_department.name}}
    else:
      service = DepartmentService()
      departments = service.list()
      return departments

