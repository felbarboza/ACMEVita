from ..models.colaborator import Colaborator
from flask import jsonify

def list_department_colaborators_service(department_id):
  colaborators = Colaborator.query.filter(Colaborator.department_id==department_id)
  colaborator_list = []
  
  for colaborator in colaborators:

    if(colaborator.dependents_number>1):
      have_dependents=True
    else:
      have_dependents=False

    colaborator_list.append({
        "full_name": colaborator.full_name,
        "have_dependents": have_dependents 
        })



  return jsonify({"colaborators": colaborator_list})