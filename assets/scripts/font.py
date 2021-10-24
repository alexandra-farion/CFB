from .pygame_init import *


class Font:
    def __init__(self, screen, size, text, x, y, color=pygame.Color("black")):
        self.screen = screen
        self.color = color

        self.font = pygame.font.Font(None, size)
        self.string = self.font.render(text, True, color)
        rect = self.string.get_rect()
        self.pos = (x - (rect.width / 2), y - (rect.height / 2))

    def render(self, text=None):
        if text is None:
            self.screen.blit(self.string, self.pos)
        else:
            self.screen.blit(self.font.render(text, True, self.color), self.pos)
