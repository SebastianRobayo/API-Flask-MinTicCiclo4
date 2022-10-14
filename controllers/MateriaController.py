from repositories.MateriaRepo import MateriaRepo
from repositories.DepartamentoRepo import DepartamentoRepo
from models.Materia import Materia
from models.Departamento import Departamento


class MateriaController():
    def __init__(self):
        self.materiaRepo = MateriaRepo()
        self.departamentoRepo = DepartamentoRepo()

    def listAll(self):
        return self.materiaRepo.findAll()

    def listOne(self, id):
        matria = Materia(self.materiaRepo.findById(id))
        return matria.__dict__

    def create(self, body):
        nuevaMateria = Materia(body)
        return self.materiaRepo.save(nuevaMateria)

    def update(self, id, body):
        materiaActual = Materia(self.materiaRepo.findById(id))
        materiaActual.nombre = body["nombre"]
        materiaActual.creditos = body["creditos"]
        return self.materiaRepo.save(materiaActual)

    def delete(self, id):
        return self.materiaRepo.delate(id)

    # TODO: Relación departamento y materia
    def asignarDepartamento(self, id, id_departamento):
        materiaActual = Materia(self.materiaRepo.findById(id))
        departamentoActual = Departamento(
            self.departamentoRepo.findById(id_departamento))
        materiaActual.departamento = departamentoActual
        return self.materiaRepo.save(materiaActual)
