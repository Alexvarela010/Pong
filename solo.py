import pygame
import sys
from config import *
from funciones1jugador import *
from pantallaganador import Ganador

# Inicializar Pygame
pygame.init()
pygame.mixer.music.load("audio.mp3")

# Configuración de la ventana
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong")
RELOJ = pygame.time.Clock()

# Puntuaciones
puntuacion_jugador1 = 0
puntuacion_jugador2 = 0

# Velocidades
if get_dificultad() == 'Facil':
    VELOCIDAD_PELOTA = [4, 4]
elif get_dificultad() == 'Intermedio':
    VELOCIDAD_PELOTA = [6, 6]
elif get_dificultad() == 'Dificil':
    VELOCIDAD_PELOTA = [8, 8]

# Función principal
def juego():
    global VELOCIDAD_PELOTA, puntuacion_jugador1, puntuacion_jugador2

    bloques1 = [[pygame.Rect(c * (BLOQUE_ANCHO + 10) + 20, f * (BLOQUE_ALTO + 10) + 50, BLOQUE_ANCHO, BLOQUE_ALTO)
                 for f in range(filas)] for c in range(columnas)]

    bloques2 = [[pygame.Rect(c * (BLOQUE_ANCHO + 10) + RAQUETA2.right + 30, f * (BLOQUE_ALTO + 10) + 50, BLOQUE_ANCHO,
                             BLOQUE_ALTO)
                 for f in range(filas)] for c in range(columnas)]

    cuadrados_extra = []  # Lista para los cuadrados extra

    while True:
        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimiento de las raquetas
        mover_raquetas1ju()



        # Movimiento de la pelota
        PELOTA.x += VELOCIDAD_PELOTA[0]
        PELOTA.y += VELOCIDAD_PELOTA[1]

        # Colisiones con la parte superior e inferior
        if PELOTA.top <= 0 or PELOTA.bottom >= ALTO:
            pygame.mixer.music.play()
            VELOCIDAD_PELOTA[1] *= -1

        # Colisiones con las raquetas
        if PELOTA.colliderect(RAQUETA1) or PELOTA.colliderect(RAQUETA2):
            pygame.mixer.music.play()
            VELOCIDAD_PELOTA[0] *= -1

        # Colisión con los bloques
        VELOCIDAD_PELOTA = manejar_colisiones_bloques1ju(bloques1, VELOCIDAD_PELOTA, cuadrados_extra)
        VELOCIDAD_PELOTA = manejar_colisiones_bloques1ju(bloques2, VELOCIDAD_PELOTA, cuadrados_extra)


        # Detectar si la pelota sale de los límites
        if PELOTA.left <= 0:
            puntuacion_jugador2 += 1
            PELOTA.x, PELOTA.y = ANCHO // 2 - 15, ALTO // 2 - 15
            if get_dificultad() == 'Facil':
                VELOCIDAD_PELOTA = [4, 4]
            elif get_dificultad() == 'Intermedio':
                VELOCIDAD_PELOTA = [6, 6]
            elif get_dificultad() == 'Dificil':
                VELOCIDAD_PELOTA = [8, 8]
            VELOCIDAD_RAQUETA = 5
        if PELOTA.right >= ANCHO:
            puntuacion_jugador1 += 1
            PELOTA.x, PELOTA.y = ANCHO // 2 - 15, ALTO // 2 - 15
            if get_dificultad() == 'Facil':
                VELOCIDAD_PELOTA = [4, 4]
            elif get_dificultad() == 'Intermedio':
                VELOCIDAD_PELOTA = [6, 6]
            elif get_dificultad() == 'Dificil':
                VELOCIDAD_PELOTA = [8, 8]

            VELOCIDAD_RAQUETA = 5


        # Reiniciar si algún jugador alcanza 7 puntos
        #if puntuacion_jugador1 == 12 or puntuacion_jugador2 == 12:
        #   reiniciar_juego()

        if puntuacion_jugador1 == 7:
            ganador = Ganador("Jugador 1")
            ganador.pantalla()
        if puntuacion_jugador2 == 7:
            ganador = Ganador("Jugador 2")
            ganador.pantalla()

        # Dibujar en la pantalla
        VENTANA.fill(NEGRO)
        for c, columna in enumerate(bloques1):
            for bloque in columna:
                pygame.draw.rect(VENTANA, COLORES_BLOQUES1[c], bloque)
        for c, columna in enumerate(bloques2):
            for bloque in columna:
                pygame.draw.rect(VENTANA, COLORES_BLOQUES2[c], bloque)
        for cuadrado in cuadrados_extra[:]:
            cuadrado.mover()  # Mover el cuadrado
            if cuadrado.colisionar_con_raquetas(RAQUETA1, RAQUETA2):
                cuadrados_extra.remove(cuadrado)  # Eliminar cuadrado si colisiona con las raquetas
            if cuadrado.colisionar_con_bordes(ANCHO, ALTO):
                cuadrados_extra.remove(cuadrado)  # Eliminar cuadrado si sale de los bordes
            # Verificar colisión con bloques
            if cuadrado.colisionar_con_bloques(bloques1, cuadrados_extra):
                continue  # Si colisionó con un bloque, continuar con el siguiente cuadrado
            if cuadrado.colisionar_con_bloques(bloques2, cuadrados_extra):
                continue  # Si colisionó con un bloque, continuar con el siguiente cuadrado
            if cuadrado.rect.x <= 10:
                puntuacion_jugador2 += 1
            if cuadrado.rect.x >= ANCHO-10:
                puntuacion_jugador1 += 1


        # Dibujar los cuadrados extra
        for cuadrado in cuadrados_extra:
            cuadrado.dibujar(VENTANA)
        pygame.draw.rect(VENTANA, BLANCO, RAQUETA1)
        pygame.draw.rect(VENTANA, BLANCO, RAQUETA2)
        pygame.draw.ellipse(VENTANA, BLANCO, PELOTA)
        pygame.draw.aaline(VENTANA, BLANCO, (ANCHO // 2, 0), (ANCHO // 2, ALTO))

        # Mostrar las puntuaciones
        texto_jugador1 = FUENTE.render(str(puntuacion_jugador1), True, BLANCO)
        texto_jugador2 = FUENTE.render(str(puntuacion_jugador2), True, BLANCO)
        VENTANA.blit(texto_jugador1, (ANCHO // 4, 20))
        VENTANA.blit(texto_jugador2, (ANCHO // 4 * 3 - 20, 20))

        pygame.display.flip()
        RELOJ.tick(60)


# Iniciar el juego
juego()
