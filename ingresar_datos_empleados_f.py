# Función para ingresar los datos de los empleados #
# Devuelve una lista de listas con una serie de datos adicionales #

from chequear_que_la_fecha_tenga_el_formato_correcto_f import verificar_formato_de_fecha
from bonificacion_ddmmyyyy_f import calculo_de_bonificacion
from datetime import datetime

def ingresar_datos_empleados():
    print('Datos del ingresante')
    nombre = input(f'Ingrese el Nombre del Empleado: ')
    apellido = input(f'Ingrese el Apellido de {nombre}: ')
    s_base = float(input(f'Cual es el Salario Mensual Base de {nombre}?: '))
    afp1_o_2 = int(input(f'Ingrese 1 si {nombre} está afiliado a AFP1 o 2 si está afiliado a AFP2: '))
    pago_afp = None
    if afp1_o_2 == 1:
        pago_afp = (s_base/100)*12
    elif afp1_o_2 == 2:
        pago_afp = (s_base / 100) * 11.4
    else:
        print('Por favor, ingrese solamente 1 o 2, de acuerdo a su AFP')
    ingreso_str = verificar_formato_de_fecha()
    print(ingreso_str)
    ingreso = datetime.strptime(ingreso_str, '%d-%m-%Y')
    print(type(ingreso))
    bonifica = calculo_de_bonificacion(ingreso_str)
    hijos = int(input(f'Indique cuantos hijos menores de 18 años tiene {nombre}: '))
    asigna = ((s_base/100)*5)*hijos
    print(asigna)
    pago_fonasa = (s_base/100)*7
    return [nombre, apellido, s_base, afp1_o_2, ingreso, hijos, bonifica, asigna, pago_fonasa, pago_afp]

