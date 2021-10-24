from .pygame_init import pygame

info = pygame.display.Info()

SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h
HALF_SCREEN_WIDTH = SCREEN_WIDTH / 2
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT / 2

RESIZE_K = SCREEN_WIDTH / 1920


def calculate(value):
    return int(value * RESIZE_K)
