
class Snake:
    def __init__(self, start_x, start_y, block_width, snake_width, window):
        self._block_width = block_width
        self._snake_width = snake_width
        self._window = window
        self._pad_x = start_x + (block_width - snake_width) / 2
        self._pad_y = start_y + (block_width - snake_width) / 2

        self.body = [(-1, 7), (-1, 8)]
        self.head = (-1, 6)
        self.curr_direction = (0, -1)
        self.target_direction = (0, -1)

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
        self._turn()
        new_head = (self.head[0] + self.curr_direction[0],
                    self.head[1] + self.curr_direction[1])
        if( not -3 < new_head[0] < 22 or
            not -3 < new_head[1] < 30):
            return
        prev = self.head
        for i in range(len(self.body)):
            prev, self.body[i] = self.body[i], prev
        self.head = new_head

    def change_direction(self, new_direction):
        self.target_direction = new_direction

    def _turn(self):
        if (self.curr_direction[0] == -self.target_direction[0] or
            self.curr_direction[1] == -self.target_direction[1]):
            return
        self.curr_direction = self.target_direction



