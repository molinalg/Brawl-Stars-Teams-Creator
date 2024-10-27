import re

# Clase para validar el formato de tags de Brawl Stars
class Validador():
    def __init__(self,datos):
        self.datos = datos
        self.validar_tags()

    def validar_tags(self):
        """Función para validar todos los tags en un conjunto de datos"""
        pattern = r"^#[PYLQGRJCUV0289]*$"

        for persona in self.datos:
            coincidencia = re.fullmatch(pattern,persona[2])
            if coincidencia is None and persona[2] != "El baneado" and persona[2] != "TAG de Brawl Stars":
                print("---------------------------------------------------------------")
                print("Tag incorrecto correspondiente a: {miembro} ({tag})".format(miembro = persona[3], tag = persona[2]))
                print("---------------------------------------------------------------")
