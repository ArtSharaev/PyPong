# Sorry for the trashed main file

import pygame
from pygame.locals import *
from random import choice

from objectclasses.ballclass import Ball
from objectclasses.racketclass import Racket

FPS = 120
RED = (255, 38, 54)
BLUE = (66, 133, 180)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)


def change_text_brightness(brightness, color):
    # increase the brightness until the desired color is obtained
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


def draw_menu_screen(screen, menuarray):
    screen.fill((50, 50, 50))
    font = pygame.font.Font('fonts/wide_latin.ttf', 80)
    text = font.render("PyPong", True, YELLOW)
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 10
    screen.blit(text, (text_x, text_y))
    font = pygame.font.Font(None, 70)
    text = font.render("PLAY", True, menuarray[0])
    text_x = width // 6 * 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 + 40
    screen.blit(text, (text_x, text_y))
    text = font.render("SETTINGS", True, menuarray[1])
    text_x = width // 6 * 4 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 + 40
    screen.blit(text, (text_x, text_y))


def draw_start_screen(screen, brightness):
    screen.fill((50, 50, 50))
    font = pygame.font.Font('fonts/wide_latin.ttf', 100)
    text = font.render("PyPong", True,
                       change_text_brightness(brightness, (255, 255, 50)))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 - 50
    screen.blit(text, (text_x, text_y))
    font = pygame.font.Font(None, 50)
    text = font.render("Press enter to start!", True,
                       change_text_brightness(brightness, (255, 255, 50)))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 + 40
    screen.blit(text, (text_x, text_y))


def draw_game_screen(screen, score1, score2):
    # there is no special class for the game screen
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
    text = font.render(str(score1) + "  -  " + str(score2),
                       True, (0, 0, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = screen.get_size()[1] - 90
    screen.blit(text, (text_x, text_y))


def start_new_round():
    global ball
    if choice([True, False]):  # the ball moves to the left or right side
        side = 1
    else:
        side = -1
    # place the ball in the center of the playing field
    ball = Ball((screen.get_size()[0] // 2,
                 (screen.get_size()[1] - 115) // 2),
                20, YELLOW, direction=(side * 5, 0))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('PyPong')
    size = width, height = 1300, 700
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    running = in_start_screen = True
    in_menu_screen = in_game_screen = False
    in_menu_screen = True
    in_start_screen = False
    red_score = blue_score = 0
    timecount = 50  # a simple time counter to change brightness of the menu
    red_racket = Racket((13, (screen.get_size()[1] - 115) // 2 - 115),
                        (30, 230), RED)
    blue_racket = Racket((screen.get_size()[0] - 45,
                          (screen.get_size()[1] - 115) // 2 - 115),
                         (30, 230), BLUE)
    start_new_round()
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and in_start_screen:
                    in_start_screen = False
                    in_menu_screen = True
                elif event.key == pygame.K_RETURN and in_menu_screen:
                    in_menu_screen = False
                    in_game_screen = True
        if pygame.key.get_pressed()[K_w] and in_game_screen:
            red_racket.move('u', screen)
        if pygame.key.get_pressed()[K_s] and in_game_screen:
            red_racket.move('d', screen)
        if pygame.key.get_pressed()[K_UP] and in_game_screen:
            blue_racket.move('u', screen)
        if pygame.key.get_pressed()[K_DOWN] and in_game_screen:
            blue_racket.move('d', screen)
        if in_start_screen:
            draw_start_screen(screen, timecount)
            timecount += 1
        elif in_menu_screen:
            draw_menu_screen(screen, [YELLOW, WHITE])
        elif in_game_screen:
            draw_game_screen(screen, red_score, blue_score)
            red_racket.render(screen, RED)
            blue_racket.render(screen, BLUE)
            if ball.touch_left_racket(red_racket) == 'goal':
                blue_score += 1
                start_new_round()
            if ball.touch_right_racket(blue_racket) == 'goal':
                red_score += 1
                start_new_round()
            ball.touch_wall(screen)
            ball.move(screen)
        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()