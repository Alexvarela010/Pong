import pygame
import sys

import config
from funciones import *
# Inicializar Pygame
pygame.init()

# Configuración de la ventana
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong")
RELOJ = pygame.time.Clock()

score_font = pygame.font.SysFont("comicsansms", 35)

def mostrar_mensaje(texto, color, posicion):
    mensaje = score_font.render(texto, True, color)
    VENTANA.blit(mensaje, posicion)

class Menu:
    def __init__(self):
        self.modo_juego = None  # Modo de juego, puede ser 1 o 2



    def mostrar(self):

        VENTANA.fill(NEGRO)

        mostrar_mensaje("Selecciona el modo de juego:", BLANCO,
                            (ANCHO // 2 - 200, ALTO // 2 - 100))

        # Opciones de menú
        mostrar_mensaje("1. Single Player", BLANCO, (ANCHO // 2 - 150, ALTO // 2))
        mostrar_mensaje("2. Multiplayer", BLANCO, (ANCHO // 2 - 150, ALTO // 2 + 50))
        pygame.display.flip()

        # Detectar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    seleccionar_dificultad1Jug()
                elif evento.key == pygame.K_2:
                    seleccionar_dificultad()


            RELOJ.tick(60)

# Pantalla de selección de dificultad
def seleccionar_dificultad():
    global dificultad
    while True:
        VENTANA.fill(NEGRO)
        mostrar_mensaje("Selecciona la dificultad:", BLANCO, (ANCHO // 2 - 200, ALTO // 2 - 100))
        mostrar_mensaje("1. Facil", BLANCO, (ANCHO // 2 - 150, ALTO // 2))
        mostrar_mensaje("2. Intermedio", BLANCO, (ANCHO // 2 - 150, ALTO // 2 + 50))
        mostrar_mensaje("3. Dificil", BLANCO, (ANCHO // 2 - 150, ALTO // 2 + 100))
        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    dificultad = 'Facil'
                    config.velocidad_bola(dificultad)
                    from juego import juego
                    return
                elif evento.key == pygame.K_2:
                    dificultad = 'Intermedio'
                    config.velocidad_bola(dificultad)
                    from juego import juego
                    return
                elif evento.key == pygame.K_3:
                    dificultad = 'Dificil'
                    config.velocidad_bola(dificultad)
                    from juego import juego
                    return


# Pantalla de selección de dificultad
def seleccionar_dificultad1Jug():
    global dificultad
    while True:
        VENTANA.fill(NEGRO)
        mostrar_mensaje("Selecciona la dificultad:", BLANCO, (ANCHO // 2 - 200, ALTO // 2 - 100))
        mostrar_mensaje("1. Facil", BLANCO, (ANCHO // 2 - 150, ALTO // 2))
        mostrar_mensaje("2. Intermedio", BLANCO, (ANCHO // 2 - 150, ALTO // 2 + 50))
        mostrar_mensaje("3. Dificil", BLANCO, (ANCHO // 2 - 150, ALTO // 2 + 100))
        pygame.display.flip()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    dificultad = 'Facil'
                    config.velocidad_bola(dificultad)
                    from solo import solo
                    return
                elif evento.key == pygame.K_2:
                    dificultad = 'Intermedio'
                    config.velocidad_bola(dificultad)
                    from solo import solo
                    return
                elif evento.key == pygame.K_3:
                    dificultad = 'Dificil'
                    config.velocidad_bola(dificultad)
                    from solo import solo
                    return