from src import app, db
from src import routes
from src.department.models.department import Department
from src.colaborator.models.colaborator import Colaborator

db.create_all()

if __name__=='__main__':
  app.run()