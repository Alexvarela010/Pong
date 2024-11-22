import pygame
import sys
import subprocess
from config import *
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

class Ganador:
    def __init__(self, player):
        self.player = player

    def pantalla(self):
        while True:
            VENTANA.fill(NEGRO)

            mostrar_mensaje("¡El ganador es:", BLANCO, (ANCHO // 2 - 200, ALTO // 2 - 50))
            mostrar_mensaje(f"{self.player}!", BLANCO, (ANCHO // 2 - 150, ALTO // 2))
            mostrar_mensaje("Oprime 1 para volver al menú principal", BLANCO, (ANCHO // 2 - 250, ALTO // 2 + 100))

            pygame.display.flip()

            # Detectar eventos
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_1:
                        # Usar subprocess para reiniciar el script
                        subprocess.run([sys.executable, sys.argv[0]])  # Ejecuta el script nuevamente
                        pygame.quit()
                        sys.exit()


            RELOJ.tick(60)

    # Pantalla de selección de dificultad
    def seleccionar_dificultad():
        global dificultad
        while True:
            pantalla.fill(NEGRO)
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
                        return
                    elif evento.key == pygame.K_2:
                        dificultad = 'Intermedio'
                        return
                    elif evento.key == pygame.K_3:
                        dificultad = 'Dificil'
                        return

    def configurar_dificultad():
        global velocidad_paleta, velocidad_pelota_x, velocidad_pelota_y
        if dificultad == 'Facil':
            velocidad_pelota_x = 4
            velocidad_paleta = 5
        elif dificultad == 'Intermedio':
            velocidad_pelota_x = 7
            velocidad_paleta = 8
        elif dificultad == 'Dificil':
            velocidad_pelota_x = 10
            velocidad_paleta = 11

