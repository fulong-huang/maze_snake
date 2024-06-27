from random import choice

class Snake:
    def __init__(self, start_x, start_y, row, col, block_width, snake_width, window, maze):
        self._block_width = block_width
        self._snake_width = snake_width
        self._row = row
        self._col = col
        self._window = window
        self._start_x = start_x
        self._start_y = start_y
        self._pad_snake_x = start_x + (block_width - snake_width) / 2
        self._pad_snake_y = start_y + (block_width - snake_width) / 2
        self._maze = maze

        self.body = [(0, 0), (1, 0)]
        self.head = (1, 1)
        self.curr_direction = (0, 1)
        self.target_direction = (0, -1)

        self.running = False
        self.lose = False
        self.win = False
        self.apple = (0, 0)
        self._spawn_apple()


    def reset(self):
        self.body = [(0, 0), (1, 0)]
        self.head = (1, 1)
        self.curr_direction = (0, 1)
        self.target_direction = (0, -1)

        self.apple = (0, 0)
        self._spawn_apple()
        self.running = False
        self.lose = False
        self.win = False

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
        if self.lose:
            self._draw_end_game()
            self._window.draw_text("YOU LOSE", 
                                   self._block_width * self._col,
                                   self._block_width * self._row)
        elif self.win:
            self._window.draw_text("YOU WIN!!!",
                                   self._block_width * self._col,
                                   self._block_width * self._row)
        elif not self.running:
            self._window.draw_text("Press any key to start",
                                   self._block_width * self._col,
                                   self._block_width * self._row)
    
    def _draw_end_game(self):
        if self.curr_direction[0] == 1:
            self._window.draw_rect(
                    self.head[1] * self._block_width + self._pad_snake_x,
                    self.head[0] * self._block_width + self._pad_snake_y + self._snake_width * 2/3,
                    self._snake_width, self._snake_width*3/5,
                    color = self._window._FRUIT
                    )
        elif self.curr_direction[0] == -1:
            self._window.draw_rect(
                    self.head[1] * self._block_width + self._pad_snake_x,
                    self.head[0] * self._block_width + self._pad_snake_y-self._snake_width*4/15,
                    self._snake_width, self._snake_width*3/5,
                    color = self._window._FRUIT
                    )

        elif self.curr_direction[1] == 1:
            self._window.draw_rect(
                    self.head[1] * self._block_width + self._pad_snake_x + self._snake_width * 2/3,
                    self.head[0] * self._block_width + self._pad_snake_y,
                    self._snake_width * 3/5, self._snake_width,
                    color = self._window._FRUIT
                    )
        else:
            self._window.draw_rect(
                    self.head[1] * self._block_width + self._pad_snake_x-self._snake_width*4/15,
                    self.head[0] * self._block_width + self._pad_snake_y,
                    self._snake_width * 3/5, self._snake_width,
                    color = self._window._FRUIT
                    )

    def move(self):
        self._turn()
        new_head = (self.head[0] + self.curr_direction[0],
                    self.head[1] + self.curr_direction[1])

        
        if new_head[0] == self.apple[0] and new_head[1] == self.apple[1]:
            self.body.append(self.head)
            self.head = new_head
            self._spawn_apple()
            return 
        elif self._check_self_collision(new_head):
            # TODO: Collied, game over?
            self.running = False
            self.lose = True
            return
        elif self._maze.collid_with_wall(self.head, new_head):
            # TODO: Collied with wall, end game?
            self.running = False
            self.lose = True
            return 
        

        prev = self.head
        for i in range(len(self.body)-1, -1, -1):
            prev, self.body[i] = self.body[i], prev
        self.head = new_head

        if( not 0 <= new_head[0] < self._row or
            not 0 <= new_head[1] < self._col):
            # TODO: move is not valid, end game?
            self.running = False
            self.win = True
            return 
        return 

    def change_direction(self, new_direction):
        if self.running:
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

        if len(empty_block) == 0:
            self._maze.remove_outer_walls()
        self.apple = choice(empty_block)

    def _check_self_collision(self, head_pos):
        for i in range(1, len(self.body)):
            if (head_pos[1] == self.body[i][1] and 
                head_pos[0] == self.body[i][0]):
                return True
        return False

