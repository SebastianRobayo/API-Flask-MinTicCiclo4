from bson import ObjectId
from repositories.InterfaceRepo import InterfaceRepo
from models.Inscripcion import Inscripcion
from bson import ObjectId


class InscripcionRepo(InterfaceRepo[Inscripcion]):
    def getListadoInscritosEnMateria(self, id_materia):
        theQuery = {"materia.$id": ObjectId(id_materia)}
        return self.query(theQuery)

    def getMayorNotaPorCurso(self):
        query1 = {
            "$group": {
                "_id": "$materia",
                "max": {
                    "$max": "$nota_final"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [query1]
        return self.queryAggregetion(pipeline)

    def promedioNotasEnMateria(self, id_materia):
        query1 = {
            "$match": {"materia.$id": ObjectId(id_materia)}
        }
        query2 = {
            "$group": {
                "_id": "$materia",
                "promedio": {
                    # "$avg": "nota_final"
                    "$sum": "nota_final"  # Suma total de todas las notas
                }
            }
        }
        pipeline = [query1, query2]
        return self.queryAggregetion(pipeline)
