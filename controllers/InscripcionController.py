from repositories.InscripcionRepo import InscripcionRepo
from repositories.EstudianteRepo import EstudianteRepo
from repositories.MateriaRepo import MateriaRepo
from models.Inscripcion import Inscripcion
from models.Estudiante import Estudiante
from models.Materia import Materia


class InscripcionController():
    def __init__(self):
        self.inscripcionRepo = InscripcionRepo()
        self.estudiantesRepo = EstudianteRepo()
        self.materiasRepo = MateriaRepo()

    def listAll(self):
        return self.inscripcionRepo.findAll()

    def listOne(self, id):
        inscripcion = Inscripcion(self.inscripcionRepo.findById(id))
        return inscripcion.__dict__
    # TODO: Asignación estudiante y materia a inscripción

    def create(self, body, id_estudiante, id_materia):
        nuevaInscripcion = Inscripcion(body)
        elEstudiante = Estudiante(self.estudiantesRepo.findById(id_estudiante))
        laMateria = Materia(self.materiasRepo.findById(id_materia))
        nuevaInscripcion.estudiante = elEstudiante
        nuevaInscripcion.materia = laMateria
        return self.inscripcionRepo.save(nuevaInscripcion)
    # TODO: Modificación de inscripción (estudiante y materia)

    def update(self, id, body, id_estudiante, id_materia):
        inscripcionActual = Inscripcion(self.inscripcionRepo.findById(id))
        inscripcionActual.anio = body["anio"]
        inscripcionActual.semestre = body["semestre"]
        inscripcionActual.nota_final = body["nota_final"]
        elEstudiante = Estudiante(self.estudiantesRepo.findById(id_estudiante))
        laMateria = Materia(self.materiasRepo.findById(id_materia))
        inscripcionActual.estudiante = elEstudiante
        inscripcionActual.materia = laMateria
        return self.inscripcionRepo.save(inscripcionActual)

    # TODO: Obtener todos los inscritos en una materia
    def listarInscritosEnMateria(self, id_materia):
        return self.inscripcionRepo.getListadoInscritosEnMateria(id_materia)

    # TODO: Obtener notas más altas por curso
    def notasMasAltasPorCurso(self):
        return self.inscripcionRepo.getMayorNotaPorCurso()

    # TODO: Obtener promedio de notas de materia
    def promedioNotasEnMateria(self, id_materia):
        return self.inscripcionRepo.promedioNotasEnMateria(id_materia)

    def delete(self, id):
        return self.inscripcionRepo.delate(id)
