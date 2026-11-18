import funciones

ruta = "libros.csv"
anio_actual = 2026

libros = funciones.cargar_libros(ruta)

menu = ""

while menu != "5":
    menu = funciones.mostrar_menu()

    match menu:

        case "1":
            funciones.dar_alta_libro(libros, ruta, anio_actual)

        case "2":
            funciones.registrar_movimiento(libros, ruta)

        case "3":
            funciones.mostrar_estadisticas(libros, anio_actual)

        case "4":
            funciones.mostrar_catalogo_ordenado(libros)

        case "5":
            funciones.mostrar_mensaje_final()

        case _:
            print("\n¡ERROR! Ingrese un valor válido.")