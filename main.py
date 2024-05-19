import pygame
from window import Window
from maze import Maze


def main():
    window = Window()
    running = True
    clock = pygame.time.Clock()
    maze = Maze(200, 100, 8, 6, 50, window)

    while running:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        window.clear()
        maze.draw()
        window.draw()
    print("Exit")

if __name__ == "__main__":
    main()

