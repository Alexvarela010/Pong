import pygame
from config import *

class Cuadrado:
    def __init__(self, x, y, direccion):
        self.rect = pygame.Rect(x, y, 10, 10)  # Usamos pygame.Rect para manejar las coordenadas y el tamaño
        self.direccion = direccion  # Dirección del movimiento

    def mover(self):
        # Mover el cuadrado según la dirección
        self.rect.x -= self.direccion[0]

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, BLANCO, self.rect)

    def colisionar_con_raquetas(self, raqueta1, raqueta2):
        # Verificar si el cuadrado colisiona con alguna de las raquetas
        if self.rect.colliderect(raqueta1) or self.rect.colliderect(raqueta2):
            return True
        return False

    def colisionar_con_bordes(self, ancho, alto):
        # Verificar si el cuadrado colisiona con los bordes
        if self.rect.left <= 0 or self.rect.right >= ancho:
            return True
        return False

    def colisionar_con_bloques(self, bloques, cuadrados_extra):
        """
        Detecta la colisión del cuadrado con los bloques.
        Si colisiona con un bloque, elimina el bloque y el cuadrado.
        """
        for c, columna in enumerate(bloques[:]):
            for bloque in columna[:]:
                if self.rect.colliderect(bloque):  # Si el cuadrado colisiona con el bloque
                    bloques[c].remove(bloque)  # Eliminar el bloque de la lista
                    cuadrados_extra.remove(self)  # Eliminar el cuadrado de la lista

                    return True  # Indica que el cuadrado ha colisionado con el bloque

        return False

