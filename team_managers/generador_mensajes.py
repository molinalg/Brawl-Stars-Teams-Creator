# Generación de mensajes para enviar por discord con todos los equipos
class Generador_Mensajes():
    def __init__(self,organizador_A,organizador_B,organizador_C):
        self.organizador_A = organizador_A
        self.organizador_B = organizador_B
        self.organizador_C = organizador_C

    def generar_mensaje_A(self):
        """Función que genera el mensaje del club A"""
        message_A = "__**Grupos A:**__\n\n"

        counter = 1
        for region in self.organizador_A.equipos:
            if len(region) != 0 and region == self.organizador_A.equipos[0]:
                message_A += "**EMEA:**\n\n"
                for equipo in region:
                    add = "-**Grupo {posicion} ({horario}):**\n".format(posicion=counter, horario=equipo[-1])
                    counter += 1
                    for persona in equipo:
                        if type(persona) == list:
                            add += "@{discord}\n".format(discord=persona[4])
                    message_A += add + "\n"
            elif len(region) != 0 and region == self.organizador_A.equipos[1]:
                message_A += "**NA & LATAM:**\n\n"
                for equipo in region:
                    add = "-**Grupo {posicion} ({horario}):**\n".format(posicion=counter, horario=equipo[-1])
                    counter += 1
                    for persona in equipo:
                        if type(persona) == list:
                            add += "@{discord}\n".format(discord=persona[4])
                    message_A += add + "\n"
            elif len(region) != 0 and region == self.organizador_A.equipos[2]:
                message_A += "**LATAM SUR:**\n\n"
                for equipo in region:
                    add = "-**Grupo {posicion} ({horario}):**\n".format(posicion=counter, horario=equipo[-1])
                    counter += 1
                    for persona in equipo:
                        if type(persona) == list:
                            add += "@{discord}\n".format(discord=persona[4])
                    message_A += add + "\n"
            elif len(region) != 0 and region == self.organizador_A.equipos[3]:
                message_A += "**EQUIPOS ESCOGIDOS POR LOS MIEMBROS:**\n\n"
                for equipo in region:
                    add = "-**Grupo {posicion}:**\n".format(posicion=counter)
                    counter += 1
                    for persona in equipo:
                        if type(persona) == list and len(persona) != 1:
                            add += "@{discord}\n".format(discord=persona[4])
                    message_A += add + "\n"
            elif len(region) == 0:
                print("Hay una categoría sin gente (A)")
            else:
                print("ERROR: Algo ha fallado generando el mensaje de equipos del A")
                print(region)
                exit(-1)

        return message_A


    def generar_mensaje_B(self):
        """Función que genera el mensaje del club B"""
        message_B = "__**Grupos B:**__\n\n"

        counter = 1
        for region in self.organizador_B.equipos:
            if len(region) != 0 and region == self.organizador_B.equipos[0]:
                message_B += "**EMEA**:\n\n"
                for equipo in region:
                    add = "-**Grupo {posicion} ({horario}):**\n".format(posicion=counter, horario=equipo[-1])
                    counter += 1
                    for persona in equipo:
                        if type(persona) == list:
                            add += "@{discord}\n".format(discord=persona[4])
                    message_B += add + "\n"
            elif len(region) != 0 and region == self.organizador_B.equipos[1]:
                message_B += "**NA & LATAM:**\n\n"
                for equipo in region:
                    add = "-**Grupo {posicion} ({horario}):**\n".format(posicion=counter, horario=equipo[-1])
                    counter += 1
                    for persona in equipo:
                        if type(persona) == list:
                            add += "@{discord}\n".format(discord=persona[4])
                    message_B += add + "\n"
            elif len(region) != 0 and region == self.organizador_B.equipos[2]:
                message_B += "**LATAM SUR:**\n\n"
                for equipo in region:
                    add = "-**Grupo {posicion} ({horario}):**\n".format(posicion=counter, horario=equipo[-1])
                    counter += 1
                    for persona in equipo:
                        if type(persona) == list:
                            add += "@{discord}\n".format(discord=persona[4])
                    message_B += add + "\n"
            elif len(region) != 0 and region == self.organizador_B.equipos[3]:
                message_B += "**EQUIPOS ESCOGIDOS POR LOS MIEMBROS:**\n\n"
                for equipo in region:
                    add = "-**Grupo {posicion}:**\n".format(posicion=counter)
                    counter += 1
                    for persona in equipo:
                        if type(persona) == list and len(persona) != 1:
                            add += "@{discord}\n".format(discord=persona[4])
                    message_B += add + "\n"
            elif len(region) == 0:
                print("Hay una categoría sin gente (B)")
            else:
                print("ERROR: Algo ha fallado generando el mensaje de equipos del B")
                print(region)
                exit(-1)
        return message_B


    def generar_mensaje_C(self):
        """Función que genera el mensaje del club C"""
        message_C = "__**Grupos C:**__\n\n"

        counter = 1
        for region in self.organizador_C.equipos:
            if len(region) != 0 and region == self.organizador_C.equipos[0]:
                message_C += "**EMEA:**\n\n"
                for equipo in region:
                    add = "-**Grupo {posicion} ({horario}):**\n".format(posicion=counter, horario=equipo[-1])
                    counter += 1
                    for persona in equipo:
                        if type(persona) == list:
                            add += "@{discord}\n".format(discord=persona[4])
                    message_C += add + "\n"
            elif len(region) != 0 and region == self.organizador_C.equipos[1]:
                message_C += "**NA & LATAM:**\n\n"
                for equipo in region:
                    add = "-**Grupo {posicion} ({horario}):**\n".format(posicion=counter, horario=equipo[-1])
                    counter += 1
                    for persona in equipo:
                        if type(persona) == list:
                            add += "@{discord}\n".format(discord=persona[4])
                    message_C += add + "\n"
            elif len(region) != 0 and region == self.organizador_C.equipos[2]:
                message_C += "**LATAM SUR:**\n\n"
                for equipo in region:
                    add = "-**Grupo {posicion} ({horario}):**\n".format(posicion=counter, horario=equipo[-1])
                    counter += 1
                    for persona in equipo:
                        if type(persona) == list:
                            add += "@{discord}\n".format(discord=persona[4])
                    message_C += add + "\n"
            elif len(region) != 0 and region == self.organizador_C.equipos[3]:
                message_C += "**EQUIPOS ESCOGIDOS POR LOS MIEMBROS:**\n\n"
                for equipo in region:
                    add = "-**Grupo {posicion}:**\n".format(posicion=counter)
                    counter += 1
                    for persona in equipo:
                        if type(persona) == list and len(persona) != 1:
                            add += "@{discord}\n".format(discord=persona[4])
                    message_C += add + "\n"
            elif len(region) == 0:
                print("Hay una categoría sin gente (C)")
            else:
                print("ERROR: Algo ha fallado generando el mensaje de equipos del C")
                print(region)
                exit(-1)
        return message_C