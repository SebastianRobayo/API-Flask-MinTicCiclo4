from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import pymongo
import certifi
from waitress import serve
from controllers.EstudianteController import EstudianteController
from controllers.DepartamentoController import DepartamentoController
from controllers.MateriaController import MateriaController
from controllers.InscripcionController import InscripcionController

app = Flask(__name__)
cors = CORS(app)
estudianteController = EstudianteController()
departamentoController = DepartamentoController()
materiaController = MateriaController()
inscripcionController = InscripcionController()


# ca = certifi.where()
# client = pymongo.MongoClient(
# "mongodb+srv://usuario-pruebas:root123456@cluster0.unflt.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
# db = client.test
# print(db)

# baseDatos = client["db-registro-academico"]
# print(baseDatos.list_collection_names())

# TODO:Controlador Estudiantes


@app.route("/estudiantes", methods=['GET'])
def getEstudiantes():
    json = estudianteController.listAll()
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['GET'])
def getEstudiante(id):
    json = estudianteController.listOne(id)
    return jsonify(json)


@app.route("/estudiantes", methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json = estudianteController.create(data)
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['PUT'])
def modificarEstudiante(id):
    data = request.get_json()
    json = estudianteController.update(id, data)
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['DELETE'])
def eliminarEstudiante(id):
    json = estudianteController.delete(id)
    return jsonify(json)

# TODO: Controlador Departamento


@app.route("/departamentos", methods=['GET'])
def getDepartamentos():
    json = departamentoController.listAll()
    return jsonify(json)


@app.route("/departamentos/<string:id>", methods=['GET'])
def getDepartamento(id):
    json = departamentoController.listOne(id)
    return jsonify(json)


@app.route("/departamentos", methods=['POST'])
def createDepartamento():
    data = request.get_json()
    json = departamentoController.create(data)
    return jsonify(json)


@app.route("/departamentos/<string:id>", methods=['PUT'])
def updateDepartamento(id):
    data = request.get_json()
    json = departamentoController.update(id, data)
    return jsonify(json)


@app.route("/departamentos/<string:id>", methods=['DELETE'])
def deleteDepartamento(id):
    json = departamentoController.delete(id)
    return jsonify(json)

# TODO: Controlador Materia


@app.route("/materias", methods=['GET'])
def getMaterias():
    json = materiaController.listAll()
    return jsonify(json)


@app.route("/materias/<string:id>", methods=['GET'])
def getMateria(id):
    json = materiaController.listOne(id)
    return jsonify(json)


@app.route("/materias", methods=['POST'])
def createMateria():
    data = request.get_json()
    json = materiaController.create(data)
    return jsonify(json)


@app.route("/materias/<string:id>", methods=['PUT'])
def updateMateria(id):
    data = request.get_json()
    json = materiaController.update(id, data)
    return jsonify(json)


@app.route("/materias/<string:id>", methods=['DELETE'])
def deleteMateria(id):
    json = materiaController.delete(id)
    return jsonify(json)


@app.route("/materias/<string:id>/departamento/<string:id_departamento>", methods=['PUT'])
def asignarDepartamentoAMateria(id, id_departamento):
    json = materiaController.asignarDepartamento(id, id_departamento)
    return jsonify(json)

    # TODO: Controlador Inscripciones


@app.route("/inscripciones", methods=['GET'])
def getInscripciones():
    json = inscripcionController.listAll()
    return jsonify(json)


@app.route("/inscripciones/<string:id>", methods=['GET'])
def getInscripcion(id):
    json = inscripcionController.listOne(id)
    return jsonify(json)


@app.route("/inscripciones/estudiante/<string:id_estudiante>/materia/<string:id_materia>", methods=['POST'])
def crearInscripcion(id_estudiante, id_materia):
    data = request.get_json()
    json = inscripcionController.create(data, id_estudiante, id_materia)
    return jsonify(json)


@app.route("/inscripciones/<string:id_inscripcion>/estudiante/<string:id_estudiante>/materia/<string:id_materia>", methods=['PUT'])
def updateInscripcion(id_inscripcion, id_estudiante, id_materia):
    data = request.get_json()
    json = inscripcionController.update(
        id_inscripcion, data, id_estudiante, id_materia)
    return jsonify(json)


@app.route("/inscripciones/<string:id_inscripcion>", methods=['DELETE'])
def deleteInscripcion(id_inscripcion):
    json = inscripcionController.delete(id_inscripcion)
    return jsonify(json)


@app.route("/inscripciones/materia/<string:id_materia>", methods=['GET'])
def inscritosEnMateria(id_materia):
    json = inscripcionController.listarInscritosEnMateria(id_materia)
    return jsonify(json)


@app.route("/inscripciones/notas_mayores", methods=['GET'])
def getNotasMayores():
    json = inscripcionController.notasMasAltasPorCurso()
    return jsonify(json)


@app.route("/inscripciones/promedio_notas/materia/<string:id_materia>", methods=['GET'])
def getPromedioNotasEnMateria(id_materia):
    json = inscripcionController.promedioNotasEnMateria(id_materia)
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)

    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print(
        f'server running:http://{dataConfig["url-backend"]}:{str(dataConfig["port"])}')
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
    # app.run(debug=True)
