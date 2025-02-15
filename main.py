from tkinter import Tk, BOTH, Canvas
from geometry import Point, Line
from maze import Cell

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
    win = Window(800, 600)
    cell1 = Cell(10,10,50,50, win)
    cell2 = Cell(100, 100, 150, 150, win)
    cell1.draw()
    cell2.draw()
    cell1.draw_move(cell2, undo=True)
    win.wait_for_close()
