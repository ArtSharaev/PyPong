import pygame
from pygame.locals import *
from random import choice

from ballclass import Ball
from rocketclass import Rocket


FPS = 120
# red_rocket = blue_rocket = ball = None


def change_text_brightness(brightness, color):
    r, g, b = color[0], color[1], color[2]
    if brightness < r:
        cr = brightness
    else:
        cr = r
    if brightness < g:
        cg = brightness
    else:
        cg = g
    if brightness < b:
        cb = brightness
    else:
        cb = b
    return cr, cg, cb


def draw_menu(screen, brightness):
    screen.fill((50, 50, 50))
    font = pygame.font.Font('fonts/wide_latin.ttf', 100)
    text = font.render("PyPong", True,
                       change_text_brightness(brightness, (255, 255, 50)))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 - 50
    screen.blit(text, (text_x, text_y))
    font = pygame.font.Font(None, 50)
    text = font.render("Press space key to start!", True,
                       change_text_brightness(brightness, (255, 255, 50)))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 + 40
    screen.blit(text, (text_x, text_y))


def draw_game(screen, red_score, blue_score):
    screen.fill((150, 150, 150))
    pygame.draw.line(screen, (255, 255, 255),
                     (screen.get_size()[0] // 2, 0),
                     (screen.get_size()[0] // 2, screen.get_size()[1] - 101),
                     10)
    pygame.draw.rect(screen, (0, 0, 0),
                     (0, 0, screen.get_size()[0], screen.get_size()[1] - 100),
                     15)
    pygame.draw.rect(screen, (0, 0, 0),
                     (0, screen.get_size()[1] - 115, screen.get_size()[0], 115),
                     15)
    font = pygame.font.Font(None, 100)
    text = font.render(str(red_score) + "  -  " + str(blue_score),
                       True, (0, 0, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = screen.get_size()[1] - 90
    screen.blit(text, (text_x, text_y))


def start_new_round():
    global ball
    if choice([True, False]):
        ball = Ball((screen.get_size()[0] // 2,
                     (screen.get_size()[1] - 115) // 2),
                    20, (255, 255, 0), (5, 0))
    else:
        ball = Ball((screen.get_size()[0] // 2,
                     (screen.get_size()[1] - 115) // 2),
                    20, (255, 255, 0), (-5, 0))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('PyPong')
    size = width, height = 1300, 700
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = True
    in_menu = True
    red_score = 0
    blue_score = 0
    timecount = 50
    red_rocket = Rocket((13, (screen.get_size()[1] - 115) // 2 - 115),
                        (30, 230), (255, 38, 54))
    blue_rocket = Rocket((screen.get_size()[0] - 45,
                          (screen.get_size()[1] - 115) // 2 - 115),
                         (30, 230), (66, 133, 180))
    start_new_round()
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and in_menu:
                    in_menu = False
        if pygame.key.get_pressed()[K_w] and not in_menu:
            red_rocket.move('up', screen)
        if pygame.key.get_pressed()[K_s] and not in_menu:
            red_rocket.move('down', screen)
        if pygame.key.get_pressed()[K_UP] and not in_menu:
            blue_rocket.move('up', screen)
        if pygame.key.get_pressed()[K_DOWN] and not in_menu:
            blue_rocket.move('down', screen)
        if in_menu:
            draw_menu(screen, timecount)
            timecount += 1
        else:
            draw_game(screen, red_score, blue_score)
            red_rocket.render(screen)
            blue_rocket.render(screen)
            if ball.check_left_rocket_collision(red_rocket) == 'goal':
                blue_score += 1
                start_new_round()
            if ball.check_right_rocket_collision(blue_rocket) == 'goal':
                red_score += 1
                start_new_round()
            ball.check_wall_collision(screen)
            ball.move(screen)
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()