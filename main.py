import pygame
from window import Window
from maze import Maze
from snake import Snake


def main():
    window = Window()
    running = True
    clock = pygame.time.Clock()
    maze = Maze(50, 50, 5, 7, 4, 4, 100, window)
    snake = Snake(50, 50, 5*4, 7*4, 25, 20, window, maze)

    tick_time = 10
    while running:
        clock.tick(tick_time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if snake.win or snake.lose:
                    snake.reset()
                    maze.reset()
                elif snake.running == False:
                    snake.running = True
                if event.key == pygame.K_w:
                    snake.change_direction((-1, 0))
                if event.key == pygame.K_a:
                    snake.change_direction((0, -1))
                if event.key == pygame.K_s:
                    snake.change_direction((1, 0))
                if event.key == pygame.K_d:
                    snake.change_direction((0, 1))

                if event.key == pygame.K_SPACE:
                    tick_time = 30
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    tick_time = 10
        if snake.running:
            snake.move()
        window.clear()
        maze.draw()
        snake.draw()
        window.draw()
    print("Exit")

if __name__ == "__main__":
    main()

