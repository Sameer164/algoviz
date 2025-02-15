from geometry import Point, Line

class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        self.has_left_wall, self.has_right_wall, self.has_top_wall, self.has_bottom_wall = True, True, True, True
        self.__x1, self.__y1, self.__x2, self.__y2 = x1, y1, x2, y2
        self.__win = win
    
    def draw(self):
        if self.has_bottom_wall:
            # The convention is this: 0,0 is top left and m,m is bottom right
            bottom_x = max(self.__x1, self.__x2)
            p1, p2 = Point(bottom_x, self.__y1), Point(bottom_x, self.__y2)
            self.__win.draw_line(Line(p1, p2), "white")
        
        if self.has_top_wall:
            # The convention is this: 0,0 is top left and m,m is bottom right
            top_x = min(self.__x1, self.__x2)
            p1, p2 = Point(top_x, self.__y1), Point(top_x, self.__y2)
            self.__win.draw_line(Line(p1, p2), "white")
        
        if self.has_left_wall:
            # The convention is this: 0,0 is top left and m,m is bottom right
            left_y = min(self.__y1, self.__y2)
            p1, p2 = Point(self.__x1, left_y), Point(self.__x2, left_y)
            self.__win.draw_line(Line(p1, p2), "white")
        
        if self.has_right_wall:
            # The convention is this: 0,0 is top left and m,m is bottom right
            right_y = max(self.__y1, self.__y2)
            p1, p2 = Point(self.__x1, right_y), Point(self.__x2, right_y)
            self.__win.draw_line(Line(p1, p2), "white")
    
    def draw_move(self, to_cell, undo=False):
        color = "red" if not undo else "gray"
        mid_x = (self.__x1 + self.__x2) // 2
        mid_y = (self.__y1 + self.__y2) // 2

        other_mid_x = (to_cell.__x1 + to_cell.__x2) // 2
        other_mid_y = (to_cell.__y1 + to_cell.__y2) // 2

        line = Line(Point(mid_x, mid_y), Point(other_mid_x, other_mid_y))
        self.__win.draw_line(line, color)



