def generar_estructura(names,goals,goals_avioded,assist):
    """Elegí generar la estructura de datos conformada por un diccionario con claves (keys) que representan 
    los nombres de los jugadores y valores (values) que son tuplas que contienen los goles, goles evitados y asistencias 
    de cada jugador. Esta estructura es la más legible y conveniente para ordenar, leer y manejar los datos, ya que 
    los datos no deben modificarse y son fijos durante la ejecución del programa.
    """
    keys=list(name.strip() for name in names.split(','))
    values=list(zip(goals,goals_avioded,assist))#Primero se crea una lista de tuplas con los datos, luego se combinan ambas listas en un diccionario.
    records=dict(zip(keys,values))
    return records