import funciones
 
puntaje = 100
apuesta = 10
 
while puntaje > 0:
    menu = input(f"""
 --------------------------------------------------------------------------------------------
 == ¡BIENVENIDO AL CASINO! ==
 
 Opciones:
1) Jugar Tragamonedas
2) Jugar BlackJack
3) Cambiar apuesta
4) Salir
 
--- Puntaje actual: {puntaje} | Apuesta actual: {apuesta} ---
Seleccione una opcion: """)
 
    match menu:
 
        case "1":
            alcanza = funciones.verificar_apuesta(apuesta, puntaje)
            
            if alcanza == True:
                puntaje -= apuesta
 
                lista_tirada = funciones.generar_tirada()
 
                print("\n>>>>>>>>>>>>>>> TIRADA <<<<<<<<<<<<<<<")
 
                for i in range(3):
                    print(lista_tirada[i], end=" ")
 
                print("\n---------------------------------------")
 
                tipo = funciones.evaluar_tirada(lista_tirada)
                print(funciones.armar_mensaje_tirada(tipo, lista_tirada, apuesta))
 
                puntaje = funciones.actualizar_puntaje_tirada(tipo, apuesta, puntaje)
                print(f"Tus puntos: {puntaje}")
 
                if tipo == "cero":
                    break
 
            else:
                print(funciones.armar_mensaje_puntos_insuficientes(apuesta, puntaje))
 
 
        case "2":
            alcanza = funciones.verificar_apuesta(apuesta, puntaje)
 
            if alcanza == True:
                puntaje -= apuesta
 
                print("\n>>>>>>>>>>>>>>> BLACKJACK <<<<<<<<<<<<<<<")
 
                jugador = funciones.sacar_cartas(2)
                banca = funciones.sacar_cartas(2)
 
                sigue = True
    
                while sigue == True:
                    texto_banca = funciones.armar_texto_mano(banca, True)
                    texto_jugador = funciones.armar_texto_mano(jugador, False)
 
                    print(f"""
Banca: {texto_banca}
Tu mano: {texto_jugador}
\n---------------------------------------""")
 
                    opcion = input("""
1) Pedir carta
2) Plantarse
Elegí una opción: """)
 
                    opcion_valida = funciones.verificar_opcion_blackjack(opcion)
 
                    if opcion_valida == False:
                        print("\n >>>>>>>>>>>>>> ¡ERROR! Ingrese un valor válido <<<<<<<<<<<<<<")
 
                    jugador = funciones.pedir_carta(opcion, jugador)
                    puntos_jugador = funciones.valor_mano(jugador)
                    sigue = funciones.verificar_turno(puntos_jugador, opcion) 

                banca = funciones.turno_banca(banca, puntos_jugador)
                puntos_banca = funciones.valor_mano(banca)

                texto_banca = funciones.armar_texto_mano(banca, False)
                texto_jugador = funciones.armar_texto_mano(jugador, False)
 
                print(f"""
--- Resultado final ---
Banca: {texto_banca}
Tu mano: {texto_jugador}
\n---------------------------------------
""")
 
                tipo = funciones.comparar_manos(puntos_jugador, puntos_banca)
                print(funciones.armar_mensaje_blackjack(tipo, apuesta))
 
                puntaje = funciones.actualizar_puntaje_blackjack(tipo, apuesta, puntaje)
                print(f"Tus puntos: {puntaje}")
 
            else:
                print(funciones.armar_mensaje_puntos_insuficientes(apuesta, puntaje))
 
 
        case "3":
            nueva_apuesta = input(f"""
                -->>>> Puntaje actual: {puntaje} | Apuesta actual: {apuesta} <<<<--
                    Ingrese el nuevo valor de la apuesta: """)
 
            print(funciones.armar_mensaje_apuesta(nueva_apuesta, puntaje))
 
            apuesta_valida = funciones.verificar_apuesta_valida(nueva_apuesta, puntaje)
 
            if apuesta_valida == True:
                apuesta = int(nueva_apuesta)
 
 
        case "4":
            print(f"""
                ¡Programa finalizado!
            -->>> Puntaje final: {puntaje} <<<--""")
            break
 
 
        case _:
            print("\n¡ERROR! Ingrese un valor válido.")
 
if puntaje <= 0:
  print("\n------>>> ¡JUEGO FINALIZADO! Te quedaste sin puntos para apostar. <<<--------")