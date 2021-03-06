
import random
from turtle import position


def choose_secret( filename ):
    """Dado un nombre de fichero, esta función devuelve una palabra aleatoria de este fichero transformada a mayúsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayúsculas. Ej. "CREMA"
    """
    palabra = ""
    with open(filename, mode="rt", encoding="utf-8") as f:
      palabras = list(f)
      if len(palabras) == 0:
        raise ValueError("El fichero no tiene palabras")
      palabra = random.choice(palabras).upper()

    return palabra

def compare_words(word, secret):
    """Dadas dos palabras en mayúsculas (word y secret), esta función calcula las posiciones de las letras de word que aparecen en la misma posición en secret, y las posiciones de las letras de word que aparecen en secret pero en una posición distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posición en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras están en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """
    
    if len(word) != len(secret):
      raise ValueError("La longitud de las palabras no son iguales")

    same_position = [] # las letras están en la misma posición que secret
    same_letter = [] # las letras de word estan en secret pero en diferente posición

    posicionWord = 0
    

    for letraWord in word:
      posicionSecret = 0
      for letraSecret in secret:
        if letraWord == letraSecret and posicionWord == posicionSecret:
          same_position.append(posicionSecret)
        elif letraWord == letraSecret:
          same_letter.append(posicionSecret)
        posicionSecret += 1
        
      posicionWord += 1

    return same_position, same_letter


def print_word(word, same_letter_position, same_letter):
    """Dada una palabra, una lista same_position y otra lista same_letter, esta función creará un string donde aparezcan en mayúsculas las letras de la palabra que ocupen las posiciones de same_position, en minúsculas las letras de la palabra que ocupen las posiciones de same_letter y un guión (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """
    posicion = 0
    transformed = "-----"

    if type(same_letter_position) != list or type(same_letter) != list:
      raise ValueError("Los valores same tiene que ser listas")


    print("Posicion igual = " + str(same_letter_position))
    print("Posicion distinta = " + str(same_letter))

    for i in same_letter_position:
      if i < 0:
        raise ValueError("No se pueden introducir valores negativos")
      if i > len(word)-1:
        raise ValueError("No se pueden introducir valores mayores a la longitud de la palabra")
      if i == 0:
        transformed = word[i] + transformed[i+1:]
      elif i == len(transformed):
        transformed = transformed[:i-1] + word[i]
      else:
        transformed = transformed[:i] + word[i] + transformed[i+1:]
    

    # for i in same_letter:
    #   if i == 0:
    #     transformed = word[i].lower() + transformed[i+1:]
    #   elif i == len(transformed):
    #     transformed = transformed[:i-1] + word[i].lower()
    #   else:
    #     transformed = transformed[:i] + word[i].lower() + transformed[i+1:]
    

    return transformed


    
def choose_secret_advanced():
    """Dado un nombre de fichero, esta función filtra solo las palabras de 5 letras que no tienen acentos (á,é,í,ó,ú). De estas palabras, la función devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayúsculas
    """
 
def check_valid_word():
    """Dada una lista de palabras, esta función pregunta al usuario que introduzca una palabra hasta que introduzca una que esté en la lista. Esta palabra es la que devolverá la función.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que está en la lista.
    """

if __name__ == "__main__":
    try:
      secret=choose_secret("palabras_reduced.txt")
      print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
      for repeticiones in range(0,6):
          word = input("Introduce una nueva palabra: ")
          same_position, same_letter = compare_words( word.upper(), secret )
          resultado=print_word(word.upper(), same_position, same_letter)
          print(resultado)
          if word == secret:
              print("HAS GANADO!!")
              exit()
      print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)  
    except Exception as e:
      print("ERROR: " + str(e))
