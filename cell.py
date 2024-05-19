class Cell:
    def __init__(self, x1, y1, x2, y2, window):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._window = window

        self.top = True
        self.bot = True
        self.left = True
        self.right = True

        self.visited = False

    def draw(self):
        if self.top:
            self._window.draw_line(
                    (self._x1, self._y1),
                    (self._x2, self._y1)
                    )
        if self.bot:
            self._window.draw_line(
                    (self._x1, self._y2),
                    (self._x2, self._y2)
                    )
        if self.left:
            self._window.draw_line(
                    (self._x1, self._y1),
                    (self._x1, self._y2)
                    )
        if self.right:
            self._window.draw_line(
                    (self._x2, self._y1),
                    (self._x2, self._y2)
                    )
