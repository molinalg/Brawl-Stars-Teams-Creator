import os
import time
from api_managers.connect_excel import Connect_Sheet
from file_extractions.csv_creator import Csv_Creator
from api_managers.bs_api_caller import BS_API
from validador.validador import Validador

#---------------------------------------------------------------------------------------
#Borrar archivos json de los miembros de los clubes
if os.path.isfile("A_json.json"):
    os.remove("A_json.json")
if os.path.isfile("B_json.json"):
    os.remove("B_json.json")
if os.path.isfile("C_json.json"):
    os.remove("C_json.json")
#Borrar archivo csv del excel del formulario
if os.path.isfile("csv_sheet.csv"):
    os.remove("csv_sheet.csv")

print("Limpieza de archivos completada")
#---------------------------------------------------------------------------------------
#Extraer datos del excel del formulario

#Conectarse al google sheet del formulario
sheet = Connect_Sheet("SHEET").connect_google_sheet(1) # ADD YOUR OWN SHEET

#Generar archivo con csv
creator_csv = Csv_Creator(sheet).crear_csv('csv_sheet.csv')

print("Archivo csv del excel generado")
#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------
#Extraer datos de los miembros de los clubes

#Generar archivos json con los miembros
bs_api = BS_API()
bs_api.connect_api()

print("Archivos Json de los clubes generados")
#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------
#Generar lista con las filas del csv
from file_readers.csv_reader import Csv_Reader
data = Csv_Reader("csv_sheet.csv").read_csv()

print("Lista con filas del excel generada")

#---------------------------------------------------------------------------------------
#Validamos los datos
Validador(data)

#Generar listas con tags de los miembros de cada club
from file_readers.json_reader import Json_Reader
tags_A = Json_Reader("A_json.json").read_json()
tags_B = Json_Reader("B_json.json").read_json()
tags_C = Json_Reader("C_json.json").read_json()

print("Listas con tags de los miembros generada")
#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------
#Extraer datos que corresponden a cada club
añadir_A = []
añadir_B = []
añadir_C = []

for line in data:
    if line[2] in tags_A:
        añadir_A.append(line)
        tags_A.remove(line[2])
    elif line[2] in tags_B:
        añadir_B.append(line)
        tags_B.remove(line[2])
    elif line[2] in tags_C:
        añadir_C.append(line)
        tags_C.remove(line[2])

print("Datos separados por clubes")
#---------------------------------------------------------------------------------------

#Esperar unos segundos para que la API no se sobrecargue
time.sleep(45)

#---------------------------------------------------------------------------------------
#Abrir las hoja de calculo para escritura y escribir las listas correspondientes
from gspread_formatting import *
#Definir y formatear encabezado
encabezado = ["Fecha Formulario","TAG BS","Nombre BS","Discord","Región","Horario","Detalles"]

formatData = cellFormat(
    backgroundColor=color(0, 0, 0),
    textFormat=textFormat(bold=True, foregroundColor=color(1, 1, 1),fontSize=11),
    horizontalAlignment='CENTER'
    )

formatData2 = cellFormat(
    backgroundColor=color(1, 1, 1),
    textFormat=textFormat(bold=False, foregroundColor=color(0, 0, 0),fontSize=10),
    horizontalAlignment='CENTER'
    )

#Abrir hoja para el A
sheet_A = Connect_Sheet("SHEET").connect_google_sheet("Club A") # ADD YOUR OWN SHEET
sheet_A.clear()

#Insertar y formatear encabezado
sheet_A.insert_row(encabezado,1)
format_cell_ranges(sheet_A, [('A1:G1', formatData), ('A2:G31', formatData2)])

counter = 2
for miembro in añadir_A:
    sheet_A.insert_row(miembro[1:],counter)
    counter += 1

print("Miembros del A ordenados: {}".format(len(añadir_A)))

#---------------------------------------------------------------------------------------

#Esperar unos segundos para que la API no se sobrecargue
time.sleep(45)

#---------------------------------------------------------------------------------------

#Abrir hoja para el B
sheet_B = Connect_Sheet("SHEET").connect_google_sheet("Club B")
sheet_B.clear()

#Insertar y formatear encabezado
sheet_B.insert_row(encabezado,1)
format_cell_ranges(sheet_B, [('A1:G1', formatData), ('A2:G31', formatData2)])

counter = 2
for miembro in añadir_B:
    sheet_B.insert_row(miembro[1:],counter)
    counter += 1

print("Miembros del B ordenados: {}".format(len(añadir_B)))

#---------------------------------------------------------------------------------------

#Esperar unos segundos para que la API no se sobrecargue
time.sleep(45)

#---------------------------------------------------------------------------------------

#Abrir hoja para el C
sheet_C = Connect_Sheet("SHEET").connect_google_sheet("Club C") # ADD YOUR OWN SHEET
sheet_C.clear()

#Insertar y formatear encabezado
sheet_C.insert_row(encabezado,1)
format_cell_ranges(sheet_C, [('A1:G1', formatData), ('A2:G31', formatData2)])

counter = 2
for miembro in añadir_C:
    sheet_C.insert_row(miembro[1:],counter)
    counter += 1

print("Miembros del C ordenados: {}".format(len(añadir_C)))
#---------------------------------------------------------------------------------------
#Rellenar datos en la ficha de información

#Abrimos la hoja de información
sheet_info = Connect_Sheet("SHEET").connect_google_sheet("Información") # ADD YOUR OWN SHEET

#Generamos fecha actual e insertamos
import datetime
fecha = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
sheet_info.update_cell(3,2,fecha)

#Insertamos la información sobre las personas presentes y faltantes
total_present = len(añadir_A) + len(añadir_B) + len(añadir_C)
sheet_info.update_cell(5,2,total_present)
sheet_info.update_cell(6,2,len(añadir_A))
sheet_info.update_cell(7,2,len(añadir_B))
sheet_info.update_cell(8,2,len(añadir_C))

total_remaining = len(tags_A) + len(tags_B) + len(tags_C)
sheet_info.update_cell(10,2,total_remaining)
sheet_info.update_cell(12,2,len(tags_A))
sheet_info.update_cell(17,2,len(tags_B))
sheet_info.update_cell(22,2,len(tags_C))

#Obtener nombres de los que faltan e insertarlos en la hoja de cálculo
from file_readers.json_reader import Json_Reader

all_names_A = Json_Reader("A_json.json").get_all_names(tags_A)
all_names_B = Json_Reader("B_json.json").get_all_names(tags_B)
all_names_C = Json_Reader("C_json.json").get_all_names(tags_C)

names_A, input_A = Json_Reader("A_json.json").get_names(tags_A)
names_B, input_B = Json_Reader("B_json.json").get_names(tags_B)
names_C, input_C = Json_Reader("C_json.json").get_names(tags_C)

all_remain_A = ", ".join(all_names_A)
all_remain_B = ", ".join(all_names_B)
all_remain_C = ", ".join(all_names_C)

remain_A = ", ".join(names_A[0])
remain_B = ", ".join(names_B[0])
remain_C = ", ".join(names_C[0])

remain_old_A = ", ".join(names_A[1])
remain_old_B = ", ".join(names_B[1])
remain_old_C = ", ".join(names_C[1])

from file_readers.procesados_controller import Procesados_Controller
procesador = Procesados_Controller()

procesador.rellenar_personas(input_A)
procesador.rellenar_personas(input_B)
procesador.rellenar_personas(input_C)
procesador.actualizar_procesados()

#Escribir todos los que faltan
sheet_info.update_cell(12,3,all_remain_A)
sheet_info.update_cell(17,3,all_remain_B)
sheet_info.update_cell(22,3,all_remain_C)

#Escribir todos los que faltan no repetidos
sheet_info.update_cell(14,3,remain_A)
sheet_info.update_cell(19,3,remain_B)
sheet_info.update_cell(24,3,remain_C)

#Escribir todos los que faltan repetidos
sheet_info.update_cell(15,3,remain_old_A)
sheet_info.update_cell(20,3,remain_old_B)
sheet_info.update_cell(25,3,remain_old_C)
#---------------------------------------------------------------------------------------

print("-----PROCESO DE ORGANIZACIÓN DEL EXCEL COMPLETADO-----")
