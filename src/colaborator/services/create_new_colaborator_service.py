from ..models.colaborator import Colaborator
from ... import db
from flask import jsonify

def create_new_colaborator_service(full_name, dependents, department_id):
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