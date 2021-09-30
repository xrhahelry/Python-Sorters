import pygame
import random

WIDTH, HEIGHT = 800, 600
GRAY = (76, 76, 76)
WHITE = (255, 255, 255)
FPS = 20
lines = []
W = 10

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quick Sort!")

def create_array_of_lines():
    w = (WIDTH//W) - (WIDTH//(W*10)-1)
    for i in range(w):
        length = random.randrange(10,HEIGHT)
        lines.append(length)

def swap(lines, a, b):
    temp = lines[a]
    lines[a] = lines[b]
    lines[b] = temp

def partition(lines, start, end):
    pIndex = start
    pValue = lines[end]

    for i in range(start,end):
        if lines[i] < pValue:
            swap(lines, i, pIndex)
            draw_rectangles()
            pIndex += 1

    swap(lines, pIndex, end)
    return pIndex


def quicksort(lines, start, end):
    if start >= end:
        return

    index = partition(lines, start, end)

    quicksort(lines, start, index - 1)
    quicksort(lines, index + 1, end)

def draw_rectangles():
    posx = 0
    WIN.fill(GRAY)
    for length in lines:
        pygame.draw.rect(WIN, WHITE, (posx, HEIGHT-length, W, length))
        posx += (W+1)
    pygame.time.delay(5)
    pygame.display.update()

def draw_window():
    WIN.fill(GRAY)
    quicksort(lines, 0, len(lines)-1)

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

create_array_of_lines() 
main() 
