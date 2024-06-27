import pygame

class Window:
    _BG = (0, 0, 0)
    _WALL = (200, 200, 200)
    _FRUIT = (100, 0, 0)
    _SNAKE = (0, 50, 50)
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

    def draw_rect(self, x, y, width, height, color=_SNAKE):
        pygame.draw.rect(self._canvas, color, [x, y, width, height])

    def draw_circle(self, x, y, radius, color=_FRUIT):
        pygame.draw.circle(self._canvas, color, (x, y), radius)


    def draw_text(self, txt, width, height):
        green = (0, 255, 0)
        blue = (0, 0, 128)
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render(txt, True, green, blue)
        textRect = text.get_rect()
        textRect.center = (width//2, height//2)
        self._canvas.blit(text, textRect)




