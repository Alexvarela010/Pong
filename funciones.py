import pygame
import random
from config import *
from cuadrado import *
from pantallaganador import *

# Función para reiniciar el juego
def reiniciar_juego():
    global puntuacion_jugador1, puntuacion_jugador2, PELOTA, VELOCIDAD_PELOTA

    puntuacion_jugador1 = 0
    puntuacion_jugador2 = 0
    PELOTA.x, PELOTA.y = ANCHO // 2 - 15, ALTO // 2 - 15
    VELOCIDAD_PELOTA = [4, 4]

# Función para manejar las colisiones con los bloques
def manejar_colisiones_bloques(bloques, VELOCIDAD_PELOTA, cuadrados_extra):
    for c, columna in enumerate(bloques[:] ):
        for bloque in columna[:]:
            if PELOTA.colliderect(bloque):
                VELOCIDAD_PELOTA[0] *= -1  # Rebote de la pelota
                columna.remove(bloque)  # Eliminar el bloque

                # Crear un cuadrado extra con dirección opuesta a la de la pelota
                # Esto asegura que el cuadrado se mueve en la dirección contraria a la pelota

                if VELOCIDAD_PELOTA[0] > 0:  # La pelota se mueve hacia la derecha
                    direccion = [-4, 0]  # El cuadrado se moverá hacia la izquierda
                elif VELOCIDAD_PELOTA[0] < 0:  # La pelota se mueve hacia la izquierda
                    direccion = [4, 0]  # El cuadrado se moverá hacia la derecha


                # Crear el cuadrado extra con la dirección opuesta a la pelota
                cuadrado_extra = Cuadrado(bloque.x + bloque.width // 2 - 5, bloque.y + bloque.height // 2 - 5, direccion)
                cuadrados_extra.append(cuadrado_extra)

    # Mover y verificar las colisiones de los cuadrados extra
    for cuadrado in cuadrados_extra[:]:
        cuadrado.mover()

        # Si el cuadrado colide con la pelota, no hace nada
        if cuadrado.rect.colliderect(PELOTA):
            continue


    return VELOCIDAD_PELOTA



# Función para manejar el movimiento de las raquetas
def mover_raquetas():
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and RAQUETA1.top > 0:
        RAQUETA1.y -= VELOCIDAD_RAQUETA
    if teclas[pygame.K_s] and RAQUETA1.bottom < ALTO:
        RAQUETA1.y += VELOCIDAD_RAQUETA
    if teclas[pygame.K_UP] and RAQUETA2.top > 0:
        RAQUETA2.y -= VELOCIDAD_RAQUETA
    if teclas[pygame.K_DOWN] and RAQUETA2.bottom < ALTO:
        RAQUETA2.y += VELOCIDAD_RAQUETA
