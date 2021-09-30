import pygame
import random
import time

WIDTH, HEIGHT = 1100, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Bubble Sorter!") 

BLACK = (33, 33, 33)
BLUE = (41, 45, 62) 
GRAY = (76, 76, 76)
WHITE = (255, 255, 255)
BROWN = (149, 134, 124)
FPS = 60
lines = []
W = 5

def create_array_of_lines(width, height):
    w = width//W
    for i in range(0,w):
        length = random.randrange(10,height)
        lines.append(length)

def sort_array_of_lines(height, lines): 
    length = len(lines) - 1 
    for i in range(0, length):
        for j in range(0, length - i):
            a = lines[j]
            b = lines[j+1]

            if a > b:
                temp = a
                lines[j] = b 
                lines[j+1] = temp
                WIN.fill(BROWN)
                draw_rectangles(lines, HEIGHT)
                pygame.display.update()

def draw_rectangles(lines, height):
    posx = 1
    state = 1
    for length in lines:
        if state % 2 == 0 :
            pygame.draw.rect(WIN, WHITE, (posx, height-length, W, length))
        else:
            pygame.draw.rect(WIN, BLACK, (posx, height-length, W, length))

        state += 1
        posx += W

def draw_window():
    WIN.fill(GRAY)
    sort_array_of_lines(HEIGHT, lines)

def main(): 
    clock = pygame.time.Clock()
    run = True 
    while run: 
        clock.tick(FPS)
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False

        draw_window() 

    pygame.quit() 


create_array_of_lines(WIDTH, HEIGHT) 
if __name__ == "__main__": 
    main() 
