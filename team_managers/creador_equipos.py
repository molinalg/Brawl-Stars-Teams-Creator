from api_managers.connect_excel import Connect_Sheet
from file_extractions.csv_creator import Csv_Creator
import os
import time

#---------------------------------------------------------------------------------------
#Borrar archivos csv de cada club antes de crear los nuevos

if os.path.isfile("csv_club_A.csv"):
    os.remove("csv_club_A.csv")
if os.path.isfile("csv_club_B.csv"):
    os.remove("csv_club_B.csv")
if os.path.isfile("csv_club_C.csv"):
    os.remove("csv_club_C.csv")

#---------------------------------------------------------------------------------------
#Extraer datos del excel del formulario

#Conectarse al google sheet del formulario
sheet = Connect_Sheet("SHEET").connect_google_sheet("Club A") # ADD YOUR OWN SHEET

#Generar archivo con csv
creator_csv = Csv_Creator(sheet).crear_csv('csv_club_A.csv')

print("Csv con los datos del A creado")
#---------------------------------------------------------------------------------------
#Extraer datos del excel del formulario

#Conectarse al google sheet del formulario
sheet = Connect_Sheet("SHEET").connect_google_sheet("Club B") # ADD YOUR OWN SHEET

#Generar archivo con csv
creator_csv = Csv_Creator(sheet).crear_csv('csv_club_B.csv')

print("Csv con los datos del B creado")
#---------------------------------------------------------------------------------------
#Extraer datos del excel del formulario

#Conectarse al google sheet del formulario
sheet = Connect_Sheet("SHEET").connect_google_sheet("Club C") # ADD YOUR OWN SHEET

#Generar archivo con csv
creator_csv = Csv_Creator(sheet).crear_csv('csv_club_C.csv')

print("Csv con los datos del C creado")
#---------------------------------------------------------------------------------------
#Generar listas con las filas de los csv
from file_readers.csv_reader import Csv_Reader
data_A = Csv_Reader("csv_club_A.csv").read_csv()
data_B = Csv_Reader("csv_club_B.csv").read_csv()
data_C = Csv_Reader("csv_club_C.csv").read_csv()

print("Listas con filas del excel generadas")
#---------------------------------------------------------------------------------------
#Separar lista de miembros segun su región y su horario

from team_managers.separador_reg_hor import Separador_Reg_Hor
datos_separados_A = Separador_Reg_Hor(data_A,"A")
print("Todos los miembros del A han sido divididos por region y horario: {}".format(datos_separados_A.total))
datos_separados_B = Separador_Reg_Hor(data_B,"B")
print("Todos los miembros del B han sido divididos por region y horario: {}".format(datos_separados_B.total))
datos_separados_C = Separador_Reg_Hor(data_C,"C")
print("Todos los miembros del C han sido divididos por region y horario: {}".format(datos_separados_C.total))

#---------------------------------------------------------------------------------------
#Crear equipos
from team_managers.organizador_equipos import Organizador_Equipos

organizador_A = Organizador_Equipos(datos_separados_A)
print("Equipos del A generados correctamente.\nTotal personas en equipo: {}".format(organizador_A.total))
time.sleep(2)
organizador_B = Organizador_Equipos(datos_separados_B)
print("Equipos del B generados correctamente.\nTotal personas en equipo: {}".format(organizador_B.total))
time.sleep(2)
organizador_C = Organizador_Equipos(datos_separados_C)
time.sleep(2)
print("Equipos del C generados correctamente.\nTotal personas en equipo: {}".format(organizador_C.total))

#---------------------------------------------------------------------------------------
#Crear mensaje con equipos
from team_managers.generador_mensajes import Generador_Mensajes

generador_mensajes = Generador_Mensajes(organizador_A,organizador_B,organizador_C)
message_A = generador_mensajes.generar_mensaje_A()
message_B = generador_mensajes.generar_mensaje_B()
message_C = generador_mensajes.generar_mensaje_C()

print("Mensajes con equipos generados correctamente")
#---------------------------------------------------------------------------------------
#Rellenar datos en la ficha de información

#Abrimos la hoja de información
sheet_equipos = Connect_Sheet("SHEET").connect_google_sheet("Equipos") # ADD YOUR OWN SHEET

#Generamos fecha actual e insertamos
import datetime
fecha = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
sheet_equipos.update_cell(3,2,str(fecha))

print("Última fecha actualizada")

#Insertamos los mensajes de los equipos
sheet_equipos.update_cell(5,2,message_A)
sheet_equipos.update_cell(6,2,message_B)
sheet_equipos.update_cell(7,2,message_C)

print("Mensajes escritos en el excel")

print("-----PROCESO DE CREACIÓN DE EQUIPOS COMPLETADO-----")





