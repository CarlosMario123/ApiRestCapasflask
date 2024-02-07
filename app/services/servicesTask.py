from app.models.Task import Tarea,db


class TareaService:
    def obtenerAllTask(self):
        return Tarea.query.all()

    def crearTarea(self, tarea):
        nuevaTarea = Tarea(descripcion=tarea['descripcion'])
        db.session.add(nuevaTarea)
        db.session.commit()
        return nuevaTarea
    
    def obtenerTareaPorId(self, tarea_id):
        return Tarea.query.get(tarea_id)    