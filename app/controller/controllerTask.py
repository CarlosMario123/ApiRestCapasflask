from flask import jsonify, request
from app.services.servicesTask import TareaService
from sqlalchemy.exc import SQLAlchemyError

tareaServices = TareaService()

class TareaController:
    @staticmethod
    def obtener_todas_las_tareas():
        tareas = tareaServices.obtenerAllTask()
        tareas_list = [{'id': tarea.id, 'descripcion': tarea.descripcion} for tarea in tareas]
        return jsonify(tareas_list)


    @staticmethod
    def crear_tarea():
        try:
            nueva_tarea = request.json
            tarea_creada = tareaServices.crearTarea(nueva_tarea)
            
            tarea_dict = {
                'id': tarea_creada.id,
                'descripcion': tarea_creada.descripcion,
            }
            
            return jsonify(tarea_dict), 201
        except SQLAlchemyError as e:
            # Manejar errores de SQLAlchemy (por ejemplo, violación de restricción única, etc.)
            error_message = str(e)
            return jsonify({'error': error_message}), 500
        except Exception as e:
            # Capturar errores generales
            error_message = str(e)
            return jsonify({'error': error_message}), 500
        
        
    @staticmethod
    def obtener_tarea_por_id(tarea_id):
        try:
            tarea = tareaServices.obtenerTareaPorId(tarea_id)

            if tarea:
                tarea_dict = {
                    'id': tarea.id,
                    'descripcion': tarea.descripcion,
                }
                return jsonify(tarea_dict)
            else:
                return jsonify({'error': 'Tarea no encontrada'}), 404
        except SQLAlchemyError as e:
            # Manejar errores de SQLAlchemy
            error_message = str(e)
            return jsonify({'error': error_message}), 500
        except Exception as e:
            # Capturar errores generales
            error_message = str(e)
            return jsonify({'error': error_message}), 500    