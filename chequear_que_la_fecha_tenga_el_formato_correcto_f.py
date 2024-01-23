def verificar_formato_de_fecha():
    # la variable ingreso_interno es usada solamente en esta función
    ingreso_interno = input(f'Usando el formato dd-mm-aaaa, indique la fecha de Ingreso: ')
    while True:
        if int(ingreso_interno[:2]) <= 31 and int(ingreso_interno[3:5]) <= 12  and 1920<int(ingreso_interno[6:10])<2024:
            return ingreso_interno
        else:
            print(f'Asegurese de estar usando el formato correcto: dd-mm-aa, con -dd- igual al día,'
          f'-mm- igual al mes y -aaaa- igual al año')
            ingreso_interno = input(f'Usando el formato dd-mm-aaaa, indique la fecha de Ingreso: ')
    return ingreso_interno

#e = verificar_formato_de_fecha()
#print(e)
#print(type(e))