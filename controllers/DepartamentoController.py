from repositories.DepartamentoRepo import DepartamentoRepo
from models.Departamento import Departamento


class DepartamentoController():
    def __init__(self):
        self.departamentoRepo = DepartamentoRepo()

    def listAll(self):
        return self.departamentoRepo.findAll()

    def listOne(self, id):
        departamento = Departamento(self.departamentoRepo.findById(id))
        return departamento.__dict__

    def create(self, body):
        nuevoDepartamento = Departamento(body)
        return self.departamentoRepo.save(nuevoDepartamento)

    def update(self, id, body):
        departamentoActual = Departamento(self.departamentoRepo.findById(id))
        departamentoActual.nombre = body["nombre"]
        departamentoActual.descripcion = body["descripcion"]
        return self.departamentoRepo.save(departamentoActual)

    def delete(self, id):
        return self.departamentoRepo.delate(id)
