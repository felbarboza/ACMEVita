from flask_classful import FlaskView, route
from flask import request

from src.colaborator.services.ColaboratorService import ColaboratorService

class ColaboratorView(FlaskView):
  @route('/', methods=['POST'])
  def create_colaborator(self):
    data = request.get_json()
    full_name = data['full_name']
    dependents = data['dependents']
    department_id = data['department_id']
    service = ColaboratorService()
    new_colaborator =  service.create(full_name, dependents, department_id)

    return new_colaborator

  @route('/list_by_deparment_id/<int:department_id>', methods=['GET'])
  def list_by_department(self, department_id):
    service = ColaboratorService()
    departments_colaboratos = service.list(department_id)

    return departments_colaboratos

