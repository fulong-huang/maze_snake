
class Snake:
    def __init__(self, start_x, start_y, block_width, snake_width, window):
        self._block_width = block_width
        self._snake_width = snake_width
        self._window = window
        self._pad_x = start_x + (block_width - snake_width) / 2
        self._pad_y = start_y + (block_width - snake_width) / 2

        self.body = [(-1, 8), (-1, 7)]
        self.head = (-1, 6)
        self.direction = (0, -1)

    def draw(self):
        self._window.draw_rect(
                self.head[1]*self._block_width + self._pad_x,
                self.head[0]*self._block_width + self._pad_y,
                self._snake_width, self._snake_width,
                )
        for row, col in self.body:
            self._window.draw_rect(
                    col * self._block_width + self._pad_x,
                    row * self._block_width + self._pad_y,
                    self._snake_width, self._snake_width,
                    color = self._window._SNAKE
                    )

    def move(self):
        pass



