import json

# Clase para leer archivos JSON
class Json_Reader():
    def __init__(self,file):
        self.file = file

    def read_json(self):
        """Función para obtener el contenido de un archivo JSON"""
        with open(self.file) as file:
            data = json.load(file)

        lista = []
        for miembro in data["items"]:
            lista.append(miembro["tag"])
        return lista

    def get_names(self,tags):
        """Función que identifica nombres nuevos no procesados en el pasado"""
        nuevos = []
        antiguos = []

        with open(self.file) as file:
            data = json.load(file)
        with open("procesados.json") as procesados:
            viejos = json.load(procesados)

        lista = []
        añadir = []
        for miembro in data["items"]:
            if miembro["tag"] in tags:
                lista.append([miembro["name"],miembro["tag"]])
                añadir.append(miembro["tag"])

        repetidos = viejos["miembros"]
        for persona in lista:
            if persona[1] not in repetidos:
                nuevos.append(persona[0])
            else:
                antiguos.append(persona[0])

        resultado = [nuevos,antiguos]

        return resultado,añadir

    def get_all_names(self,tags):
        """Función que extrae todos los nombres presentes en un JSON"""
        with open(self.file) as file:
            data = json.load(file)

        lista = []
        for miembro in data["items"]:
            if miembro["tag"] in tags:
                lista.append(miembro["name"])

        return lista
