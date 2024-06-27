from random import choice, random
from cell import Cell
class Maze:
    def __init__(self, start_x, start_y,
                 rows, cols,
                 sub_rows, sub_cols,
                 cell_width, window):
        self._start_x = start_x
        self._start_y = start_y
        self._rows = rows
        self._cols = cols
        self._sub_rows = sub_rows
        self._sub_cols = sub_cols
        self._cell_width = cell_width
        self._window = window
        self._cells = []
        self._create_cells()
        self._create_maze()

    def reset(self):
        self._cells = []
        self._create_cells()
        self._create_maze()


    def remove_outer_walls(self):
        for i in range(self._rows):
            self._cells[i][0].left = False
        for i in range(self._rows):
            self._cells[i][-1].right = False

        for i in range(self._cols):
            self._cells[0][i].top = False
        for i in range(self._cols):
            self._cells[-1][i].bot = False
    
    def collid_with_wall(self, start, end):
        start_row = start[0] // self._sub_rows
        end_row = end[0] // self._sub_rows
        start_col = start[1] // self._sub_cols
        end_col = end[1] // self._sub_cols

        same_row = start_row == end_row
        same_col = start_col == end_col
        if(same_row and same_col):
            return False
        if not same_col:
            if start_col > end_col:
                return self._cells[start_row][start_col].left
            return self._cells[start_row][start_col].right
        if not same_row:
            if start_row > end_row:
                return self._cells[start_row][start_col].top
            return self._cells[start_row][start_col].bot




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
        # self._break_random_wall()

    def _break_random_wall(self):
        for i in range(0, self._rows-1):
            for j in range(0, self._cols-1):
                if random() < 0.2:
                    self._cells[i][j].right = False
                    self._cells[i][j+1].left = False
                if random() < 0.2:
                    self._cells[i][j].bot = False
                    self._cells[i+1][j].top = False
        
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
    

