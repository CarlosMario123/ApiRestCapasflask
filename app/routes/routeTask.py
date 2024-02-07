from flask import Blueprint
from app.controller.controllerTask import TareaController

tareaRoute = Blueprint('tarea', __name__, url_prefix='/tareas')

tareaRoute.route("",methods=['GET'])(TareaController.obtener_todas_las_tareas)
tareaRoute.route("",methods=['POST'])(TareaController.crear_tarea)
tareaRoute.route("/<int:tarea_id>", methods=['GET'])(TareaController.obtener_tarea_por_id)