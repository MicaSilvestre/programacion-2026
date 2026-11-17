import random
 
#-------------------------------------- GENERALES ------------------------------------------------------------
 
def mostrar_menu() -> str:
    """
    Muestra el menu principal y pide la opción al usuario.\n
    Retorna:\n
        - str: opción ingresada por el usuario.
    """
    opcion = input("""
 --------------------------------------------------------------------------------------------
 == GESTIÓN DE BIBLIOTECA ==
 
 Opciones:
1) Alta de libro
2) Registrar un préstamo o devolución
3) Consultar estadísticas
4) Mostrar catálogo ordenado
5) Salir
 
Seleccione una opcion: """).strip()
 
    return opcion
 
 
def mostrar_mensaje_final() -> None:
    """
    Muestra el mensaje de cierre del programa.
    """
    print("""
                ¡Programa finalizado!
        -->>> ¡Gracias por utilizar el sistema de biblioteca! <<<--""")
 
 
 
#-------------------------------------- ARCHIVO CSV ------------------------------------------------------------
 
def cargar_libros(ruta: str) -> list:
    """
    Lee los libros desde el archivo CSV. Si el archivo no existe, devuelve una lista vacía.\n
    Parámetros:\n
        - ruta (str): ruta del archivo CSV.\n
    Retorna:\n
        - list: lista de diccionarios con los datos de cada libro.
    """
    try:
        with open(ruta, "r") as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        lineas = []
 
    lista_libros = []
 
    for i in range(1, len(lineas)):
        linea = lineas[i].strip()
 
        if linea != "":
            partes = linea.split(",")
 
            libro = {
                "isbn": partes[0],
                "titulo": partes[1],
                "autor": partes[2],
                "genero": partes[3],
                "anio": int(partes[4]),
                "stock": int(partes[5]),
                "cantidad_prestamos": int(partes[6])
            }
 
            lista_libros += [libro]
 
    return lista_libros
 
 
def guardar_libros(ruta: str, libros: list) -> None:
    """
    Guarda todos los libros de la lista en el archivo CSV.\n
    Parámetros:\n
        - ruta (str): ruta del archivo CSV.
        - libros (list): lista de diccionarios con los datos de los libros.
    """
    with open(ruta, "w") as archivo:
        archivo.write("isbn,titulo,autor,genero,anio,stock,cantidad_prestamos\n")
 
        for libro in libros:
            partes = [
                libro["isbn"],
                libro["titulo"],
                libro["autor"],
                libro["genero"],
                str(libro["anio"]),
                str(libro["stock"]),
                str(libro["cantidad_prestamos"])
            ]
 
            archivo.write(",".join(partes) + "\n")
 
 
 
#-------------------------------------- ALTA DE LIBRO ------------------------------------------------------------
 
def verificar_isbn_existente(libros: list, isbn: str) -> bool:
    """
    Verifica si un ISBN ya se encuentra registrado en la lista de libros.\n
    Parámetros:\n
        - libros (list): lista de diccionarios con los libros registrados.
        - isbn (str): ISBN que se desea buscar.\n
    Retorna:\n
        - bool: True si el ISBN existe, False en caso contrario.
    """
    existe = False
 
    for libro in libros:
        if libro["isbn"] == isbn:
            existe = True
            break
 
    return existe
 
 
def generar_isbn(libros: list) -> str:
    """
    Genera un ISBN de 13 números con el formato 3-1-2-6-1 y verifica que no esté repetido.\n
    Parámetros:\n
        - libros (list): lista de diccionarios con los libros registrados.\n
    Retorna:\n
        - str: ISBN generado.
    """
    repetido = True
 
    while repetido == True:
        numeros = ""
 
        for _ in range(13):
            numeros += str(random.randint(0, 9))
 
        isbn = numeros[0:3] + "-" + numeros[3] + "-" + numeros[4:6] + "-" + numeros[6:12] + "-" + numeros[12]
 
        repetido = verificar_isbn_existente(libros, isbn)
 
    return isbn
 
 
def verificar_texto(texto: str) -> bool:
    """
    Verifica que el texto tenga entre 3 y 50 caracteres y que no contenga comas.\n
    Parámetros:\n
        - texto (str): texto ingresado por el usuario.\n
    Retorna:\n
        - bool: True si el texto es válido, False en caso contrario.
    """
    valido = True
 
    if len(texto) < 3 or len(texto) > 50:
        valido = False
 
    for caracter in texto:
        if caracter == ",":
            valido = False
            break
 
    return valido
 
 
def pedir_texto(mensaje: str) -> str:
    """
    Solicita un texto hasta que sea válido, normalizado con formato de titulo.\n
    Parámetros:\n
        - mensaje (str): mensaje que se muestra al solicitar el texto.\n
    Retorna:\n
        - str: texto ingresado, sin espacios sobrantes y con formato de titulo.
    """
    texto = ""
    valido = False
 
    while valido == False:
        texto = input(mensaje).strip().title()
        valido = verificar_texto(texto)
 
        if valido == False:
            print("¡ERROR! El texto debe tener entre 3 y 50 caracteres y no contener comas.")
 
    return texto
 
 
def verificar_genero(genero: str) -> bool:
    """
    Verifica que el género sea uno de los permitidos.\n
    Parámetros:\n
        - genero (str): género ingresado (ya normalizado con capitalize).\n
    Retorna:\n
        - bool: True si es Ciencia ficcion, Thriller, Clasicos, Fantasia o Historia.
    """
    valido = False
 
    if genero == "Ciencia ficcion" or genero == "Thriller" or genero == "Clasicos" or genero == "Fantasia" or genero == "Historia":
        valido = True
 
    return valido
 
 
def pedir_genero(mensaje: str) -> str:
    """
    Solicita el género del libro hasta que sea uno de los permitidos.\n
    Parámetros:\n
        - mensaje (str): mensaje que se muestra al solicitar el género.\n
    Retorna:\n
        - str: género ingresado, sin espacios sobrantes y con la primera letra en mayúscula (capitalizado).
    """
    genero = ""
    valido = False
 
    while valido == False:
        genero = input(mensaje).strip().capitalize()
        valido = verificar_genero(genero)
 
        if valido == False:
            print("¡ERROR! Género inválido. Opciones: Ciencia ficcion, Thriller, Clasicos, Fantasia, Historia.")
 
    return genero
 
 
def verificar_entero_valido(texto: str, minimo: int) -> bool:
    """
    Verifica que el texto sea un entero mayor o igual al mínimo.\n
    Parámetros:\n
        - texto (str): número ingresado por el usuario.
        - minimo (int): valor mínimo permitido.\n
    Retorna:\n
        - bool: True si es válido, False en caso contrario.
    """
    valido = texto.isdecimal()
 
    if valido == True:
        numero = int(texto)
        if numero < minimo:
            valido = False
 
    return valido
 
 
def pedir_entero(mensaje: str, minimo: int) -> int:
    """
    Solicita un número entero hasta que sea mayor o igual al mínimo.\n
    Parámetros:\n
        - mensaje (str): mensaje que se muestra al solicitar el número.
        - minimo (int): valor mínimo permitido.\n
    Retorna:\n
        - int: número ingresado y validado.
    """
    texto = ""
    valido = False
 
    while valido == False:
        texto = input(mensaje).strip()
        valido = verificar_entero_valido(texto, minimo)
 
        if valido == False:
            print(f"¡ERROR! Debe ingresar un número entero mayor o igual a {minimo}.")
 
    return int(texto)
 
 
def armar_mensaje_alta(isbn: str) -> str:
    """
    Arma el mensaje que informa que el libro fue agregado.\n
    Parámetros:\n
        - isbn (str): ISBN asignado al libro.\n
    Retorna:\n
        - str: mensaje para mostrar al usuario.
    """
    mensaje = f"""
¡Libro agregado correctamente!
ISBN asignado: {isbn}"""
 
    return mensaje
 
 
def dar_alta_libro(libros: list, ruta: str) -> None:
    """
    Pide los datos de UN libro, genera su ISBN, lo agrega a la lista y actualiza el archivo CSV.\n
    Parámetros:\n
        - libros (list): lista de diccionarios con los libros registrados (se modifica).
        - ruta (str): ruta del archivo CSV.
    """
    print("\n----- ALTA DE LIBRO -----")
 
    titulo = pedir_texto("Ingrese el título: ")
    autor = pedir_texto("Ingrese el autor: ")
    genero = pedir_genero("Ingrese el género: ")
    anio = pedir_entero("Ingrese el año de publicación (mayor a 1500): ", 1501)
    stock = pedir_entero("Ingrese el stock disponible: ", 0)
    isbn = generar_isbn(libros)
 
    libro = {
        "isbn": isbn,
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "anio": anio,
        "stock": stock,
        "cantidad_prestamos": 0
    }
 
    libros += [libro]
    guardar_libros(ruta, libros)
 
    print(armar_mensaje_alta(isbn))
 
 
 
#-------------------------------------- PRESTAMO / DEVOLUCION ------------------------------------------------------------
 
def armar_texto_lista_libros(libros: list) -> str:
    """
    Arma el texto con el título y el ISBN de todos los libros registrados.\n
    Parámetros:\n
        - libros (list): lista de diccionarios con los libros registrados.\n
    Retorna:\n
        - str: texto con los títulos y los ISBN de los libros.
    """
    texto = "\n----- LIBROS EN EL CATÁLOGO -----\n"
 
    for libro in libros:
        texto += f"""
Título: {libro["titulo"]}
ISBN: {libro["isbn"]}
------------------------------
"""
 
    return texto
 
 
def buscar_libro(libros: list, isbn: str) -> int:
    """
    Busca un libro por su ISBN y obtiene su posición en la lista (el ISBN debe existir).\n
    Parámetros:\n
        - libros (list): lista de diccionarios con los libros registrados.
        - isbn (str): ISBN del libro que se desea buscar.\n
    Retorna:\n
        - int: posición del libro en la lista.
    """
    posicion = 0
 
    for i in range(len(libros)):
        if libros[i]["isbn"] == isbn:
            posicion = i
            break
 
    return posicion
 
 
def verificar_movimiento(movimiento: str) -> bool:
    """
    Verifica que el movimiento elegido sea valido.\n
    Parámetros:\n
        - movimiento (str): movimiento ingresado por el usuario (ya en minúsculas).\n
    Retorna:\n
        - bool: True si el movimiento es "p" o "d", False en caso contrario.
    """
    valido = True
 
    if movimiento != "p" and movimiento != "d":
        valido = False
 
    return valido
 
 
def pedir_movimiento() -> str:
    """
    Solicita si se desea registrar un préstamo o una devolución hasta que la opción sea válida.\n
    Retorna:\n
        - str: "p" para préstamo o "d" para devolución.
    """
    movimiento = ""
    valido = False
 
    while valido == False:
        movimiento = input("Ingrese P para préstamo o D para devolución: ").strip().lower()
        valido = verificar_movimiento(movimiento)
 
        if valido == False:
            print("¡ERROR! Ingrese una opción válida.")
 
    return movimiento
 
 
def evaluar_movimiento(movimiento: str, stock: int) -> str:
    """
    Clasifica el movimiento según el stock disponible.\n
    Parámetros:\n
        - movimiento (str): "p" (préstamo) o "d" (devolución).
        - stock (int): stock actual del libro.\n
    Retorna:\n
        - str: retorna "devolucion", "prestamo" o "sin stock".
    """
    if movimiento == "d":
        tipo = "devolucion"
 
    elif stock > 0:
        tipo = "prestamo"
 
    else:
        tipo = "sin stock"
 
    return tipo
 
 
def actualizar_libro(tipo: str, libro: dict) -> None:
    """
    Actualiza el stock y la cantidad de préstamos del libro según el movimiento (modifica el diccionario).\n
    Parámetros:\n
        - tipo (str): resultado devuelto por evaluar_movimiento.
        - libro (dict): libro sobre el que se realiza el movimiento.
    """
    if tipo == "prestamo":
        libro["stock"] -= 1
        libro["cantidad_prestamos"] += 1
 
    elif tipo == "devolucion":
        libro["stock"] += 1
 
 
def armar_mensaje_movimiento(tipo: str) -> str:
    """
    Arma el mensaje con el resultado del movimiento.\n
    Parámetros:\n
        - tipo (str): resultado devuelto por evaluar_movimiento.\n
    Retorna:\n
        - str: mensaje para mostrar al usuario.
    """
    if tipo == "prestamo":
        mensaje = "\nPréstamo registrado correctamente."
 
    elif tipo == "devolucion":
        mensaje = "\nDevolución registrada correctamente."
 
    else:
        mensaje = "\nNo hay stock disponible para realizar el préstamo."
 
    return mensaje
 
 
def registrar_movimiento(libros: list, ruta: str) -> None:
    """
    Registra un préstamo o una devolución sobre un libro elegido por ISBN y actualiza el archivo CSV.\n
    Parámetros:\n
        - libros (list): lista de diccionarios con los libros registrados (se modifica).
        - ruta (str): ruta del archivo CSV.
    """
    if len(libros) == 0:
        mensaje = "\nNo hay libros cargados."
 
    else:
        print(armar_texto_lista_libros(libros))
 
        isbn = input("Ingrese el ISBN del libro: ").strip()
        existe = verificar_isbn_existente(libros, isbn)
 
        if existe == False:
            mensaje = "\n¡ERROR! No se encontró un libro con ese ISBN."
 
        else:
            posicion = buscar_libro(libros, isbn)
            movimiento = pedir_movimiento()
            tipo = evaluar_movimiento(movimiento, libros[posicion]["stock"])
            actualizar_libro(tipo, libros[posicion])
 
            if tipo != "sin stock":
                guardar_libros(ruta, libros)
 
            mensaje = armar_mensaje_movimiento(tipo)
 
    print(mensaje)
 
 
 
#-------------------------------------- ESTADISTICAS ------------------------------------------------------------
 
def calcular_mayor_prestamos(libros: list) -> int:
    """
    Calcula la mayor cantidad de préstamos que tiene un libro.\n
    Parámetros:\n
        - libros (list): lista de diccionarios con los libros registrados.\n
    Retorna:\n
        - int: mayor cantidad de préstamos (0 si ningún libro fue prestado).
    """
    mayor = 0
 
    for libro in libros:
        if libro["cantidad_prestamos"] > mayor:
            mayor = libro["cantidad_prestamos"]
 
    return mayor
 
 
def armar_texto_libros_mas_solicitados(libros: list) -> str:
    """
    Arma el texto con el libro (o los libros, si hay empate) más solicitado/s.\n
    Parámetros:\n
        - libros (list): lista de diccionarios con los libros registrados.\n
    Retorna:\n
        - str: título y cantidad de préstamos de cada libro más solicitado.
    """
    mayor = calcular_mayor_prestamos(libros)
 
    if mayor == 0:
        texto = "Todavía no se registraron préstamos.\n"
 
    else:
        texto = ""
 
        for libro in libros:
            if libro["cantidad_prestamos"] == mayor:
                texto += f"Título: {libro['titulo']}\nCantidad de préstamos: {mayor}\n"
 
    return texto
 
 
def calcular_prestamos_por_genero(libros: list) -> dict:
    """
    Acumula la cantidad de préstamos de cada género.\n
    Parámetros:\n
        - libros (list): lista de diccionarios con los libros registrados.\n
    Retorna:\n
        - dict: {género: cantidad de préstamos}.
    """
    prestamos_generos = {
        "Ciencia ficcion": 0,
        "Thriller": 0,
        "Clasicos": 0,
        "Fantasia": 0,
        "Historia": 0
    }
 
    for libro in libros:
        prestamos_generos[libro["genero"]] += libro["cantidad_prestamos"]
 
    return prestamos_generos
 
 
def armar_texto_generos_mas_solicitados(prestamos_generos: dict) -> str:
    """
    Arma el texto con el género (o los géneros, si hay empate) con mayor cantidad de préstamos.\n
    Parámetros:\n
        - prestamos_generos (dict): {género: cantidad de préstamos}.\n
    Retorna:\n
        - str: género/s más solicitado/s y su cantidad de préstamos.
    """
    mayor = 0
 
    for genero, prestamos in prestamos_generos.items():
        if prestamos > mayor:
            mayor = prestamos
 
    if mayor == 0:
        texto = "Todavía no se registraron préstamos.\n"
 
    else:
        texto = ""
 
        for genero, prestamos in prestamos_generos.items():
            if prestamos == mayor:
                texto += f"{genero} - {mayor} préstamos\n"
 
    return texto
 
 
def calcular_porcentaje_sin_prestamos(libros: list) -> float:
    """
    Calcula el porcentaje de libros que nunca fueron prestados.\n
    Parámetros:\n
        - libros (list): lista de diccionarios con los libros registrados.\n
    Retorna:\n
        - float: porcentaje de libros sin préstamos.
    """
    contador = 0
 
    for libro in libros:
        if libro["cantidad_prestamos"] == 0:
            contador += 1
 
    porcentaje = contador * 100 / len(libros)

    return porcentaje
 
 
def contar_libros_sin_stock(libros: list) -> int:
    """
    Cuenta la cantidad de libros que no tienen unidades disponibles.\n
    Parámetros:\n
        - libros (list): lista de diccionarios con los libros registrados.\n
    Retorna:\n
        - int: cantidad de libros sin stock.
    """
    contador = 0
 
    for libro in libros:
        if libro["stock"] == 0:
            contador += 1
 
    return contador
 
 
def calcular_promedio_antiguedad(libros: list, anio_actual: int) -> float:
    """
    Calcula la antigüedad promedio de los libros del catálogo.\n
    Parámetros:\n
        - libros (list): lista de diccionarios con los libros registrados.
        - anio_actual (int): año actual utilizado para calcular la antigüedad.\n
    Retorna:\n
        - float: antigüedad promedio en años.
    """
    total = 0
 
    for libro in libros:
        total += anio_actual - libro["anio"]
 
    promedio = total / len(libros)

    return promedio
 
 
def armar_texto_estadisticas(libros: list, anio_actual: int) -> str:
    """
    Arma el texto con todas las estadísticas del catálogo.\n
    Parámetros:\n
        - libros (list): lista de diccionarios con los libros registrados.
        - anio_actual (int): año actual utilizado para calcular la antigüedad.\n
    Retorna:\n
        - str: estadísticas listas para mostrar.
    """
    if len(libros) == 0:
        texto = "\nNo hay libros cargados."
 
    else:
        prestamos_generos = calcular_prestamos_por_genero(libros)
        porcentaje = calcular_porcentaje_sin_prestamos(libros)
        sin_stock = contar_libros_sin_stock(libros)
        antiguedad = calcular_promedio_antiguedad(libros, anio_actual)
 
        texto = f"""
Libro/s más solicitado/s:
{armar_texto_libros_mas_solicitados(libros)}
Género/s más solicitado/s:
{armar_texto_generos_mas_solicitados(prestamos_generos)}
Porcentaje de libros nunca prestados: {porcentaje:.2f}%
Cantidad de libros sin stock: {sin_stock}
Antigüedad promedio de los libros: {antiguedad:.2f} años"""
 
    return texto
 
 
def mostrar_estadisticas(libros: list, anio_actual: int) -> None:
    """
    Muestra por pantalla las estadísticas del catálogo.\n
    Parámetros:\n
        - libros (list): lista de diccionarios con los libros registrados.
        - anio_actual (int): año actual utilizado para calcular la antigüedad.
    """
    print(f"""
========== ESTADÍSTICAS ==========
{armar_texto_estadisticas(libros, anio_actual)}""")
 
 
 
#-------------------------------------- CATALOGO ORDENADO ------------------------------------------------------------
 
def verificar_criterio(criterio: str) -> bool:
    """
    Verifica que el criterio de ordenamiento sea valido.\n
    Parámetros:\n
        - criterio (str): criterio ingresado por el usuario (ya en minúsculas).\n
    Retorna:\n
        - bool: True si es "titulo", "anio" o "genero", False en caso contrario.
    """
    valido = True
 
    if criterio != "titulo" and criterio != "anio" and criterio != "genero":
        valido = False
 
    return valido
 
 
def pedir_criterio() -> str:
    """
    Solicita el criterio de ordenamiento hasta que sea válido, normalizado en minúsculas.\n
    Retorna:\n
        - str: "titulo", "anio" o "genero".
    """
    criterio = ""
    valido = False
 
    while valido == False:
        criterio = input("Ordenar por (titulo / anio / genero): ").strip().lower()
 
        if criterio == "título":
            criterio = "titulo"
        elif criterio == "año":
            criterio = "anio"
        elif criterio == "género":
            criterio = "genero"
 
        valido = verificar_criterio(criterio)
 
        if valido == False:
            print("¡ERROR! Criterio inválido.")
 
    return criterio
 
 
def verificar_orden(orden: str) -> bool:
    """
    Verifica que el orden de clasificación sea valido.\n
    Parámetros:\n
        - orden (str): orden ingresado por el usuario (ya en minúsculas).\n
    Retorna:\n
        - bool: True si es "asc" o "desc", False en caso contrario.
    """
    valido = True
 
    if orden != "asc" and orden != "desc":
        valido = False
 
    return valido
 
 
def pedir_orden() -> str:
    """
    Solicita el orden de clasificación hasta que sea válido, normalizado en minúsculas.\n
    Retorna:\n
        - str: "asc" para ascendente o "desc" para descendente.
    """
    orden = ""
    valido = False
 
    while valido == False:
        orden = input("Orden (asc / desc): ").strip().lower()
        valido = verificar_orden(orden)
 
        if valido == False:
            print("¡ERROR! Orden inválido.")
 
    return orden
 
 
def armar_texto_catalogo(libros: list, criterio: str, orden: str) -> str:
    """
    Arma el texto del catálogo completo ordenado según el criterio y el orden elegidos (sin modificar la lista).\n
    Parámetros:\n
        - libros (list): lista de diccionarios con los libros registrados.
        - criterio (str): "titulo", "anio" o "genero".
        - orden (str): "asc" o "desc".\n
    Retorna:\n
        - str: catálogo completo listo para mostrar.
    """
    pares = []
 
    for i in range(len(libros)):
        valor = libros[i][criterio]
 
        if criterio != "anio":
            valor = valor.lower()
 
        pares += [(valor, i)]
 
    if orden == "asc":
        pares.sort()
    else:
        pares.sort(reverse=True)
 
    texto = "\n========== CATÁLOGO DE LIBROS ==========\n"
 
    for _, posicion in pares:
        libro = libros[posicion]
 
        texto += f"""
ISBN: {libro["isbn"]}
Título: {libro["titulo"]}
Autor: {libro["autor"]}
Género: {libro["genero"]}
Año: {libro["anio"]}
Stock: {libro["stock"]}
Cantidad de préstamos: {libro["cantidad_prestamos"]}
----------------------------------------
"""
 
    return texto
 
 
def mostrar_catalogo_ordenado(libros: list) -> None:
    """
    Pide el criterio y el orden de clasificación y muestra el catálogo completo (sin importar el stock).\n
    Parámetros:\n
        - libros (list): lista de diccionarios con los libros registrados.
    """
    if len(libros) == 0:
        mensaje = "\nNo hay libros cargados."
 
    else:
        criterio = pedir_criterio()
        orden = pedir_orden()
        mensaje = armar_texto_catalogo(libros, criterio, orden)
 
    print(mensaje)