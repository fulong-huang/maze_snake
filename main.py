import pygame
from window import Window


def main():
    window = Window()
    running = True
    clock = pygame.time.Clock()

    while running:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        window.clear()
        window.draw_square(300, 200, 100, 100)
        window.draw()
    print("Exit")

if __name__ == "__main__":
    main()

