import json

# Clase para tratar con archivos JSON
class Json_Extractor():
    def __init__(self,data,name):
        self.data = data
        self.name = name

    def extract_json_from_dataframe(self):
        """Función para crear archivos JSON a partir de un dataframe"""
        json_file = self.data.to_json(orient='records')
        with open(self.name, 'w') as f:
            f.write(json_file)

    def extract_json(self):
        """Función para crear archivos JSON"""
        with open(self.name, 'w') as json_file:
            json.dump(self.data,json_file,indent=6)