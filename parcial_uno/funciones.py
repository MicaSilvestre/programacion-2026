import random

def crear_patente(cant_letras_inicio: int, cant_numeros: int, cant_letras_final: int) -> str:
    """
    Genera una patente aleatoria por medio del código ASCII, combinando letras y números según las cantidades 
    ingresadas por parámetro (pudiéndose repetir caracteres).\n
    Parámetros:\n
        - cant_letras_inicio (int): cantidad de letras (mayúsculas) generadas aleatoriamente para el inicio de la patente.
        - cant_numeros (int): cantidad de números generados aleatoriamente para el centro de la patente.
        - cant_letras_final (int): cantidad de letras (mayúsculas) generadas aleatoriamente para el final de la patente.\n
    Return:\n
        - str: retorna una cadena de caracteres, siendo esta la patente creada aleatoriamente.
    """
    
    patente = ""

    for inicio in range(cant_letras_inicio):
        numeros = random.randint(65, 90)
        letras = chr(numeros)
        patente += letras

    for num in range(cant_numeros):
        numeros = random.randint(0, 9)
        patente += str(numeros)

    for fin in range(cant_letras_final):
        numeros = random.randint(65, 90)
        letras = chr(numeros)
        patente += letras

    return patente



def buscar_patente_repetida(lista: list, patente_buscada: str) -> bool:
    """
    Recorre una lista para verificar si la patente buscada ya se encuentra en ella.\n
    Parámetros:\n
        - lista (list): lista en la cual se buscará la existencia de la patente.
        - patente_buscada (str): patente que se va a buscar en la lista.\n
    Return:\n
        - bool: retorna True si encontró que la patente se repite en la lista o se mantiene en False en caso contrario.
    """
    encontrada = False

    for i in range(len(lista)):
        if lista[i] == patente_buscada:
            encontrada = True

    return encontrada



def transformar_a_mayusculas(cadena: str) -> str:
    """
    Transforma las letras minúsculas en mayúsculas segun el código ASCII.\n
    Parámetros:\n
        - cadena (str): la cadena de caracteres que se quiere transformar.\n
    Return:\n
        - str: retorna la cadena ya modificada a mayúsculas.
    """
    resultado = ""

    for i in range(len(cadena)):
        if cadena[i] >= "a" and cadena[i] <= "z":
            resultado += chr(ord(cadena[i]) - 32) 
        else:
            resultado += cadena[i]

    return resultado


def validar_ingreso_cantidad_patentes(cadena: str) -> bool:
    """Valida por medio del código ASCII que el usuario haya ingresado un número cuando se solicita la cantidad de patentes por crear, y no una letra.\n
    Parámetros:\n
    - cadena (str): cadena de caracteres para validar.\n
    Return:\n
        - bool: retorna True si todos los caracteres son numeros o False si alguno no lo es.
    """
    valido = True

    for i in range(len(cadena)):
        cadena_ord = ord(cadena[i])

        if cadena_ord < 48 or cadena_ord > 57:
            valido = False

    return valido



def validar_formato_patente(patente: str) -> bool:
    """Valida que la patente cumpla estrictamente con el formato LLNNNLL (L: letra | N: número).\n
    Parámetros:\n
    - patente (str): la patente que se desea validar.\n
    Return:\n
        - bool: retorna True si la patetnte tiene el formato correcto o False si el formato es incorrecto.
    """
    formato_valido = True

    if patente[0] < "A" or patente[0] > "Z" or patente[1] < "A" or patente[1] > "Z" or (
        patente[2] < "0" or patente[2] > "9" or patente[3] < "0" or patente[3] > "9" or patente[4] < "0" or patente[4] > "9") or (
        patente[-2] < "A" or patente[-2] > "Z" or patente[-1] < "A" or patente[-1] > "Z"):

        formato_valido = False

    return formato_valido



def buscar_mayor_menor_patente(lista: list, criterio: str) -> str:
    """Busca la patente que sea menor o mayor (según lo que se ingrese en el criterio) dentro de una lista.
    Teniendo en cuenta que solo se toman los números del centro de la pantente como indicador para determinarlo.\n
    Parámetros:\n
    - lista (list): la lista en la cual se va a buscar el elemento de mayor o menor valor.
    - criterio (str): que elemento se desea buscar, (debe ser estrictamente "MAYOR" / "MENOR" en mayúscula).\n
    Return:\n
        - str: retorna la patente obtenida según el criterio ingresado.
    """
    patente_resultado = lista[0]

    numero_patente_resultado = patente_resultado[2] + patente_resultado[3] + patente_resultado[4]

    for i in range(len(lista)):
        patente_original = lista[i]
        numero_patente_original = patente_original[2] + patente_original[3] + patente_original[4]

        if criterio == "MAYOR":
            if numero_patente_original > numero_patente_resultado:
                patente_resultado = patente_original
                numero_patente_resultado = numero_patente_original

        if criterio == "MENOR":
            if numero_patente_original < numero_patente_resultado:
                patente_resultado = patente_original
                numero_patente_resultado = numero_patente_original

    return patente_resultado



def crear_lista_abecedario(inicio: str, final: str) -> list:
    """
    Crea una lista del abecedario en mayúscula (sin caracteres especiales) 
    mediante el rango ingresado por parámetro según el código ASCII.\n
    Parámetros:\n
    - inicio (str): a partir de que letra se quiere crear el abecedario.
    - final (str): hasta que letra se quiere crear el abecedario.\n
    Return:\n
        - list: retorna la lista del abecedario creado, según los parámetros ingresados.
    """
    lista_abecedario = []

    inicio_ord = ord(inicio)
    final_ord = ord(final) + 1

    for i in range(inicio_ord, final_ord):
        letra = chr(i)
        lista_abecedario += [letra]

    return lista_abecedario



def calcular_porcentaje(dividendo: int, divisor: int) -> float:
    """
    Calcula el porcentaje de dos números enteros.\n
    Parámetros:\n
    - dividendo (int): el número que va a ser dividido.
    - divisor (int): el número que va a dividir al dividendo.\n
    Return:\n
        - float: retorna el porcentaje de esa división.
    """
    porcentaje = (dividendo / divisor) * 100

    return porcentaje



def contar_por_primera_letra(lista: list, letra_buscada: str) -> int:
    """
    Recorre la lista ingresada por parametro y cuenta cuantas empiezan con la letra indicada en el segundo parámetro.\n
    Parámetros:\n
    - lista (list): la lista en la cual se va a realizar la busqueda (teniendo en cuenta solo la primera letra).
    - letra_buscada (str): la letra que se desea buscar.\n
    Return:\n
        - int: retorna la cantidad de veces que se encontró esa letra.
    """
    contador = 0

    for i in range(len(lista)):
        patente = lista[i]

        if patente[0] == letra_buscada:
            contador += 1
            
    return contador



def intercambiar_elementos(lista: list, i: int, j: int) -> None:
    """Intercambia dos elementos de una lista usando una variable auxiliar.\n
    Parámetros:\n
    - lista (list): la lista en la cual se va a realizar el cambio de elementos.
    - i (int): el indice del primer elemento que se desea intercambiar.
    - j (int): el indice del segundo elemento que se desea intercambiar.\n
    Return:\n
        - None
    """
    aux = lista[i]
    lista[i] = lista[j] 
    lista[j] = aux



def ordenar_lista(lista: list, criterio: str) -> bool:
    """Ordena la lista de patentes de forma ascendente o descendente (según criterio ingresado) utilizando el método de ordenamiento burbuja.\n
    Parámetros:\n
    - lista (list): la lista en la cual se va a realizar el orden.
    - criterio (str): el que indica si va a ir de forma ascendente o descendente (debe ser estrictamente "ASC" / "DESC" en mayúscula).\n
    Return:\n
        - bool: retorna True si la lista se pudo ordenar, y False si no se pudo ordenar debido a que hay menos de dos elementos y no se pueda realizar dicha comparación.
    """
    bandera_orden = True

    for i in range(len(lista) - 1): 
        for j in range(i + 1, len(lista)):
            if (criterio == "ASC" and lista[i] > lista[j]) or (criterio == "DESC" and lista[i] < lista[j]):
                intercambiar_elementos(lista, i, j) 

    return bandera_orden