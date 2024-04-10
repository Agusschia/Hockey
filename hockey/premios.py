"""
Las primeras versiones de esta función eran con muchas líneas o con más de un recorrido de la estructura, 
hasta que empecé a ver de cerca la función max, ya que esta me permite encontrar el valor máximo de un 
iterable (records.items()) con la función opcional "key=" que me permite definir con qué elemento determinará 
el máximo, implementando la función lambda que se encarga de devolver el elemento a ser procesado 
por la función "max()" (los goles, ubicados en los valores del diccionario y primera posición de la 
tupla(item[1][0])) para luego devolver el nombre en goleador y la posición 0 de la tupla que tiene los goles.
"""
def obtener_goleador(records):
    goleador, max_goles = max(records.items(), key=lambda item: item[1][0])
    return goleador, max_goles[0]

"""
De la misma manera que en el sub-inciso anterior, en este también opté por usar la función max() usando 
como criterio el resultado de la función lambda que devuelve, por cada elemento del diccionario 
(principalmente la tupla con todos sus datos), el promedio ponderado de cada jugador.
"""
def obtener_influyente(records):
    influyente= max(records.items(), key=lambda item: (item[1][0]*1.5+item[1][1]*1.25+item[1][2])/3)
    return influyente[0]

"""
Esta función recibe el registro de los jugadores y devuelve la suma de todos los goles del 
equipo, para luego dividirlo por el total de partidos. Utilizo "sum()" que suma todos los 
elementos de un iterable, que en este caso son las tuplas guardadas en los "values" del 
diccionario y accediendo particularmente a la posición 0 de la tupla, que son los goles. 
"""
def obtener_promedio_general(records):
    return sum(item[0] for item in records.values())/25

"""
En principio, iba a reutilizar la función del sub-inciso 2 (def obtener_goleador(records)) 
para obtener los goles, pero a su vez tendría que recibir el nombre, que para este sub-inciso no era útil. 
Por lo tanto, opté por recorrer el diccionario buscando únicamente en sus "values" para obtener 
únicamente la cantidad máxima de goles a promediar.
"""
def obtener_promedio_individual(records):
    max_goles=max(records.values(), key=lambda item: item[0])
    return max_goles[0]/25