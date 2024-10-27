import requests
from file_extractions.json_extractor import Json_Extractor

# Clase que se conecta a la API de Brawl Stars y recupera información de los clubes pedidos
class BS_API():
    def __init__(self):
        pass

    def connect_api(self):
        """Función que se conecta a la API y pide los datos de los 3 clubes"""
        URL_A = "https://api.brawlstars.com/v1/clubs/%TAG/members" # ADD THE CLUB TAG
        URL_B = "https://api.brawlstars.com/v1/clubs/%TAG/members" # ADD THE CLUB TAG
        URL_C = "https://api.brawlstars.com/v1/clubs/%TAG/members" # ADD THE CLUB TAG

        token = "NONE" # Añadir tu clave de la API de Brawl Stars

        json_A = self.generate_json(URL_A, token)
        json_B = self.generate_json(URL_B, token)
        json_C = self.generate_json(URL_C, token)

        json_name = "A_json.json"
        excel_extractor = Json_Extractor(json_A, json_name)
        excel_extractor.extract_json()

        json_name = "B_json.json"
        excel_extractor = Json_Extractor(json_B, json_name)
        excel_extractor.extract_json()

        json_name = "C_json.json"
        excel_extractor = Json_Extractor(json_C, json_name)
        excel_extractor.extract_json()

    def generate_json(self, URL, token):
        """Función para obtener los datos de los clubes a través de la API"""
        header = {'Authorization': "Bearer {}".format(token)}
        auth_response = requests.get(URL, headers=header)

        if auth_response.status_code != 200:
            print("ERROR: Los datos no pudieron ser generados (response code {})".format(auth_response.status_code))
            print("Detalles: {}".format(auth_response.json()))
            return

        else:
            print("Codigo de response {}. JSON generado correctamente".format(auth_response.status_code))
            return auth_response.json()
