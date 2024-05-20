import pygame
from window import Window
from maze import Maze
from snake import Snake


def main():
    window = Window()
    running = True
    clock = pygame.time.Clock()
    maze = Maze(50, 50, 5, 7, 100, window)
    snake = Snake(50, 50, 25, 20, window)

    while running:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        window.clear()
        maze.draw()
        snake.draw()
        window.draw()
    print("Exit")

if __name__ == "__main__":
    main()

