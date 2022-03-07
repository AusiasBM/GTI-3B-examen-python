import random

def encontrar_menores(diccionario,letra):
    """Dado un diccionario de palabras, y una letra, esta función devuelve la lista de palabras que empiezan por una letra que alfabéticamente está antes que la indicada.
    Args:
      diccionario
      letra
    Returns:
      resultado: ej. ['AUNQUE','ABINAR']
    """
    # El erro se debe a que estaba limpiando el array en cada entrada de palabra nueva
    # Sacandolo fuera ya no se reace y se devuelve entero
    resultado=[]
    for clave in diccionario:
        for palabra in diccionario[clave]:
            if palabra[0] < letra:
                resultado.append(palabra)

    print(resultado)
    return resultado

def add_client(clients_list,nif,name,address,phone,email):
    """Dado un diccionario de clientes y datos de un nuevo cliente, esta función inserta estos datos como un nuevo cliente.
    Args:
      diccionario
      nif
      name 
      address
      phone
      email
    """
    # Se estaba metienedo un valor nif que tenenía la información del cliente
    # insertando la información del cliente directamente se arregla  
    clients_list[nif] = {'name': name,
              'address': address,
              'phone': phone,
              'email': email
        }
    

def repartir_cartas(cartas_iniciales,repeticiones):
    """Dada una baraja de cartas iniciales y un número de repeticiones, esta función selecciona 5 cartas aleatorias de esta baraja y las mete en un diccionario llamado combinaciones. El proceso se repite tantas veces como repeticiones se indiquen.
    Args:
      cartas_iniciales
      repeticiones
    Returns:
      combinaciones: ej. {'repeticion1': ['contable', 'alguacil', 'asesino', 'cardenal', 'obispo']}
    """    

    # El problema de este era en la 3 prueba, cuando intenta insertar 5 cartas en la última última vuelta
    # quitando la linia de remove ya quedan cartas para hacer la 3 vuelta

    combinaciones={}
    for i in range(1,repeticiones+1):
        cartas_aleatorias = cartas_iniciales 
        combinaciones["repeticion"+str(i)]=[]
        for j in range(0,5):
            carta=random.choice(cartas_aleatorias)
            combinaciones["repeticion"+str(i)].append(carta)
            #cartas_aleatorias.remove(carta)

    return combinaciones

    
