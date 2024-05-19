from cell import Cell
class Maze:
    def __init__(self, rows, cols, cell_width, window):
        self._rows = rows
        self._cols = cols
        self._cell_width = cell_width
        self._window = window
        self._cells = []

    def _create_cells(self):
        for r in range(self._rows):
            curr_row = []
            for c in range(self._cols):
                x = r*self._cell_width
                y = c * self._cell_width
                curr_row.append(
                        Cell(
                            x, y,
                            x+self._cell_width, y+self._cell_width,
                            self._window
                            )
                        )
            self._cells.append(curr_row)



