from geometry import Point, Line

class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        self.has_left_wall, self.has_right_wall, self.has_top_wall, self.has_bottom_wall = True, True, True, True
        self.__x1, self.__y1, self.__x2, self.__y2 = x1, y1, x2, y2
        self.__win = win
        self.visited = False
    
    def draw(self):

        """
        If we don't have a black drawing when we don't have a border, nothing will change when we break a wall. 

        Before breaking our wall, we have already drawn on our canvas. Now, say we break a wall, call draw again, call window.redraw(), it will
        refresh the canvas widget. Now since we dont have a logic for what to draw when we dont have a wall, we will do nothing. 

        Which means whatever was drawn before is still there. 

        So, we need an else condition for each has_wall if condition. So, we draw black on top of the existing white whenever we break a wall.
        
        """

        bottom_y = max(self.__y1, self.__y2)
        p1, p2 = Point(self.__x1, bottom_y), Point(self.__x2, bottom_y)

        if self.has_bottom_wall:
            # The convention is this: 0,0 is top left and m,m is bottom right
            self.__win.draw_line(Line(p1, p2), "white")
        else:
            self.__win.draw_line(Line(p1, p2), "black")

        top_y = min(self.__y1, self.__y2)
        p1, p2 = Point(self.__x1, top_y), Point(self.__x2, top_y)
        if self.has_top_wall:
            # The convention is this: 0,0 is top left and m,m is bottom right
            self.__win.draw_line(Line(p1, p2), "white")
        else:
            self.__win.draw_line(Line(p1, p2), "black")

        left_x = min(self.__x1, self.__x2)
        p1, p2 = Point(left_x, self.__y1), Point(left_x, self.__y2)
        if self.has_left_wall:
            # The convention is this: 0,0 is top left and m,m is bottom right
            self.__win.draw_line(Line(p1, p2), "white")
        else:
            self.__win.draw_line(Line(p1, p2), "black")

        right_x = max(self.__x1, self.__x2)
        p1, p2 = Point(right_x, self.__y1), Point(right_x, self.__y2)
        if self.has_right_wall:
            # The convention is this: 0,0 is top left and m,m is bottom right
            self.__win.draw_line(Line(p1, p2), "white")
        else:
            self.__win.draw_line(Line(p1, p2), "black")

    
    def draw_move(self, to_cell, undo=False):
        color = "red" if not undo else "gray"
        mid_x = (self.__x1 + self.__x2) // 2
        mid_y = (self.__y1 + self.__y2) // 2

        other_mid_x = (to_cell.__x1 + to_cell.__x2) // 2
        other_mid_y = (to_cell.__y1 + to_cell.__y2) // 2

        line = Line(Point(mid_x, mid_y), Point(other_mid_x, other_mid_y))
        self.__win.draw_line(line, color)



