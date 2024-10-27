import json
import datetime

# Clase para manejar el archivo de miembros procesados
class Procesados_Controller():
    personas = []
    def __init__(self):
        pass

    def rellenar_personas(self,personas):
        """Función que carga datos en una lista de la clase"""
        for element in personas:
            self.personas.append(element)

    def actualizar_procesados(self):
        """Función que actualiza el contenido del archivo de procesados si corresponde"""
        with open("procesados.json") as procesados:
            registros = json.load(procesados)

        if registros["fecha"] == "2022":
            print("Lista de antiguos miembros NO actualizada")
            return

        elementos_fecha = registros["fecha"]
        lista = elementos_fecha.split("-")

        if lista[1][0] == "0":
            lista[1] = lista[1][1]
        if lista[2][0] == "0":
            lista[2] = lista[2][1]

        fecha = datetime.date(int(lista[0]), int(lista[1]), int(lista[2]))
        hoy = datetime.datetime.now().date()

        diferencia = hoy - fecha
        dias = diferencia.days

        if dias >= 14:
            for persona in self.personas:
                registros["miembros"].append(persona)
        else:
            print("Lista de antiguos miembros NO actualizada")
            return

        registros["fecha"] = str(hoy)

        with open("procesados.json", 'w') as json_file:
            json.dump(registros,json_file,indent=6)

        print("Lista de antiguos miembros actualizada")
