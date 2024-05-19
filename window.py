import pygame

class Window:
    _BG = (0, 0, 0)
    _WALL = (200, 200, 200)
    _FRUIT = (100, 0, 0)
    def __init__(self, width=800, height=600):
        self._width = width
        self._height = height

        pygame.init()
        self._canvas = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption("Maze Snake")

    def clear(self):
        self._canvas.fill(Window._BG)
    
    def draw(self):
        pygame.display.flip()

    def draw_line(self, point1, point2, color=_WALL):
        pygame.draw.line(self._canvas, color, point1, point2)

    def draw_square(self, x, y, width, height, color=_FRUIT):
        pygame.draw.rect(self._canvas, color, [x, y, width, height])



