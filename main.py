from tkinter import Tk, BOTH, Canvas
from geometry import Point, Line
from maze import Maze

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Random window")
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        # Frameworks like Tkinter work sort of in an event loop. self.root is a GUI. updating it means getting all the key
        # presses, mouse clicks etc. Widget is something is displayed on the GUI. Now, canvas is a widget. When we update the 
        # canvas, the GUI needs to use this updated canvas. If we don't update the GUI, we won't see what new thing is added on 
        # the canvas. 
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color=fill_color)
        
    def close(self):
        self.running = False

if __name__ == "__main__":
    win = Window(810, 610)
    maze = Maze(x1=10, y1=10, num_rows=10, num_cols=15, cell_size_x=50, cell_size_y=50, win=win, seed = 5)
    maze.solve()
    win.wait_for_close()
