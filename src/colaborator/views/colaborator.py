from flask_classful import FlaskView, route
from flask import request

from src.colaborator.services.create_new_colaborator_service import create_new_colaborator_service
from src.colaborator.services.list_department_colaborators_service import list_department_colaborators_service
from ... import app

class ColaboratorView(FlaskView):
  @route('/', methods=['POST'])
  def create_colaborator(self):
    data = request.get_json()
    full_name = data['full_name']
    dependents = data['dependents']
    department_id = data['department_id']

    new_colaborator =  create_new_colaborator_service(full_name, dependents, department_id)

    return new_colaborator

  @route('/list_by_deparment_id/<int:department_id>', methods=['GET'])
  def list_by_department(self, department_id):
    departments_colaboratos =  list_department_colaborators_service(department_id)

    return departments_colaboratos

ColaboratorView.register(app, route_base='/colaborators')