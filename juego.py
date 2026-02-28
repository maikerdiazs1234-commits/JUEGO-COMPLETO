import random

print("===== JUEGO: PIEDRA, PAPEL O TIJERA =====")

nombre = input("Ingrese su nombre: ")

puntos_jugador = 0
puntos_pc = 0

while True:
    print("\n1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    
    opcion = int(input("Seleccione una opción (1-3): "))
    
    if opcion < 1 or opcion > 3:
        print("Opción inválida")
        continue
    
    pc = random.randint(1, 3)
    
    if opcion == pc:
        print("Empate")
    elif (opcion == 1 and pc == 3) or \
         (opcion == 2 and pc == 1) or \
         (opcion == 3 and pc == 2):
        print("Ganaste")
        puntos_jugador += 1
    else:
        print("Perdiste")
        puntos_pc += 1
    
    print(f"Puntos {nombre}: {puntos_jugador}")
    print(f"Puntos PC: {puntos_pc}")
    
    repetir = input("¿Desea jugar nuevamente? (s/n): ")
    if repetir.lower() != "s":
        break

print("Juego finalizado")