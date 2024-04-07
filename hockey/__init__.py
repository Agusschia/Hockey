"""Elegi generar la estructura de datos conformado por: Un diccionario con claves que
son los nombres y su valor que es una lista de tuplas que contiene goles, goles
asistidos y asistencias por cada nombre de jugador (son tuplas debido a que los datos no deberian ser modificados), 
siendo la forma mas legible y comoda
Para ordenar, leer y manejar los datos"""
def generar_estructura(names,goals,goals_avioded,assist):
    keys=list(name.strip() for name in names.split(','))
    values=list(zip(goals,goals_avioded,assist))
    records=dict(zip(keys,values))
    return records

"""Las primeras versiones de esta funcion eran con muchas lineas o con mas de
un recorrido de la estructura, hasta que empece a ver de cerca la funcion max
ya que esta me permite encontar el valor maximo de un iterable (records.items()) con la funcion
opcional "key=" que me permite definir con que elemento determinara el maximo,
implementando la funcion lambda que se encarga de devolver
tanto el elemento para ser procesado por la funcion "max()" que son
los goles, ubicados en los valores del diccionario y primera posicion de la tupla(item[1][0])
como tambien guardar el nombre del goleador en cuestion"""
def obtener_goleador(records):
    goleador, max_goles = max(records.items(), key=lambda item: item[1][0])
    return goleador, max_goles