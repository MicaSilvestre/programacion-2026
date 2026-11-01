import random

def verificar_apuesta(apuesta: int, puntaje: int) -> bool:
    """
    Verifica que el puntaje alcance para cubrir la apuesta.\n
    Parámetros:\n
        - apuesta (int): apuesta actual.
        - puntaje (int): puntaje disponible del jugador.\n
    Retorna:\n
        - bool: True si la apuesta alcanza, False en caso contrario.
    """
    alcanza = True
 
    if apuesta > puntaje:
        alcanza = False
 
    return alcanza



def armar_mensaje_puntos_insuficientes(apuesta: int, puntaje: int) -> str:
    """
    Arma el mensaje que informa que el puntaje no alcanza para cubrir la apuesta.\n
    Parámetros:\n
        - apuesta (int): apuesta actual.
        - puntaje (int): puntaje disponible del jugador.\n
    Retorna:\n
        - str: mensaje de error para mostrar al jugador.
    """
    mensaje = f"""
    \n¡No te alcanzan los puntos para realizar esta jugada! (Tenés {puntaje} y tu apuesta es {apuesta}).
    Por favor, cambia tu apuesta (opción 3) o, precioná opción 4 para salir."""
 
    return mensaje



def verificar_apuesta_valida(apuesta: str, puntaje: int) -> bool:
    """
    Verifica que el texto sea un entero mayor o igual a 1 y que no supere el puntaje.\n
    Parámetros:\n
        - apuesta (str): apuesta ingresada por el usuario.
        - puntaje (int): puntaje disponible del jugador.\n
    Retorna:\n
        - bool: True si la apuesta es válida, False en caso contrario.
    """
    valida = True

    if apuesta == "":
        valida = False

    else:
        for caracter in apuesta:
            if caracter < "0" or caracter > "9":
                valida = False
                break

    if valida == True:
        numero = int(apuesta)

        if numero < 1 or numero > puntaje:
            valida = False

    return valida



def armar_mensaje_apuesta(apuesta: str, puntaje: int) -> str:
    """
    Arma el mensaje que informa si la apuesta ingresada fue aceptada.\n
    Parámetros:\n
        - apuesta (str): apuesta ingresada por el usuario.
        - puntaje (int): puntaje disponible del jugador.\n
    Retorna:\n
        - str: mensaje de éxito o de error según corresponda.
    """
    es_valida = verificar_apuesta_valida(apuesta, puntaje)

    if es_valida == True:
        mensaje = f"\n¡Apuesta actualizada con éxito! Nueva apuesta: {apuesta}"

    else:
        mensaje = f"\n¡ERROR! La apuesta debe ser mayor o igual a 1 y no puede superar tu puntaje ({puntaje})."

    return mensaje



#-------------------------------------- TRAGAMONEDAS ----------------------------------------------------------------------------

def generar_tirada(cant_caracteres: int = 3) -> list:
    """
    Genera una fila de cierta cantidad de caracteres aleatorios (por defecto es 3).\n
    Parámetros:\n
        - cant_caracteres (int): cantidad de caracteres que se desea (por defecto es 3).\n
    Retorna:\n
        - list: lista con los caracteres elegidos entre A, B, C, D, E, 0 y 7.
    """
    caracteres = ["A", "B", "C", "D", "E", 0, 7]
    lista_tirada = []

    for _ in range(cant_caracteres):
        numero = random.randint(0, len(caracteres) - 1)
        lista_tirada += [caracteres[numero]]

    return lista_tirada



def evaluar_tirada(lista_tirada: list) -> str:
    """
    Clasifica la tirada según las reglas del juego.\n
    Parámetros:\n
        - lista_tirada (list): lista con los 3 caracteres de la tirada.\n
    Retorna:\n
        - str: retorna "cero" (tres ceros), "siete" (tres sietees), "tres iguales", "dos iguales" o "distintos".
    """
    if lista_tirada[0] == 0 and lista_tirada[1] == 0 and lista_tirada[2] == 0:
        tipo = "cero"

    elif lista_tirada[0] == 7 and lista_tirada[1] == 7 and lista_tirada[2] == 7:
        tipo = "siete"

    elif lista_tirada[0] == lista_tirada[1] == lista_tirada[2]:
        tipo = "tres iguales"

    elif lista_tirada[0] == lista_tirada[1] or lista_tirada[1] == lista_tirada[2] or lista_tirada[0] == lista_tirada[2]:
        tipo = "dos iguales"

    else:
        tipo = "distintos"
 
    return tipo



def armar_mensaje_tirada(resultado_tirada: str, lista_tirada: list, apuesta: int) -> str:
    """
    Arma el mensaje con el resultado de la tirada.\n
    Parámetros:\n
        - resultado_tirada (str): resultado devuelto por evaluar_tirada.
        - lista_tirada (list): lista con los 3 caracteres de la tirada.
        - apuesta (int): apuesta de la jugada.\n
    Retorna:\n
        - str: mensaje para mostrar al jugador.
    """
    if resultado_tirada == "cero":

        mensaje = f"""
¡Tres {lista_tirada[0]}!
¡Perdés todos puntos acumulados!
>>>>>>>>>>FIN DEL JUEGO<<<<<<<<<<"""
        
    elif resultado_tirada == "siete":

        mensaje = f"""
¡Tres {lista_tirada[0]}!
¡Ganaste {apuesta * 10} puntos!"""
        
    elif resultado_tirada == "tres iguales":

        mensaje = f"""
¡Tres {lista_tirada[0]}!
¡Ganaste {apuesta * 5} puntos!"""
        
    elif resultado_tirada == "dos iguales":
        mensaje = f"""
¡Dos iguales!
¡Ganaste {apuesta * 2} puntos!"""
        
    else:
        mensaje = "Perdiste la apuesta..."
 
    return mensaje



def actualizar_puntaje_tirada(resultado_tirada: str, apuesta: int, puntaje: int) -> int:
    """
    Actualiza el puntaje según el resultado de la tirada.\n
    Parámetros:\n
       - resultado_tirada (str): resultado devuelto por la funcion evaluar_tirada.
       - apuesta (int): apuesta de la jugada.
       - puntaje (int): puntaje con la apuesta ya descontada.\n
    Retorna:\n
       - int: puntaje actualizado (puntaje 0 si salieron tres 0).
    """
    if resultado_tirada == "cero":
        puntaje = 0

    elif resultado_tirada == "siete":
        puntaje += apuesta * 10

    elif resultado_tirada == "tres iguales":
        puntaje += apuesta * 5

    elif resultado_tirada == "dos iguales":
        puntaje += apuesta * 2
 
    return puntaje



#-------------------------------------- BLACK JACK ----------------------------------------------------------------------------


def sacar_cartas(cant_cartas: int = 1) -> list:
    """
    Saca una cierta cantidad de cartas al azar del mazo, sin distinguir palos (por defecto es 1).\n
    Parámetros:\n
        - cant_cartas (int): cantidad de cartas que se desea (por defecto es 1).\n
    Retorna:\n
        - list: lista con las cartas elegidas entre "A", "2" a "10", "J", "Q" y "K".
    """
    cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    lista_cartas = []
 
    for _ in range(cant_cartas):
        numero = random.randint(0, len(cartas) - 1)
        lista_cartas += [cartas[numero]]
 
    return lista_cartas
 
 
 
def valor_mano(mano: list) -> int:
    """
    Calcula el valor total de una mano. Los Ases valen 11, pero pasan a valer 1 (de a uno) mientras el total supere 21.\n
    Parámetros:\n
        - mano (list): lista de cartas.\n
    Retorna:\n
        - int: valor total de la mano.
    """
    total = 0
    ases = 0

    for carta in mano:
        if carta == "A":
            total += 11
            ases += 1

        elif carta == "J" or carta == "Q" or carta == "K":
            total += 10

        else:
            total += int(carta)

    while total > 21 and ases > 0:
        total -= 10
        ases -= 1

    return total
 
 
 
def armar_texto_mano(lista_cartas: list, ocultar_segunda_carta: bool) -> str:
    """
    Arma el texto para mostrar una mano.\n
    Parámetros:\n
        - lista_cartas (list): lista de cartas.
        - ocultar_segunda_carta (bool): True para mostrar solo la primera carta (la segunda aparece como "?").\n
    Retorna:\n
        - str: texto con las cartas (y el total si no está oculta).
    """
    if ocultar_segunda_carta == True:
        texto = f"{lista_cartas[0]} ?"
 
    else:
        texto = ""
 
        for carta in lista_cartas:
            texto += f"{carta} "
 
        texto += f"(total: {valor_mano(lista_cartas)})"
 
    return texto
 
 
 
def verificar_turno(puntos_jugador: int, opcion: str) -> bool:
    """
    Indica si el jugador todavia puede pedir cartas.\n
    Parámetros:\n
        - puntos_jugador (int): valor de la mano del jugador.
        - opcion (str): última opción elegida por el jugador.\n
    Retorna:\n
        - bool: False si se pasó de 21 o se plantó, True en caso contrario.
    """
    sigue = True

    if puntos_jugador > 21 or opcion == "2":
        sigue = False

    return sigue
 
 
 
def verificar_opcion_blackjack(opcion: str) -> bool: 
    """
    Verifica que la opción elegida en el turno del jugador sea valida.\n
    Parámetros:\n
        - opcion (str): opción ingresada por el usuario.\n
    Retorna:\n
        - bool: True si la opción es "1" o "2", False en caso contrario.
    """
    valida = True
 
    if opcion != "1" and opcion != "2":
        valida = False
 
    return valida
 
 
 
def pedir_carta(opcion: str, mano_jugador: list) -> list: 
    """
    Aplica la opción elegida: con "1" el jugador recibe una carta.\n
    Parámetros:\n
        - opcion (str): opción ingresada por el usuario.
        - mano_jugador (list): mano del jugador.\n
    Retorna:\n
        - list: mano del jugador actualizada.
    """
    if opcion == "1":
        mano_jugador += sacar_cartas()
 
    return mano_jugador
 
 
 
def turno_banca(banca: list, puntos_jugador: int) -> list:
    """
    Turno de la banca: pide cartas mientras tenga menos de 17. Si el jugador ya se pasó de 21, la banca no juega.\n
    Parámetros:\n
        - banca (list): mano de la banca.
        - puntos_jugador (int): valor final de la mano del jugador.\n
    Retorna:\n
        - list: mano final de la banca.
    """
    puntos_banca = valor_mano(banca)

    while puntos_jugador <= 21 and puntos_banca < 17:
        carta_nueva = sacar_cartas()
        banca += carta_nueva

        puntos_banca = valor_mano(banca)

    return banca
 
 
 
def comparar_manos(puntos_jugador: int, puntos_banca: int) -> str:
    """
    Determina el resultado de la ronda de BlackJack.\n
    Parámetros:\n
        - puntos_jugador (int): valor final de la mano del jugador.
        - puntos_banca (int): valor final de la mano de la banca.\n
    Retorna:\n
        - str: retorna "jugador pasado", "banca pasada", "gana jugador", "gana banca" o "empate".
    """
    if puntos_jugador > 21:
        tipo = "jugador pasado"
 
    elif puntos_banca > 21:
        tipo = "banca pasada"
 
    elif puntos_jugador > puntos_banca:
        tipo = "gana jugador"
 
    elif puntos_jugador < puntos_banca:
        tipo = "gana banca"
 
    else:
        tipo = "empate"
 
    return tipo
 
 
 
def armar_mensaje_blackjack(tipo: str, apuesta: int) -> str:
    """
    Arma el mensaje con el resultado de la ronda de BlackJack.\n
    Parámetros:\n
        - tipo (str): resultado devuelto por comparar_manos.
        - apuesta (int): apuesta de la ronda.\n
    Retorna:\n
        - str: mensaje para mostrar al jugador.
    """
    if tipo == "jugador pasado":
        mensaje = "Te pasaste de 21. ¡Perdiste la apuesta!"
 
    elif tipo == "banca pasada":
        mensaje = f"La banca se pasó de 21. ¡Ganaste {apuesta * 2} puntos!"
 
    elif tipo == "gana jugador":
        mensaje = f"¡Ganaste {apuesta * 2} puntos!"
 
    elif tipo == "gana banca":
        mensaje = "¡Perdiste la apuesta! La banca gana."
 
    else:
        mensaje = "Empate (push). Se te devuelve la apuesta."
 
    return mensaje
 
 
 
def actualizar_puntaje_blackjack(tipo: str, apuesta: int, puntaje: int) -> int:
    """
    Actualiza el puntaje según el resultado de la ronda de BlackJack.\n
    Parámetros:\n
        - tipo (str): resultado devuelto por la funcion comparar_manos.
        - apuesta (int): apuesta de la ronda.
        - puntaje (int): puntaje con la apuesta ya descontada.\n
    Retorna:\n
        - int: puntaje actualizado (doble de la apuesta si gana, la apuesta si empata, sin cambios si pierde).
    """
    if tipo == "banca pasada" or tipo == "gana jugador":
        puntaje += apuesta * 2
 
    elif tipo == "empate":
        puntaje += apuesta
 
    return puntaje