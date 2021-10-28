from tkinter import *
from CellularAutomata.model.GridContainer.GridContainer import GridContainer


class GridContainerCanvas(Canvas):
    """
    Tkinter Canvas that contains a GridContainer object.
    It displays the GridContainer object as 2D grid.
    """
    def __init__(self, master: Tk, grid_container: GridContainer, res=5):
        """
        Initializes a GridContainerCanvas.

        :param master: Tk object in which this Canvas exists
        :param grid_container: GridContainer that is displayed
        :param res: Size of one Grid cell
        """
        super().__init__(master, height=grid_container.rows * res, width=grid_container.cols * res, bg='white')
        self.height = grid_container.rows * res
        self.width = grid_container.cols * res
        self.res = res
        self.grid_container = grid_container
        self.colors = ['white', 'black', 'green', 'red', 'blue', 'pink']

    def update(self):
        """
        Redraws the Grid in which the GridContainer is displayed.

        :return: None
        """
        super().update()
        self.delete(ALL)
        for i in range(self.grid_container.cols):
            for j in range(self.grid_container.rows):
                color = 'white' if self.grid_container.grid[j][i] == 0 else 'black'
                x1 = i * self.res
                y1 = j * self.res
                x2 = (i + 1) * self.res
                y2 = (j + 1) * self.res
                self.create_rectangle(x1, y1, x2, y2, fill=color)
        # checkered grid
        for i in range(self.grid_container.cols):
            x = i * self.res
            self.create_line(x, 0, x, self.height, fill="#A9A9A9")
        for j in range(self.grid_container.rows):
            y = j * self.res
            self.create_line(0, y, self.width, y, fill="#A9A9A9")
