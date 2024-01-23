from datetime import datetime

# El parámetro es un string con formato dd-mm-yyyy.
# La fecha de ingreso ya fue verificada en una función previa

def calculo_de_bonificacion(ingreso):
    # Voy a convertir el string fecha_ingreso_str en un objeto datetime usando strptime #
    fecha_ingreso = datetime.strptime(ingreso, '%d-%m-%Y')
    #print(fecha_ingreso)
    #print(type(fecha_ingreso))
    # y esto me devuelve un objeto datetime.datetime #

    # Ahora, vamos con la fecha de hoy pero en formato dd-mm-yyyy...
    fecha_hoy = fechaActual=datetime.now()
    #print(fecha_hoy)
    #print(type(fecha_hoy))
    # hoy_str es un objeto datetime.datetime, así que la diferencia debería funcionar... #

    # Calcula la diferencia en meses
    diferencia_meses = (fecha_hoy.year - fecha_ingreso.year) * 12 + (fecha_hoy.month - fecha_ingreso.month)
    print(f'La diferencia en meses es: {diferencia_meses}')
    print(type(diferencia_meses))
    if diferencia_meses <100:
        return (diferencia_meses/100)
    else:
        return 0

# verificacion = calculo_de_bonificacion('12-10-2012')
# print(verificacion)