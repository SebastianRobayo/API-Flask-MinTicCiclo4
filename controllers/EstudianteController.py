from repositories.EstudianteRepo import EstudianteRepo
from models.Estudiante import Estudiante


class EstudianteController():
    def __init__(self):
        self.estudiantesRepo = EstudianteRepo()

    def listAll(self):
        return self.estudiantesRepo.findAll()

    def listOne(self, id):
        elEstudiante = Estudiante(self.estudiantesRepo.findById(id))
        return elEstudiante.__dict__

    def create(self, body):
        nuevoEstudiante = Estudiante(body)
        return self.estudiantesRepo.save(nuevoEstudiante)

    def update(self, id, body):
        estudianteActual = Estudiante(self.estudiantesRepo.findById(id))
        estudianteActual.cedula = body["cedula"]
        estudianteActual.nombre = body["nombre"]
        estudianteActual.apellido = body["apellido"]
        return self.estudiantesRepo.save(estudianteActual)

    def delete(self, id):
        return self.estudiantesRepo.delate(id)
