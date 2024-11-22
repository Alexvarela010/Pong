import pygame

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
ANCHO, ALTO = 900, 700
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pong")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
COLORES_BLOQUES1 = [(255, 0, 0), (0, 255, 0)]  # Rojo y Verde
COLORES_BLOQUES2 = [(255, 255, 0), (0, 0, 255)]

# FPS
FPS = 60
RELOJ = pygame.time.Clock()

# Jugadores y pelota
ANCHO_RAQUETA, ALTO_RAQUETA = 10, 100
RAQUETA1 = pygame.Rect(100, ALTO // 2 - ALTO_RAQUETA // 2, ANCHO_RAQUETA, ALTO_RAQUETA)
RAQUETA2 = pygame.Rect(ANCHO - 110, ALTO // 2 - ALTO_RAQUETA // 2, ANCHO_RAQUETA, ALTO_RAQUETA)
PELOTA = pygame.Rect(ANCHO // 2 - 15, ALTO // 2 - 15, 20, 20)

VELOCIDAD_PELOTA = [0,0]
dificultad1 = 'Dificil'
def velocidad_bola(dificultad):
    global dificultad1
    dificultad1 = dificultad
    print(dificultad1)

def get_dificultad():
    return dificultad1

print(dificultad1)

# Velocidades
if dificultad1 == 'Facil':
    VELOCIDAD_PELOTA = [4, 4]
elif dificultad1 == 'Intermedio':
    VELOCIDAD_PELOTA = [6, 6]
elif dificultad1 == 'Dificil':
    VELOCIDAD_PELOTA = [8, 8]
VELOCIDAD_RAQUETA = 5

# Bloques
BLOQUE_ANCHO, BLOQUE_ALTO = 20, 60  # Más estrechos y verticales
columnas = 2  # Dos columnas
filas = 9  # Menos bloques por fila
bloques1 = [[pygame.Rect(c * (BLOQUE_ANCHO + 10) + 20, f * (BLOQUE_ALTO + 10) + 50, BLOQUE_ANCHO, BLOQUE_ALTO)
            for f in range(filas)] for c in range(columnas)]

bloques2 = [[pygame.Rect(c * (BLOQUE_ANCHO + 10) + RAQUETA2.right + 30, f * (BLOQUE_ALTO + 10) + 50, BLOQUE_ANCHO, BLOQUE_ALTO)
            for f in range(filas)] for c in range(columnas)]

# Fuente para el puntaje (Ahora lo inicializamos aquí, después de pygame.init())
FUENTE = pygame.font.Font(None, 74)
