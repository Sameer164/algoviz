import time
from .cell import Cell
from geometry import Point, Line

class Maze:
    def __init__(self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None
    ):
        
        self.__start_x = x1
        self.__start_y = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = win
        self.create_cells()

    def create_cells(self):
        self._cells = [[None] * self.__num_cols for _ in range(self.__num_rows)]
        current_x = self.__start_x
        for i in range(self.__num_rows):
            current_y = self.__start_y
            for j in range(self.__num_cols):
                self._cells[i][j] = Cell(current_x, current_y, current_x+self.__cell_size_x, current_y+self.__cell_size_y, self.__window)
                current_y += self.__cell_size_y
            current_x += self.__cell_size_x
        
        [self.draw_cell(i, j) for j in range(self.__num_cols) for i in range(self.__num_rows)]

    
    def draw_cell(self, i, j):
        if not self.__window:
            return
        self._cells[i][j].draw()
        self._animate()
    
    def _animate(self):
        self.__window.redraw()
        time.sleep(0.05)

        
        


        