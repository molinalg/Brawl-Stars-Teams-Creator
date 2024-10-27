import pandas as pd
import csv

# Clase para crear archivos csv con datos de hojas de calculo de google
class Csv_Creator():
    def __init__(self, sheet):
        self.sheet = sheet

    def crear_csv(self,name):
        """Función para crear un csv con los datos"""
        # Crear dataframe con los datos del excel
        dataframe = pd.DataFrame(self.sheet.get_all_records())

        # Crear csv desde el dataframe
        csv_sheet = dataframe.to_csv()

        # Convertir csv en una lista
        list_of_rows = csv_sheet.split("\r\n")

        # Convertir lista en un matriz
        list_csv = []
        for element in list_of_rows:
            list_csv.append([element])

        # Crear y escribir csv
        with open(name, 'w', newline="", encoding='UTF-8') as file:
            writer = csv.writer(file, )
            writer.writerows(list_csv)
