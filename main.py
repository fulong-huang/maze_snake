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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    snake.change_direction((-1, 0))
                if event.key == pygame.K_a:
                    snake.change_direction((0, -1))
                if event.key == pygame.K_s:
                    snake.change_direction((1, 0))
                if event.key == pygame.K_d:
                    snake.change_direction((0, 1))
        snake.move()
        window.clear()
        maze.draw()
        snake.draw()
        window.draw()
    print("Exit")

if __name__ == "__main__":
    main()

