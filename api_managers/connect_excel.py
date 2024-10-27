import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Clase que utiliza la API de Google Sheets
class Connect_Sheet():
    def __init__(self,file):
        self.file = file

    def connect_google_sheet(self,op):
        """Función que organiza los datos para la conexión a la API y pide la conexión"""
        self.scopes = [
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/drive'
        ]
        self.credentials = "credentialsAPI.json" # ADD YOUR OWN CREDENTIALS FILE FOR THE GOOGLE SHEETS API

        # Sacar datos del excel
        if op == 1:
            sheet = self.extraer_datos()
        else:
            sheet = self.extraer_datos_por_worksheet(op)

        return sheet

    def extraer_datos(self):
        """Función que se conecta a la API y devuelve los datos de la primera hoja de una tabla de datos"""
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.credenciales,
                                                                       self.scopes)  # access the json key
        file = gspread.authorize(credentials)  # authenticate the JSON key with gspread
        sheet = file.open(self.file)  # open sheet
        sheet = sheet.sheet1
        return sheet

    def extraer_datos_por_worksheet(self,name):
        """Función que se conecta a la API y devuelve los datos de una hoja de una tabla de datos a partir de su nombre"""
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.credenciales,
                                                                       self.scopes)  # access the json key
        file = gspread.authorize(credentials)  # authenticate the JSON key with gspread
        sheet = file.open(self.file).worksheet(name)  # open sheet
        return sheet
