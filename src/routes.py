
from .department.views.department import DepartmentView
from .colaborator.views.colaborator import ColaboratorView

from src import app

DepartmentView.register(app, route_base='/departments/')
ColaboratorView.register(app, route_base='/colaborators')