import random

# Clase para crear los equipos finales según su elección horaria y regíón
class Organizador_Equipos():

    def __init__(self,datos_separados):
        self.datos_separados = datos_separados
        self.grupos_EMEA = []
        self.grupos_LNorte = []
        self.grupos_LSur = []
        self.grupos_Prefabricados = []

        self.crear_prefabricados(self.datos_separados.prefabricados)

        self.crear_individual(self.datos_separados.mañanas_EMEA,self.datos_separados.mañanas_LNorte,
                              self.datos_separados.mañanas_LSur,"mañana")

        self.crear_individual(self.datos_separados.tardes_EMEA, self.datos_separados.tardes_LNorte,
                              self.datos_separados.tardes_LSur, "tarde")

        self.crear_individual(self.datos_separados.noches_EMEA, self.datos_separados.noches_LNorte,
                              self.datos_separados.noches_LSur, "noche")

        self.crear_compuesto(self.datos_separados.mañanas_tardes_EMEA,self.datos_separados.mañanas_tardes_LNorte,
                             self.datos_separados.mañanas_tardes_LSur, "Por la mañana", "Por la tarde")

        self.crear_compuesto(self.datos_separados.mañanas_noches_EMEA, self.datos_separados.mañanas_noches_LNorte,
                             self.datos_separados.mañanas_noches_LSur, "Por la mañana", "Por la noche")

        self.crear_compuesto(self.datos_separados.tardes_noches_EMEA, self.datos_separados.tardes_noches_LNorte,
                             self.datos_separados.tardes_noches_LSur, "Por la tarde", "Por la noche")

        self.crear_siempre()

        self.total = self.recuento_distribuidos()
        self.equipos = [self.grupos_EMEA,self.grupos_LNorte,self.grupos_LSur,self.grupos_Prefabricados]

    def crear_individual(self,emea,l_norte,l_sur,tiempo):
        """Función para crear los equipos que son de un solo horario disponible"""
        while len(emea) != 0:
            if len(emea) > 4:
                grupo = []
                for i in range(0, 3):
                    selection = random.choice(emea)
                    grupo.append(selection)
                for element in grupo:
                    emea.remove(element)
                grupo.append("Por la {}".format(tiempo))
                self.grupos_EMEA.append(grupo)

            elif len(emea) == 4:
                grupo = []
                done = False
                while not done:
                    if len(grupo) == 2:
                        done = True
                    else:
                        selection = random.choice(emea)
                        if selection not in grupo:
                            grupo.append(selection)

                for element in grupo:
                    emea.remove(element)
                grupo.append("Por la {}".format(tiempo))
                self.grupos_EMEA.append(grupo)

                grupo = []
                for element in emea:
                    grupo.append(element)
                for element in grupo:
                    emea.remove(element)
                grupo.append("Por la {}".format(tiempo))
                self.grupos_EMEA.append(grupo)

            elif len(emea) == 3 or len(emea) == 2:
                grupo = []
                for element in emea:
                    grupo.append(element)
                for element in grupo:
                    emea.remove(element)
                grupo.append("Por la {}".format(tiempo))
                self.grupos_EMEA.append(grupo)

            elif len(emea) == 1:
                grupo = []
                selection = emea[0]
                grupo.append(emea[0])
                emea.remove(selection)
                grupo.append("Por la {}".format(tiempo))
                self.grupos_EMEA.append(grupo)

            else:
                print("ERROR: No se pudieron crear los grupos")
                exit(-1)

        while len(l_norte) != 0:
            if len(l_norte) > 4:
                grupo = []
                for i in range(0, 3):
                    selection = random.choice(l_norte)
                    grupo.append(selection)
                    l_norte.remove(selection)
                grupo.append("Por la {}".format(tiempo))
                self.grupos_LNorte.append(grupo)

            elif len(l_norte) == 4:
                grupo = []
                done = False
                while not done:
                    if len(grupo) == 2:
                        done = True
                    else:
                        selection = random.choice(l_norte)
                        if selection not in grupo:
                            grupo.append(selection)

                for element in grupo:
                    l_norte.remove(element)
                grupo.append("Por la {}".format(tiempo))
                self.grupos_LNorte.append(grupo)

                grupo = []
                for element in l_norte:
                    grupo.append(element)
                for element in grupo:
                    l_norte.remove(element)
                grupo.append("Por la {}".format(tiempo))
                self.grupos_LNorte.append(grupo)

            elif len(l_norte) == 3 or len(l_norte) == 2:
                grupo = []
                for element in l_norte:
                    grupo.append(element)
                for element in grupo:
                    l_norte.remove(element)
                grupo.append("Por la {}".format(tiempo))
                self.grupos_LNorte.append(grupo)

            elif len(l_norte) == 1:
                grupo = []
                selection = l_norte[0]
                grupo.append(l_norte[0])
                l_norte.remove(selection)
                grupo.append("Por la {}".format(tiempo))
                self.grupos_LNorte.append(grupo)

            else:
                print("ERROR: No se pudieron crear los grupos")
                exit(-1)

        while len(l_sur) != 0:
            if len(l_sur) > 4:
                grupo = []
                for i in range(0, 3):
                    selection = random.choice(l_sur)
                    grupo.append(selection)
                    l_sur.remove(selection)
                grupo.append("Por la {}".format(tiempo))
                self.grupos_LSur.append(grupo)

            elif len(l_sur) == 4:
                grupo = []
                done = False
                while not done:
                    if len(grupo) == 2:
                        done = True
                    else:
                        selection = random.choice(l_sur)
                        if selection not in grupo:
                            grupo.append(selection)

                for element in grupo:
                    l_sur.remove(element)
                grupo.append("Por la {}".format(tiempo))
                self.grupos_LSur.append(grupo)

                grupo = []
                for element in l_sur:
                    grupo.append(element)
                    l_sur.remove(element)
                grupo.append("Por la {}".format(tiempo))
                self.grupos_LSur.append(grupo)

            elif len(l_sur) == 3 or len(l_sur) == 2:
                grupo = []
                for element in l_sur:
                    grupo.append(element)
                for element in grupo:
                    l_sur.remove(element)
                grupo.append("Por la {}".format(tiempo))
                self.grupos_LSur.append(grupo)

            elif len(l_sur) == 1:
                grupo = []
                selection = l_sur[0]
                grupo.append(l_sur[0])
                l_sur.remove(selection)
                grupo.append("Por la {}".format(tiempo))
                self.grupos_LSur.append(grupo)

            else:
                print("ERROR: No se pudieron crear los grupos")
                exit(-1)

    def crear_compuesto(self,emea,l_norte,l_sur,op1,op2):
        """Función para crear los equipos que son de 2 horarios"""
        segundaOP = op2.split(" ")[2]
        while len(emea) != 0:
            finish = False
            while not finish:
                if len(emea) == 0:
                    break
                finish = True
                for equipo in self.grupos_EMEA:
                    if equipo[-1] == op1 and (len(equipo) == 2 or len(equipo) == 3):
                        removed = equipo.pop(-1)
                        introduced = emea[0]
                        equipo.append(introduced)
                        equipo.append(removed)
                        emea.remove(introduced)
                        finish = False
            finish = False
            if len(emea) != 0:
                while not finish:
                    if len(emea) == 0:
                        break
                    finish = True
                    for equipo in self.grupos_EMEA:
                        if equipo[-1] == op2 and (len(equipo) == 2 or len(equipo) == 3):
                            removed = equipo.pop(-1)
                            introduced = emea[0]
                            equipo.append(introduced)
                            equipo.append(removed)
                            emea.remove(introduced)
                            finish = False

            if len(emea) != 0:
                if len(emea) > 4:
                    grupo = []
                    for i in range(0, 3):
                        selection = random.choice(emea)
                        grupo.append(selection)
                        emea.remove(selection)
                    grupo.append("{o1} y {o2}".format(o1 = op1, o2 = segundaOP))
                    self.grupos_EMEA.append(grupo)

                elif len(emea) == 4:
                    grupo = []
                    done = False
                    while not done:
                        if len(grupo) == 2:
                            done = True
                        else:
                            selection = random.choice(emea)
                            if selection not in grupo:
                                grupo.append(selection)

                    for element in grupo:
                        emea.remove(element)
                    grupo.append("{o1} y {o2}".format(o1 = op1, o2 = segundaOP))
                    self.grupos_EMEA.append(grupo)

                    grupo = []
                    for element in emea:
                        grupo.append(element)
                    for element in grupo:
                        emea.remove(element)
                    grupo.append("{o1} y {o2}".format(o1 = op1, o2 = segundaOP))
                    self.grupos_EMEA.append(grupo)

                elif len(emea) == 3 or len(emea) == 2:
                    grupo = []
                    for element in emea:
                        grupo.append(element)
                    for element in grupo:
                        emea.remove(element)
                    grupo.append("{o1} y {o2}".format(o1 = op1, o2 = segundaOP))
                    self.grupos_EMEA.append(grupo)

                elif len(emea) == 1:
                    grupo = []
                    selection = emea[0]
                    grupo.append(emea[0])
                    emea.remove(selection)
                    grupo.append("{o1} y {o2}".format(o1 = op1, o2 = segundaOP))
                    self.grupos_EMEA.append(grupo)

                else:
                    print("ERROR: No se pudieron crear los grupos")
                    exit(-1)

        while len(l_norte) != 0:
            finish = False
            while not finish:
                if len(l_norte) == 0:
                    break
                finish = True
                for equipo in self.grupos_LNorte:
                    if equipo[-1] == op1 and (len(equipo) == 2 or len(equipo) == 3):
                        removed = equipo.pop(-1)
                        introduced = l_norte[0]
                        equipo.append(introduced)
                        equipo.append(removed)
                        l_norte.remove(introduced)
                        finish = False
            finish = False
            if len(l_norte) != 0:
                while not finish:
                    if len(l_norte) == 0:
                        break
                    finish = True
                    for equipo in self.grupos_LNorte:
                        if equipo[-1] == op2 and (len(equipo) == 2 or len(equipo) == 3):
                            removed = equipo.pop(-1)
                            introduced = l_norte[0]
                            equipo.append(introduced)
                            equipo.append(removed)
                            l_norte.remove(introduced)
                            finish = False

            if len(l_norte) != 0:
                if len(l_norte) > 4:
                    grupo = []
                    for i in range(0, 3):
                        selection = random.choice(l_norte)
                        grupo.append(selection)
                        l_norte.remove(selection)
                    grupo.append("{o1} y {o2}".format(o1 = op1, o2 = segundaOP))
                    self.grupos_LNorte.append(grupo)

                elif len(l_norte) == 4:
                    grupo = []
                    done = False
                    while not done:
                        if len(grupo) == 2:
                            done = True
                        else:
                            selection = random.choice(l_norte)
                            if selection not in grupo:
                                grupo.append(selection)

                    for element in grupo:
                        l_norte.remove(element)
                    grupo.append("{o1} y {o2}".format(o1 = op1, o2 = segundaOP))
                    self.grupos_LNorte.append(grupo)

                    grupo = []
                    for element in l_norte:
                        grupo.append(element)
                    for element in grupo:
                        l_norte.remove(element)
                    grupo.append("{o1} y {o2}".format(o1 = op1, o2 = segundaOP))
                    self.grupos_LNorte.append(grupo)

                elif len(l_norte) == 3 or len(l_norte) == 2:
                    grupo = []
                    for element in l_norte:
                        grupo.append(element)
                    for element in grupo:
                        l_norte.remove(element)
                    grupo.append("{o1} y {o2}".format(o1 = op1, o2 = segundaOP))
                    self.grupos_LNorte.append(grupo)

                elif len(l_norte) == 1:
                    grupo = []
                    selection = l_norte[0]
                    grupo.append(l_norte[0])
                    l_norte.remove(selection)
                    grupo.append("{o1} y {o2}".format(o1 = op1, o2 = segundaOP))
                    self.grupos_LNorte.append(grupo)

                else:
                    print("ERROR: No se pudieron crear los grupos")
                    exit(-1)

        while len(l_sur) != 0:
            finish = False
            while not finish:
                if len(l_sur) == 0:
                    break
                finish = True
                for equipo in self.grupos_LSur:
                    if equipo[-1] == op1 and (len(equipo) == 2 or len(equipo) == 3):
                        removed = equipo.pop(-1)
                        introduced = l_sur[0]
                        equipo.append(introduced)
                        equipo.append(removed)
                        l_sur.remove(introduced)
                        finish = False
            finish = False
            if len(l_sur) != 0:
                while not finish:
                    if len(l_sur) == 0:
                        break
                    finish = True
                    for equipo in self.grupos_LSur:
                        if equipo[-1] == op2 and (len(equipo) == 2 or len(equipo) == 3):
                            removed = equipo.pop(-1)
                            introduced = l_sur[0]
                            equipo.append(introduced)
                            equipo.append(removed)
                            l_sur.remove(introduced)
                            finish = False

            if len(l_sur) != 0:
                if len(l_sur) > 4:
                    grupo = []
                    for i in range(0, 3):
                        selection = random.choice(l_sur)
                        grupo.append(selection)
                        l_sur.remove(selection)
                    grupo.append("{o1} y {o2}".format(o1 = op1, o2 = segundaOP))
                    self.grupos_LSur.append(grupo)

                elif len(l_sur) == 4:
                    grupo = []
                    done = False
                    while not done:
                        if len(grupo) == 2:
                            done = True
                        else:
                            selection = random.choice(l_sur)
                            if selection not in grupo:
                                grupo.append(selection)

                    for element in grupo:
                        l_sur.remove(element)
                    grupo.append("{o1} y {o2}".format(o1 = op1, o2 = segundaOP))
                    self.grupos_LSur.append(grupo)

                    grupo = []
                    for element in l_sur:
                        grupo.append(element)
                    for element in grupo:
                        l_sur.remove(element)
                    grupo.append("{o1} y {o2}".format(o1 = op1, o2 = segundaOP))
                    self.grupos_LSur.append(grupo)

                elif len(l_sur) == 3 or len(l_sur) == 2:
                    grupo = []
                    for element in l_sur:
                        grupo.append(element)
                    for element in grupo:
                        l_sur.remove(element)
                    grupo.append("{o1} y {o2}".format(o1 = op1, o2 = segundaOP))
                    self.grupos_LSur.append(grupo)

                elif len(l_sur) == 1:
                    grupo = []
                    selection = l_sur[0]
                    grupo.append(l_sur[0])
                    l_sur.remove(selection)
                    grupo.append("{o1} y {o2}".format(o1 = op1, o2 = segundaOP))
                    self.grupos_LSur.append(grupo)

                else:
                    print("ERROR: No se pudieron crear los grupos")
                    exit(-1)

    def crear_siempre(self):
        """Función para crear los equipos de gente siempre disponible"""
        while len(self.datos_separados.siempre_EMEA) != 0:
            finish = False
            while not finish:
                if len(self.datos_separados.siempre_EMEA) == 0:
                    break
                finish = True
                for equipo in self.grupos_EMEA:
                    if equipo[-1] == "Por la tarde" and (len(equipo) == 2 or len(equipo) == 3):
                        if len(self.datos_separados.siempre_EMEA) == 0:
                            break
                        removed = equipo.pop(-1)
                        introduced = self.datos_separados.siempre_EMEA[0]
                        equipo.append(introduced)
                        equipo.append(removed)
                        self.datos_separados.siempre_EMEA.remove(introduced)
                        finish = False
            finish = False
            if len(self.datos_separados.siempre_EMEA) != 0:
                while not finish:
                    if len(self.datos_separados.siempre_EMEA) == 0:
                        break
                    finish = True
                    for equipo in self.grupos_EMEA:
                        if equipo[-1] == "Por la noche" and (len(equipo) == 2 or len(equipo) == 3):
                            if len(self.datos_separados.siempre_EMEA) == 0:
                                break
                            removed = equipo.pop(-1)
                            introduced = self.datos_separados.siempre_EMEA[0]
                            equipo.append(introduced)
                            equipo.append(removed)
                            self.datos_separados.siempre_EMEA.remove(introduced)
                            finish = False
            finish = False
            if len(self.datos_separados.siempre_EMEA) != 0:
                while not finish:
                    if len(self.datos_separados.siempre_EMEA) == 0:
                        break
                    finish = True
                    for equipo in self.grupos_EMEA:
                        if equipo[-1] == "Por la mañana" and (len(equipo) == 2 or len(equipo) == 3):
                            if len(self.datos_separados.siempre_EMEA) == 0:
                                break
                            removed = equipo.pop(-1)
                            introduced = self.datos_separados.siempre_EMEA[0]
                            equipo.append(introduced)
                            equipo.append(removed)
                            self.datos_separados.siempre_EMEA.remove(introduced)
                            finish = False

            if len(self.datos_separados.siempre_EMEA) != 0:
                if len(self.datos_separados.siempre_EMEA) > 4:
                    grupo = []
                    for i in range(0, 3):
                        selection = random.choice(self.datos_separados.siempre_EMEA)
                        grupo.append(selection)
                        self.datos_separados.siempre_EMEA.remove(selection)
                    grupo.append("Siempre")
                    self.grupos_EMEA.append(grupo)

                elif len(self.datos_separados.siempre_EMEA) == 4:
                    grupo = []
                    for i in range(0, 2):
                        selection = random.choice(self.datos_separados.siempre_EMEA)
                        grupo.append(selection)
                        self.datos_separados.siempre_EMEA.remove(selection)
                    grupo.append("Siempre")
                    self.grupos_EMEA.append(grupo)

                    grupo = []
                    for element in self.datos_separados.siempre_EMEA:
                        grupo.append(element)
                        self.datos_separados.siempre_EMEA.remove(element)
                    grupo.append("Siempre")
                    self.grupos_EMEA.append(grupo)

                elif len(self.datos_separados.siempre_EMEA) == 3 or len(
                        self.datos_separados.siempre_EMEA) == 2:
                    grupo = []
                    for element in self.datos_separados.siempre_EMEA:
                        grupo.append(element)
                    for element in grupo:
                        self.datos_separados.siempre_EMEA.remove(element)
                    grupo.append("Siempre")
                    self.grupos_EMEA.append(grupo)

                elif len(self.datos_separados.siempre_EMEA) == 1:
                    grupo = []
                    selection = self.datos_separados.siempre_EMEA[0]
                    grupo.append(self.datos_separados.siempre_EMEA[0])
                    self.datos_separados.siempre_EMEA.remove(selection)
                    grupo.append("Siempre")
                    self.grupos_EMEA.append(grupo)

                else:
                    print("ERROR: No se pudieron crear los grupos")
                    exit(-1)
        while len(self.datos_separados.siempre_LNorte) != 0:
            finish = False
            while not finish:
                if len(self.datos_separados.siempre_LNorte) == 0:
                    break
                finish = True
                for equipo in self.grupos_LNorte:
                    if equipo[-1] == "Por la tarde" and (len(equipo) == 2 or len(equipo) == 3):
                        if len(self.datos_separados.siempre_LNorte) == 0:
                            break
                        removed = equipo.pop(-1)
                        introduced = self.datos_separados.siempre_LNorte[0]
                        equipo.append(introduced)
                        equipo.append(removed)
                        self.datos_separados.siempre_LNorte.remove(introduced)
                        finish = False
            finish = False
            if len(self.datos_separados.siempre_LNorte) != 0:
                while not finish:
                    if len(self.datos_separados.siempre_LNorte) == 0:
                        break
                    finish = True
                    for equipo in self.grupos_LNorte:
                        if equipo[-1] == "Por la noche" and (len(equipo) == 2 or len(equipo) == 3):
                            if len(self.datos_separados.siempre_LNorte) == 0:
                                break
                            removed = equipo.pop(-1)
                            introduced = self.datos_separados.siempre_LNorte[0]
                            equipo.append(introduced)
                            equipo.append(removed)
                            self.datos_separados.siempre_LNorte.remove(introduced)
                            finish = False
            finish = False
            if len(self.datos_separados.siempre_LNorte) != 0:
                while not finish:
                    if len(self.datos_separados.siempre_LNorte) == 0:
                        break
                    finish = True
                    for equipo in self.grupos_LNorte:
                        if equipo[-1] == "Por la mañana" and (len(equipo) == 2 or len(equipo) == 3):
                            if len(self.datos_separados.siempre_LNorte) == 0:
                                break
                            removed = equipo.pop(-1)
                            introduced = self.datos_separados.siempre_LNorte[0]
                            equipo.append(introduced)
                            equipo.append(removed)
                            self.datos_separados.siempre_LNorte.remove(introduced)
                            finish = False

            if len(self.datos_separados.siempre_LNorte) != 0:
                if len(self.datos_separados.siempre_LNorte) > 4:
                    grupo = []
                    for i in range(0, 3):
                        selection = random.choice(self.datos_separados.siempre_LNorte)
                        grupo.append(selection)
                        self.datos_separados.siempre_LNorte.remove(selection)
                    grupo.append("Siempre")
                    self.grupos_LNorte.append(grupo)

                elif len(self.datos_separados.siempre_LNorte) == 4:
                    grupo = []
                    for i in range(0, 2):
                        selection = random.choice(self.datos_separados.siempre_LNorte)
                        grupo.append(selection)
                        self.datos_separados.siempre_LNorte.remove(selection)
                    grupo.append("Siempre")
                    self.grupos_LNorte.append(grupo)

                    grupo = []
                    for element in self.datos_separados.siempre_LNorte:
                        grupo.append(element)
                        self.datos_separados.siempre_LNorte.remove(element)
                    grupo.append("Siempre")
                    self.grupos_LNorte.append(grupo)

                elif len(self.datos_separados.siempre_LNorte) == 3 or len(
                        self.datos_separados.siempre_LNorte) == 2:
                    grupo = []
                    for element in self.datos_separados.siempre_LNorte:
                        grupo.append(element)
                    for element in grupo:
                        self.datos_separados.siempre_LNorte.remove(element)
                    grupo.append("Siempre")
                    self.grupos_LNorte.append(grupo)

                elif len(self.datos_separados.siempre_LNorte) == 1:
                    grupo = []
                    selection = self.datos_separados.siempre_LNorte[0]
                    grupo.append(self.datos_separados.siempre_LNorte[0])
                    self.datos_separados.siempre_LNorte.remove(selection)
                    grupo.append("Siempre")
                    self.grupos_LNorte.append(grupo)

                else:
                    print("ERROR: No se pudieron crear los grupos")
                    exit(-1)

        while len(self.datos_separados.siempre_LSur) != 0:
            finish = False
            while not finish:
                if len(self.datos_separados.siempre_LSur) == 0:
                    break
                finish = True
                for equipo in self.grupos_LSur:
                    if equipo[-1] == "Por la tarde" and (len(equipo) == 2 or len(equipo) == 3):
                        if len(self.datos_separados.siempre_LSur) == 0:
                            break
                        removed = equipo.pop(-1)
                        introduced = self.datos_separados.siempre_LSur[0]
                        equipo.append(introduced)
                        equipo.append(removed)
                        self.datos_separados.siempre_LSur.remove(introduced)
                        finish = False
            finish = False
            if len(self.datos_separados.siempre_LSur) != 0:
                while not finish:
                    if len(self.datos_separados.siempre_LSur) == 0:
                        break
                    finish = True
                    for equipo in self.grupos_LSur:
                        if equipo[-1] == "Por la noche" and (len(equipo) == 2 or len(equipo) == 3):
                            if len(self.datos_separados.siempre_LSur) == 0:
                                break
                            removed = equipo.pop(-1)
                            introduced = self.datos_separados.siempre_LSur[0]
                            equipo.append(introduced)
                            equipo.append(removed)
                            self.datos_separados.siempre_LSur.remove(introduced)
                            finish = False
            finish = False
            if len(self.datos_separados.siempre_LSur) != 0:
                while not finish:
                    if len(self.datos_separados.siempre_LSur) == 0:
                        break
                    finish = True
                    for equipo in self.grupos_LSur:
                        if equipo[-1] == "Por la mañana" and (len(equipo) == 2 or len(equipo) == 3):
                            if len(self.datos_separados.siempre_LSur) == 0:
                                break
                            removed = equipo.pop(-1)
                            introduced = self.datos_separados.siempre_LSur[0]
                            equipo.append(introduced)
                            equipo.append(removed)
                            self.datos_separados.siempre_LSur.remove(introduced)
                            finish = False

            if len(self.datos_separados.siempre_LSur) != 0:
                if len(self.datos_separados.siempre_LSur) > 4:
                    grupo = []
                    for i in range(0, 3):
                        selection = random.choice(self.datos_separados.siempre_LSur)
                        grupo.append(selection)
                        self.datos_separados.siempre_LSur.remove(selection)
                    grupo.append("Siempre")
                    self.grupos_LSur.append(grupo)

                elif len(self.datos_separados.siempre_LSur) == 4:
                    grupo = []
                    for i in range(0, 2):
                        selection = random.choice(self.datos_separados.siempre_LSur)
                        grupo.append(selection)
                        self.datos_separados.siempre_LSur.remove(selection)
                    grupo.append("Siempre")
                    self.grupos_LSur.append(grupo)

                    grupo = []
                    for element in self.datos_separados.siempre_LSur:
                        grupo.append(element)
                        self.datos_separados.siempre_LSur.remove(element)
                    grupo.append("Siempre")
                    self.grupos_LSur.append(grupo)

                elif len(self.datos_separados.siempre_LSur) == 3 or len(
                        self.datos_separados.siempre_LSur) == 2:
                    grupo = []
                    for element in self.datos_separados.siempre_LSur:
                        grupo.append(element)
                    for element in grupo:
                        self.datos_separados.siempre_LSur.remove(element)
                    grupo.append("Siempre")
                    self.grupos_LSur.append(grupo)

                elif len(self.datos_separados.siempre_LSur) == 1:
                    grupo = []
                    selection = self.datos_separados.siempre_LSur[0]
                    grupo.append(self.datos_separados.siempre_LSur[0])
                    self.datos_separados.siempre_LSur.remove(selection)
                    grupo.append("Siempre")
                    self.grupos_LSur.append(grupo)

                else:
                    print("ERROR: No se pudieron crear los grupos")
                    exit(-1)

    def crear_prefabricados(self,prefabricados):
        """Función para agrupar la gente que ya tiene equipo prefabricado"""
        for element in prefabricados:
            grupo = []
            for persona in element:
                if len(persona) != 1:
                    grupo.append(persona)
            self.grupos_Prefabricados.append(grupo)

    def recuento_distribuidos(self):
        """Función para contar todas las personas que tienen algún equipo"""
        total = 0

        for equipo in self.grupos_EMEA:
            total += len(equipo) - 1

        for equipo in self.grupos_LNorte:
            total += len(equipo) - 1

        for equipo in self.grupos_LSur:
            total += len(equipo) - 1

        return total



