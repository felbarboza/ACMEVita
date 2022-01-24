from src.colaborator.models.colaborator import Colaborator
from main import db
from flask import jsonify

class ColaboratorService():
  def create(self, full_name, dependents, department_id):
    new_colaborator = Colaborator(full_name=full_name, dependents=dependents, department_id=department_id)

    db.session.add(new_colaborator)
    db.session.commit()

    response = jsonify({
      "colaborator":{
        "id": new_colaborator.id,
        "full_name": full_name,
        "dependents": dependents,
        "department_id": department_id,
      }
    })

    return response

  def list(self, department_id):
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
