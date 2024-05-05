import pygame.display
from pygame import *
import sys
import time

pygame.init()

screen = pygame.display.set_mode((750, 750))

running = True
playing = False
BGC = (255, 255, 255)
speed = 1
maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0, 2, 1], [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 1, 1, 0, 1], [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1], [1, 0, 1, 1, 0, 1, 1, 1, 1, 1], [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

lives = 3
timer = 8
end_result = 0


def draw_maze():
    count1 = 0
    for i in maze:
        count2 = 0
        for n in i:
            if n == 1:
                pygame.draw.rect(screen, (0, 0, 0), (count2 * 75, count1 * 75, 75, 75))
            elif n == 2:
                pygame.draw.rect(screen, (255, 255, 0), (count2 * 75, count1 * 75, 75, 75))
            count2 += 1
        count1 += 1


player_x = 612
player_y = 612


def draw_screen():
    screen.fill(BGC)
    draw_maze()
    player = pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, 50, 50))
    screen.blit(pygame.font.SysFont("freesansbold.ttf", 52).render(str(lives) + " lives", True, (255, 0, 0)), (30, 20))
    screen.blit(pygame.font.SysFont("freesansbold.ttf", 52).render((str(timer) + " Seconds"), True, (254, 254, 254)),
                (300, 20))


def pos_check():
    global player_x, player_y, lives, playing, end_result

    # left
    if screen.get_at((player_x, player_y + 25)) == (0, 0, 0):
        player_x += 20
        lives -= 1
    # right
    elif screen.get_at((player_x + 50, player_y + 25)) == (0, 0, 0):
        player_x -= 20
        lives -= 1
    # up
    elif screen.get_at((player_x + 25, player_y)) == (0, 0, 0):
        player_y += 20
        lives -= 1
    # down
    elif screen.get_at((player_x + 25, player_y + 50)) == (0, 0, 0):
        player_y -= 20
        lives -= 1

    if screen.get_at((player_x + 50, player_y + 25)) == (255, 255, 0):
        playing = False
        end_result = 1


first_input = True
start_time = 0


def detect_first_input():
    global first_input, start_time, timer
    if first_input:
        first_input = False
        start_time = time.time()


def start():
    global playing, player_x, player_y, first_input, timer, lives
    draw_screen()
    playing = True
    first_input = True
    timer = 8
    lives = 3
    player_x = 612
    player_y = 612


start()

while running:
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    playing = False
                    running = False
                elif event.key == pygame.K_RETURN:
                    start()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= speed
            detect_first_input()
        if keys[pygame.K_RIGHT]:
            player_x += speed
            detect_first_input()
        if keys[pygame.K_UP]:
            player_y -= speed
            detect_first_input()
        if keys[pygame.K_DOWN]:
            player_y += speed
            detect_first_input()

        if not first_input:
            timer = (8 - round(time.time() - start_time))

        if lives == 0 or timer == 0:
            playing = False
            end_result = 2

        pos_check()

        draw_screen()
        pygame.display.update()

    if end_result == 1:
        screen.fill((0, 0, 255))
        screen.blit(pygame.font.SysFont("freesansbold.ttf", 152).render("YOU WIN!", True, (255, 0, 0)), (125, 300))
        screen.blit(pygame.font.SysFont("freesansbold.ttf", 75).render("Press ENTER to play again", True, (255, 0, 0)),
                    (50, 425))
    elif end_result == 2:
        screen.fill((255, 0, 0))
        screen.blit(pygame.font.SysFont("freesansbold.ttf", 152).render("GAME OVER!", True, (255, 255, 0)), (45, 300))
        screen.blit(
            pygame.font.SysFont("freesansbold.ttf", 75).render("Press ENTER to play again", True, (255, 255, 0)),
            (50, 425))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:
                start()

    pygame.display.update()

pygame.quit()
sys.exit()
