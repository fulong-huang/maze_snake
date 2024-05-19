from random import choice
from cell import Cell
class Maze:
    def __init__(self, start_x, start_y, rows, cols, cell_width, window):
        self._start_x = start_x
        self._start_y = start_y
        self._rows = rows
        self._cols = cols
        self._cell_width = cell_width
        self._window = window
        self._cells = []
        self._create_cells()
        self._create_maze()

    def _create_cells(self):
        for r in range(self._rows):
            curr_row = []
            for c in range(self._cols):
                x = c*self._cell_width + self._start_x
                y = r * self._cell_width + self._start_y
                curr_row.append(
                        Cell(
                            x, y,
                            x+self._cell_width, y+self._cell_width,
                            self._window
                            )
                        )
            self._cells.append(curr_row)

    def draw(self):
        for row in self._cells:
            for cell in row:
                cell.draw()

    def _create_maze(self):
        self._break_wall(0, 0)
        
    def _break_wall(self, i, j):
        self._cells[i][j].visited = True
        while True:
            valid_move = []
            if i > 0 and self._cells[i-1][j].visited == False:
                valid_move.append((i-1, j))
            if j > 0 and self._cells[i][j-1].visited == False:
                valid_move.append((i, j-1))
            if i < self._rows - 1 and self._cells[i+1][j].visited == False:
                valid_move.append((i+1, j))
            if j < self._cols - 1 and self._cells[i][j+1].visited == False:
                valid_move.append((i, j+1))
            if len(valid_move) == 0:
                break
            move_i, move_j = choice(valid_move)
            if move_i != i:
                if move_i < i:
                    self._cells[i][j].top = False
                    self._cells[i-1][j].bot = False
                else:
                    self._cells[i][j].bot = False
                    self._cells[i+1][j].top = False
            else:
                if move_j < j:
                    self._cells[i][j].left = False
                    self._cells[i][j-1].right = False
                else:
                    self._cells[i][j].right = False
                    self._cells[i][j+1].left = False

            self._break_wall(move_i, move_j)
    

