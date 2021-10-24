import os
from .pygame_init import pygame


def load_image(name, size):
    image = pygame.transform.scale(pygame.image.load(os.path.join(images_folder, name)), size)
    if name[-3] == "j":
        return image.convert()
    return image.convert_alpha()


def load_sound(name, volume=1):
    sound = pygame.mixer.Sound(os.path.join(sounds_folder, name + ".wav"))
    sound.set_volume(volume)
    return sound


images_folder = "assets/images"
sounds_folder = "assets/sounds"
