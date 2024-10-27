import csv

# Clase para leer archivos CSV
class Csv_Reader():
    def __init__(self,file):
        self.file = file

    def read_csv(self):
        """Función para leer archivos CSV y convertirlos en listas"""
        data = []
        with open(self.file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for line in reader:
                appended = line[0].split(",")

                # Solucionando problema de formato csv cuando seleccionan mas de un horario:
                if len(appended) > 10:
                    print("ERROR: La fila en el proceso es demasiado larga")
                    return

                elif len(appended) < 8 and appended != ['']:
                    print("ERROR: La fila en el proceso es demasiado corta")
                    return

                elif len(appended) == 9:
                    appended2 = []
                    for i in range(0,6):
                        appended2.append(appended[i])
                    horario = appended[6] + "," + appended[7]
                    appended2.append(horario)
                    appended2.append(appended[8])

                    data.append(appended2)

                elif len(appended) == 10:
                    appended2 = []
                    for i in range(0,6):
                        appended2.append(appended[i])
                    horario = appended[6] + appended[7] + appended[8]
                    appended2.append(horario)
                    appended2.append(appended[9])

                    data.append(appended2)

                elif len(appended) == 8:
                    data.append(appended)

                else:
                    print("ERROR: Desconocido")

        return data
