from datetime import datetime

#En este archivo proceso el ingreso de datos de los empleados:

def ingresar_datos_empleados():
    print('Datos del ingresante')
    nombre = input(f'Ingrese el Nombre del Empleado: ')
    apellido = input(f'Ingrese el Apellido de {nombre}: ')
    s_base = float(input(f'Cual es el Salario Mensual Base de {nombre}?: '))
    afp1_o_2 = int(input(f'Ingrese 1 si {nombre} está afiliado a AFP1 o 2 si está afiliado a AFP2: '))
    pago_afp = None
    if afp1_o_2 == 1:
        pago_afp = (s_base/100)*12
        afp1_o_2 = 'AFP1'
    elif afp1_o_2 == 2:
        pago_afp = (s_base / 100) * 11.4
        afp1_o_2 = 'AFP2'
    else:
        print('Por favor, ingrese solamente 1 o 2, de acuerdo a su AFP')
    ingreso = ""
    try:
        ingreso = input(f'Usando el formato dd-mm-aaaa, indique la fecha de Ingreso: ')
        if int(ingreso[:2]) <= 31 and int(ingreso[3:5]) <= 12  and 1920<int(ingreso[6:10])<2024:
            ingreso = ingreso
        else:
            print(f'Asegurese de estar usando el formato correcto: dd-mm-aa, con -dd- igual al día,'
                      f'-mm- igual al mes y -aaaa- igual al año')
    except ValueError:
        print ('Por favor, use un formato de fecha válido: dd-mm-aaaa.')
    fecha_ingreso = datetime.strptime(ingreso, '%d-%m-%Y')
    hijos = int(input(f'Indique cuantos hijos menores de 18 años tiene {nombre}: '))
    fecha_ingreso = datetime.strptime(ingreso, '%d-%m-%Y')
    # Acá se recibe un objeto datetime. Calculamos la fecha de hoy en formato dd-mm-yyyy...
    fecha_hoy = datetime.now()
    # Calculo la diferencia en meses
    diferencia_meses = (fecha_hoy.year - fecha_ingreso.year) * 12 + (fecha_hoy.month - fecha_ingreso.month)
    factor = 1
    if diferencia_meses <100:
        factor = (diferencia_meses/100)
    else:
        factor = 0
    bonifica = s_base*(1+factor)
    asigna=((s_base / 100) * 5) * hijos
    pago_fonasa = (s_base/100)*7
    base_imponible = int(s_base + bonifica + asigna)
    return [nombre, apellido, s_base, afp1_o_2, fecha_ingreso, hijos, bonifica, asigna, pago_fonasa, pago_afp,
            base_imponible]