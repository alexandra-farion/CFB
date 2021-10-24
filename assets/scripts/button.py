from .pygame_init import pygame
from .colors import PowderBlue
from .audio_hub import click_sound


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((150, 50))
        self.image.fill(PowderBlue)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def click(self, x, y):
        if (self.rect.left <= x <= self.rect.right) and (self.rect.top <= y <= self.rect.bottom):
            click_sound.play()
