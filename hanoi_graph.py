import tkinter as tk
from math import sqrt
from functools import reduce


class HanoiGraph(tk.Tk):
    """HanoiGraph class definition."""

    def __init__(self):
        """Initialize the HanoiGraph class."""
        tk.Tk.__init__(self)

        self.title('Hanoi\'s triangle')

        self.width = 600
        self.height = self.width * sqrt(3.0)/2.0  # <- sin(60 deg) = sqrt(3)/2
        self.margin = 10

        self.canvas = tk.Canvas(self,
                                width=self.width + 2*self.margin,
                                height=self.height + 2*self.margin,
                                bg='white')
        self.canvas.pack()

        self.btn = tk.Button(self, text='Draw', command=self.draw)
        self.btn.pack(side=tk.LEFT, padx=self.margin)

        self.label = tk.Label(self, text='Number of plates')
        self.label.pack()

        self.plates = tk.Entry(self, width=3, justify=tk.CENTER)
        self.plates.insert(tk.INSERT, '1')
        self.plates.pack()

        # Draw the Hanoi graph
        self.draw()

        # Display
        self.resizable(0, 0)
        self.mainloop()

    def draw(self):
        """Draw the Hanoi graph."""
        # Clear previous canvas
        self.canvas.delete('all')

        # One must introduce an integer number of plates
        try:
            plates = int(self.plates.get())

            x1 = self.margin + 0
            y1 = self.margin + self.height
            x2 = self.margin + self.width/2
            y2 = self.margin + 0
            x3 = self.margin + self.width
            y3 = self.margin + self.height

            self.recursion(plates, x1, y1, x2, y2, x3, y3)
        except ValueError as err:
            self.canvas.create_text(self.width/2, self.height/2,
                                    text='Set a valid number of plates')
            raise err

    def recursion(self, plates, x1, y1, x2, y2, x3, y3):
        """Draw recursively a new level of the Hanoi graph."""
        if plates <= 1:
            # Draw the base case triangle
            self.canvas.create_line(x1, y1, x2, y2)
            self.canvas.create_line(x2, y2, x3, y3)
            self.canvas.create_line(x3, y3, x1, y1)
        else:
            plates -= 1
            # Number of divisions for each side for a given number of plates
            divs = reduce(lambda x, _: 2*x + 1, range(1, plates+2))
            val = divs // 2

            # Compute the new triangles height and side
            length = val*(x2 - x1)/divs
            height = val*(y1 - y2)/divs

            # Draw recursively the triangles
            self.recursion(plates,
                           x1, y1,
                           x1 + length, y1 - height,
                           x1 + 2*length, y1)
            self.recursion(plates,
                           x2 - length, y2 + height,
                           x2, y2,
                           x2 + length, y2 + height)
            self.recursion(plates,
                           x3 - 2*length, y3,
                           x3 - length, y3 - height,
                           x3, y3)

            # Connect the triangles with lines
            self.canvas.create_line(x1 + length, y1 - height,
                                    x2 - length, y2 + height)
            self.canvas.create_line(x2 + length, y2 + height,
                                    x3 - length, y3 - height)
            self.canvas.create_line(x1 + 2*length, y1,
                                    x3 - 2*length, y3)


# Display the HanoiGraph class window
HanoiGraph()
