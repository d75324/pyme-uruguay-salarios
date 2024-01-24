import csv
import os
from funciones_complementarias import ingresar_datos_empleados

# La pyme tiene 10 empleados pero vamos a dar la opción de que tenga 2 para simplificar la carga:

cantidad_de_empleados = int(input('Hola, bienvenido. Cuantos empleados tiene su PYME?: '))
if cantidad_de_empleados == 1:
    print(f'Vamos a ingresar la información de ese empleado.')
else:
    print(f'Vamos a ingresar la información de esos {cantidad_de_empleados} empleados.')

tabla_de_empleados =    [
                            [
                                'Nombre',
                                'Apellido',
                                'Salario Base',
                                'AFP a la que pertenece',
                                'Ingreso',
                                'Cantidad Hijos a Cargo',
                                'Bonificacion',
                                'Asignacion',
                                'Pagar a FONASA',
                                'Pagar a AFP',
                                'Base Imponible'
                            ],
                        ]

for cantidad_de_empleados_for in range (cantidad_de_empleados):
    esclavo = ingresar_datos_empleados()
    tabla_de_empleados.append(esclavo)
print(tabla_de_empleados)

carpeta_destino = 'mi_pyme_box'
nombre_archivo = 'mi_pyme.csv'
ruta_completa = os.path.join('mi_pyme_box', 'mi_pyme.csv')

# Como la carpeta destino no existe, la creo:
if not os.path.exists('mi_pyme_box'):
    os.makedirs('mi_pyme_box')

# Defino la ruta:
ruta_completa = os.path.join('mi_pyme_box', 'mi_pyme.csv')

# Escribo la tabla en un archivo_CSV
with open(ruta_completa, 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    # Escribo cada fila de la tabla en el archivo CSV
    for fila in tabla_de_empleados:
        escritor_csv.writerow(fila)
