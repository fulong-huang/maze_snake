from random import choice

class Snake:
    def __init__(self, start_x, start_y, row, col, block_width, snake_width, window):
        self._block_width = block_width
        self._snake_width = snake_width
        self._row = row
        self._col = col
        self._window = window
        self._start_x = start_x
        self._start_y = start_y
        self._pad_snake_x = start_x + (block_width - snake_width) / 2
        self._pad_snake_y = start_y + (block_width - snake_width) / 2

        self.body = [(-1, 8), (-1, 7)]
        self.head = (-1, 6)
        self.curr_direction = (0, -1)
        self.target_direction = (0, -1)

        self.apple = (0, 0)
        self._spawn_apple()

    def draw(self):
        self._window.draw_rect(
                self.head[1]*self._block_width + self._pad_snake_x,
                self.head[0]*self._block_width + self._pad_snake_y,
                self._snake_width, self._snake_width,
                (100, 100, 100)
                )
        for row, col in self.body:
            self._window.draw_rect(
                    col * self._block_width + self._pad_snake_x,
                    row * self._block_width + self._pad_snake_y,
                    self._snake_width, self._snake_width,
                    color = self._window._SNAKE
                    )
        self._window.draw_circle(
                (self.apple[1]+0.5)*self._block_width + self._start_x,
                (self.apple[0]+0.5)*self._block_width + self._start_y,
                self._block_width * 0.4
                )

    def move(self):
        self._turn()
        new_head = (self.head[0] + self.curr_direction[0],
                    self.head[1] + self.curr_direction[1])
        if( not -3 < new_head[0] < self._row + 2 or
            not -3 < new_head[1] < self._col + 2):
            return
        
        if new_head[0] == self.apple[0] and new_head[1] == self.apple[1]:
            self.body.append(self.head)
            self.head = new_head
            self._spawn_apple()
            return

        prev = self.head
        for i in range(len(self.body)-1, -1, -1):
            prev, self.body[i] = self.body[i], prev
        self.head = new_head

    def change_direction(self, new_direction):
        self.target_direction = new_direction

    def _turn(self):
        if (self.curr_direction[0] == -self.target_direction[0] or
            self.curr_direction[1] == -self.target_direction[1]):
            return
        self.curr_direction = self.target_direction

    def _spawn_apple(self):
        empty_block = []
        for i in range(self._row):
            for j in range(self._col):
                if (i, j) not in self.body:
                    empty_block.append((i, j))
        self.apple = choice(empty_block)

