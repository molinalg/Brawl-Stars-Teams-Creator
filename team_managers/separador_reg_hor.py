# Clase para separar a los miembros del club según su region horaria
class Separador_Reg_Hor():
    def __init__(self,datos,letra):
        self.datos = datos
        self.codig = "EQ" + letra
        self.separar_reg_hor()
        self.total = self.total_separados()

    def separar_reg_hor(self):
        """Función para separar a los miembros según su región horaria y si tienen un equipo predefinido o no"""
        mañanas_EMEA, mañanas_LSur, mañanas_LNorte = [], [], []
        tardes_EMEA, tardes_LSur, tardes_LNorte = [], [], []
        noches_EMEA, noches_LSur, noches_LNorte = [], [], []

        mañanas_tardes_EMEA, mañanas_tardes_LSur, mañanas_tardes_LNorte = [], [], []
        mañanas_noches_EMEA, mañanas_noches_LSur, mañanas_noches_LNorte = [], [], []
        tardes_noches_EMEA, tardes_noches_LSur, tardes_noches_LNorte = [], [], []

        siempre_EMEA, siempre_LSur, siempre_LNorte = [], [], []

        prefabricados = []

        # Se separan los grupos prefabricados del resto de personas
        for persona in self.datos:
            if persona[-1][0:3] == self.codig and persona[-1][3] == "[":
                try:
                    i1 = persona[-1].index("[")
                    i2 = persona[-1].index("]")
                except:
                    print("--ERROR: Ha habido un problema identificando equipos prefabricados--")
                    exit(-1)

                identificador = persona[-1][i1+1:i2]
                asignado = False
                for element in prefabricados:
                    if element[0] == identificador:
                        if len(element) >= 4:
                            print("--ERROR: Se han detectado demasiadas personas con el identificador {}--".format(identificador))
                            exit(-1)
                        element.append(persona)
                        asignado = True

                if not asignado:
                    prefabricados.append([identificador])
                    prefabricados[-1].append(persona)

        eliminar = []
        for grupo in prefabricados:
            if len(grupo) >= 3:
                for integrante in grupo:
                    if len(integrante) != 1:
                        self.datos.remove(integrante)
            else:
                eliminar.append(grupo)

        for sobrante in eliminar:
            prefabricados.remove(sobrante)


        for persona in self.datos:
            if persona[6] == "Por la mañana":
                if persona[5] == "EMEA":
                    mañanas_EMEA.append(persona)
                elif persona[5] == "NA & LATAM N":
                    mañanas_LNorte.append(persona)
                elif persona[5] == "LATAM S":
                    mañanas_LSur.append(persona)
                else:
                    print("ERROR: Algo ha pasado chequeando la región de un miembro")
                    print("Región detectada: {}".format(persona[5]))
                    exit(-1)

            elif persona[6] == "Por la tarde":
                if persona[5] == "EMEA":
                    tardes_EMEA.append(persona)
                elif persona[5] == "NA & LATAM N":
                    tardes_LNorte.append(persona)
                elif persona[5] == "LATAM S":
                    tardes_LSur.append(persona)
                else:
                    print("ERROR: Algo ha pasado chequeando la región de un miembro")
                    print("Región detectada: {}".format(persona[5]))
                    exit(-1)

            elif persona[6] == "Por la noche":
                if persona[5] == "EMEA":
                    noches_EMEA.append(persona)
                elif persona[5] == "NA & LATAM N":
                    noches_LNorte.append(persona)
                elif persona[5] == "LATAM S":
                    noches_LSur.append(persona)
                else:
                    print("ERROR: Algo ha pasado chequeando la región de un miembro")
                    print("Región detectada: {}".format(persona[5]))
                    exit(-1)

            elif persona[6] == '"""Por la tarde, Por la noche"""':
                if persona[5] == "EMEA":
                    tardes_noches_EMEA.append(persona)
                elif persona[5] == "NA & LATAM N":
                    tardes_noches_LNorte.append(persona)
                elif persona[5] == "LATAM S":
                    tardes_noches_LSur.append(persona)
                else:
                    print("ERROR: Algo ha pasado chequeando la región de un miembro")
                    print("Región detectada: {}".format(persona[5]))
                    exit(-1)

            elif persona[6] == '"""Por la mañana, Por la noche"""':
                if persona[5] == "EMEA":
                    mañanas_noches_EMEA.append(persona)
                elif persona[5] == "NA & LATAM N":
                    mañanas_noches_LNorte.append(persona)
                elif persona[5] == "LATAM S":
                    mañanas_noches_LSur.append(persona)
                else:
                    print("ERROR: Algo ha pasado chequeando la región de un miembro")
                    print("Región detectada: {}".format(persona[5]))
                    exit(-1)

            elif persona[6] == '"""Por la mañana, Por la tarde"""':
                if persona[5] == "EMEA":
                    mañanas_tardes_EMEA.append(persona)
                elif persona[5] == "NA & LATAM N":
                    mañanas_tardes_LNorte.append(persona)
                elif persona[5] == "LATAM S":
                    mañanas_tardes_LSur.append(persona)
                else:
                    print("ERROR: Algo ha pasado chequeando la región de un miembro")
                    print("Región detectada: {}".format(persona[5]))
                    exit(-1)

            elif persona[6] == '"""Por la mañana Por la tarde Por la noche"""':
                if persona[5] == "EMEA":
                    siempre_EMEA.append(persona)
                elif persona[5] == "NA & LATAM N":
                    siempre_LNorte.append(persona)
                elif persona[5] == "LATAM S":
                    siempre_LSur.append(persona)
                else:
                    print("ERROR: Algo ha pasado chequeando la región de un miembro")
                    print("Región detectada: {}".format(persona[5]))
                    exit(-1)

        self.mañanas_EMEA = mañanas_EMEA
        self.tardes_EMEA = tardes_EMEA
        self.noches_EMEA = noches_EMEA
        self.mañanas_tardes_EMEA = mañanas_tardes_EMEA
        self.mañanas_noches_EMEA = mañanas_noches_EMEA
        self.tardes_noches_EMEA = tardes_noches_EMEA
        self.siempre_EMEA = siempre_EMEA

        self.mañanas_LNorte = mañanas_LNorte
        self.tardes_LNorte = tardes_LNorte
        self.noches_LNorte = noches_LNorte
        self.mañanas_tardes_LNorte = mañanas_tardes_LNorte
        self.mañanas_noches_LNorte = mañanas_noches_LNorte
        self.tardes_noches_LNorte = tardes_noches_LNorte
        self.siempre_LNorte = siempre_LNorte

        self.mañanas_LSur = mañanas_LSur
        self.tardes_LSur = tardes_LSur
        self.noches_LSur = noches_LSur
        self.mañanas_tardes_LSur = mañanas_tardes_LSur
        self.mañanas_noches_LSur = mañanas_noches_LSur
        self.tardes_noches_LSur = tardes_noches_LSur
        self.siempre_LSur = siempre_LSur

        self.prefabricados = prefabricados

    def total_separados(self):
        """Función que calcula cuanta gente hay disponible en cada parte del día"""
        total_mañanas = len(self.mañanas_EMEA) + len(self.mañanas_LNorte) + len(self.mañanas_LSur)
        total_tardes = len(self.tardes_EMEA) + len(self.tardes_LNorte) + len(self.tardes_LSur)
        total_noches = len(self.noches_EMEA) + len(self.noches_LNorte) + len(self.noches_LSur)
        total_siempre = len(self.siempre_EMEA) + len(self.siempre_LNorte) + len(self.siempre_LSur)
        total_mañanas_tardes = len(self.mañanas_tardes_EMEA) + len(self.mañanas_tardes_LNorte) + len(self.mañanas_tardes_LSur)
        total_mañanas_noches = len(self.mañanas_noches_EMEA) + len(self.mañanas_noches_LNorte) + len(self.mañanas_noches_LSur)
        total_tardes_noches = len(self.tardes_noches_EMEA) + len(self.tardes_noches_LNorte) + len(self.tardes_noches_LSur)

        total_prefabricados = 0
        for element in self.prefabricados:
            total_prefabricados = total_prefabricados + len(element) - 1

        total = total_mañanas+total_tardes+total_noches+total_siempre+total_mañanas_tardes+total_mañanas_noches+total_tardes_noches+total_prefabricados

        return total