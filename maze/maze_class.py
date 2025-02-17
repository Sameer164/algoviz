import time, random
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
        win = None, 
        seed = None,
    ):
        
        self.__start_x = x1
        self.__start_y = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = win
        if seed is not None:
            random.seed(seed)
        self.create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        

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

    def _break_entrance_and_exit(self):
        entrance, exit = self._cells[0][0], self._cells[-1][-1]
        entrance.has_top_wall = False
        self.draw_cell(0,0)
        exit.has_bottom_wall = False
        self.draw_cell(-1,-1)
    
    def __get_possible_cells_from(self, i, j):
        possible = []
        if i - 1  >= 0 and not self._cells[i - 1][j].visited:
            possible.append((i - 1, j))
        if i + 1 < self.__num_rows and not self._cells[i + 1][j].visited:
            possible.append((i + 1, j))
        if j - 1 >= 0 and not self._cells[i][j - 1].visited:
            possible.append((i, j - 1))
        if j + 1 < self.__num_cols and not self._cells[i][j + 1].visited:
            possible.append((i, j + 1))
        return possible

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            neighbors = self.__get_possible_cells_from(i, j)
            if not neighbors:
                self.draw_cell(i, j)
                return
            neighbor = random.choice(neighbors)
            if neighbor[0] > i:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            if neighbor[0] < i:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if neighbor[1] > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if neighbor[1] < j:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False  
            self._break_walls_r(*neighbor)

    def _reset_cells_visited(self):
        for i in range(self.__num_rows):
            for j in range(self.__num_cols):
                self._cells[i][j].visited = False 
    
    def solve(self):
        self.__solve_r(i=0,j=0)
    
    def __get_coords(self, i, j):
        return (self.__start_x + i * self.__cell_size_x + self.__cell_size_x // 2, self.__start_y + j * self.__cell_size_y + self.__cell_size_y//2)
    
    def __draw_mid_cell_lines(self, from_i, from_j, to_i, to_j, color):
        from_coords = self.__get_coords(from_i, from_j)
        to_coords = self.__get_coords(to_i, to_j)
        line = Line(Point(*from_coords), Point(*to_coords))
        line.draw(self.__window.canvas, color)


    def __solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.__num_rows - 1 and j == self.__num_cols - 1:
            return True
        
        neighbors = self.__get_possible_cells_from(i, j)
        for neighbor in neighbors:
            if neighbor[0] == i + 1:
                if not self._cells[i][j].has_right_wall:
                    self.__draw_mid_cell_lines(i, j, *neighbor, "green")
                    if self.__solve_r(*neighbor):
                        return True
                    else:
                        self.__draw_mid_cell_lines(i, j, *neighbor, "red")
            elif neighbor[0] == i - 1:
                if not self._cells[i][j].has_left_wall:
                    self.__draw_mid_cell_lines(i, j, *neighbor, "green")
                    if self.__solve_r(*neighbor):
                        return True
                    else:
                        self.__draw_mid_cell_lines(i, j, *neighbor, "red")
            elif neighbor[1] == j + 1:
                if not self._cells[i][j].has_bottom_wall:
                    self.__draw_mid_cell_lines(i, j, *neighbor, "green")
                    if self.__solve_r(*neighbor):
                        return True
                    else:
                        self.__draw_mid_cell_lines(i, j, *neighbor, "red")
            elif neighbor[1] == j - 1:
                if not self._cells[i][j].has_top_wall:
                    self.__draw_mid_cell_lines(i, j, *neighbor, "green")
                    if self.__solve_r(*neighbor):
                        return True
                    else:
                        self.__draw_mid_cell_lines(i, j, *neighbor, "red")
        return False 
    
    def draw_cell(self, i, j):
        if not self.__window:
            return
        self._cells[i][j].draw()
        self._animate()
    
    def _animate(self):
        self.__window.redraw()
        time.sleep(0.05)

        
        


        