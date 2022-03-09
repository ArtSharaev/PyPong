import pygame


class Rocket:

    def __init__(self, coords, size, color):
        self.coords, self.size, self.color = coords, size, color

    def render(self, screen):
        pygame.draw.rect(screen, (0, 0, 0),
                         (self.coords[0], self.coords[1],
                          self.size[0], self.size[1]),
                         2)
        pygame.draw.rect(screen, self.color,
                         (self.coords[0] + 2, self.coords[1] + 2,
                          self.size[0] - 4, self.size[1] - 4),
                         0)

    def move(self, key, screen):
        if key == 'up':
            if self.coords[1] - 5 < 15:
                self.coords = (self.coords[0], 15)
            else:
                self.coords = (self.coords[0], self.coords[1] - 5)
        elif key == 'down':
            if self.coords[1] + 5 > screen.get_size()[1] - 115 - self.size[1]:
                self.coords = (self.coords[0],
                               screen.get_size()[1] - 115 - self.size[1])
            else:
                self.coords = (self.coords[0], self.coords[1] + 5)