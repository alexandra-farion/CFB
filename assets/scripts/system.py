import sys
import os
from .pygame_init import pygame


def terminate():
    pygame.quit()
    os.abort()
    sys.exit()
