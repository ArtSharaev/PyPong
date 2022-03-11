import pygame


class Ball:
    """Configurable ball for pong"""
    def __init__(self, coords, radius, color, direction=(10, 10)):
        self.coords, self.radius, self.color = coords, radius, color
        # moving per frame in pixels along the x and y axes
        self.direction = direction

    def render(self, screen):
        pygame.draw.circle(screen, (0, 0, 0),
                           (self.coords[0], self.coords[1]), self.radius)
        pygame.draw.circle(screen, self.color,
                           (self.coords[0], self.coords[1]), self.radius - 2)

    def move(self, screen):
        self.coords = (self.coords[0] + self.direction[0],
                       self.coords[1] + self.direction[1])
        self.render(screen)

    def touch_left_racket(self, rocketclass):
        # difficult rebound mechanics to the
        c = self.coords[1]
        r = self.radius
        rc = rocketclass.coords[1]
        rs = rocketclass.size[1]
        x = self.direction[0]
        y = self.direction[1]
        multiplier = 1
        if (self.coords[0] <= rocketclass.coords[0] + self.radius +
                rocketclass.size[0]):  # behind the racket
            if (c >= rc - r) and (c <= rc + rs + r):  # falling in a racket
                if (x <= 0) and (y >= 0):  # the ball moves from top to bottom
                    multiplier = -1
                elif (x <= 0) and (y <= 0):  # the ball moves from bottom to top
                    multiplier = 1
                if (c >= rc - r) and (c < rc + rs // 5):
                    y1 = multiplier * (x // 3)
                    x1 = 15 + y1 * multiplier
                    self.direction = (x1, y1)
                elif (c >= rc + rs // 5) and (c < rc + (rs // 5) * 2):
                    y1 = multiplier * (x // 2)
                    x1 = 15 + y1 * multiplier
                    self.direction = (x1, y1)
                elif (c >= rc + (rs // 5) * 2) and (c < rc + (rs // 5) * 3):
                    y1 = y
                    x1 = -1 * x
                    self.direction = (x1, y1)
                elif (c >= rc + (rs // 5) * 3) and (c < rc + (rs // 5) * 4):
                    y1 = multiplier * (x // 2)
                    x1 = 15 + y1 * multiplier
                    self.direction = (x1, y1)
                elif (c >= rc + (rs // 5) * 4) and (c <= rc + rs + r):
                    y1 = multiplier * (x // 3)
                    x1 = 15 + y1 * multiplier
                    self.direction = (x1, y1)
            else:
                return 'goal'

    def touch_right_racket(self, rocketclass):
        c = self.coords[1]
        r = self.radius
        rc = rocketclass.coords[1]
        rs = rocketclass.size[1]
        x = self.direction[0]
        y = self.direction[1]
        multiplier = 1
        if self.coords[0] >= rocketclass.coords[0] - self.radius:  # behind the racket
            if (c >= rc - r) and (c <= rc + rs + r):  # falling in a racket
                if (x >= 0) and (y >= 0):  # the ball moves from top to bottom
                    multiplier = 1
                elif (x >= 0) and (y <= 0):  # the ball moves from bottom to top
                    multiplier = -1
                if (c >= rc - r) and (c < rc + rs // 5):
                    y1 = multiplier * (x // 3)
                    x1 = -15 + y1 * multiplier
                    self.direction = (x1, y1)
                elif (c >= rc + rs // 5) and (c < rc + (rs // 5) * 2):
                    y1 = multiplier * (x // 2)
                    x1 = -15 + y1 * multiplier
                    self.direction = (x1, y1)
                elif (c >= rc + (rs // 5) * 2) and (c < rc + (rs // 5) * 3):
                    y1 = y
                    x1 = -1 * x
                    self.direction = (x1, y1)
                elif (c >= rc + (rs // 5) * 3) and (c < rc + (rs // 5) * 4):
                    y1 = multiplier * (x // 2)
                    x1 = -15 + y1 * multiplier
                    self.direction = (x1, y1)
                elif (c >= rc + (rs // 5) * 4) and (c < rc + rs + r):
                    y1 = multiplier * (x // 3)
                    x1 = -15 + y1 * multiplier
                    self.direction = (x1, y1)
            else:
                return 'goal'

    def touch_wall(self, screen):
        if (self.coords[1] <= 15 + self.radius) or\
                (self.coords[1] >= screen.get_size()[1] - 115 - self.radius):
            self.direction = (self.direction[0], -1 * self.direction[1])
            return True
