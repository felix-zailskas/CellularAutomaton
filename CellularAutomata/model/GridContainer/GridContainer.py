import numpy as np


class GridContainer:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid = np.empty([self.rows, self.cols], dtype=int)

    def print_values(self):
        print("Rows: ", self.rows, "Cols:", self.cols)

    def print_cells(self):
        print("[")
        for i in range(self.rows):
            print("[", end="")
            for j in range(self.cols):
                print(self.grid[i][j], end="", sep="")
                if j < self.cols - 1:
                    print(", ", end="")
            print("]", end="")
            if j < self.cols - 1:
                print(",")
        print("\n]")

    def set_cells(self, cells: [[int]] = None):
        """
        Sets the cells of the Grid.
        A 2D integer array can be given to initialize the cells with
        that array. If no array is given then the grid is initialized randomly.

        :param cells:
        :return:
        """
        # fill with given cells
        if cells is not None:
            self.grid = np.array(cells, dtype=int)
            return
        # fill randomly
        self.grid = np.around(np.random.rand(self.rows, self.cols)).astype(int)

    def get_neighbors(self, row, col):
        """
        Returns a list of tuples of the coordinates of all neighbors of a given cell of the grid, which are not out of
        bounds. Considers the following neighbors: (x+1, y), (x-1, y), (x, y+1), (x, y-1)

        :param row: Row of the cell
        :param col: Column of the cell
        :return: List of the four neighbors
        """
        neighbors = []
        if row > 0:
            neighbors.append((row - 1, col))
        if col > 0:
            neighbors.append((row, col - 1))
        if row < self.rows - 1:
            neighbors.append((row + 1, col))
        if col < self.cols - 1:
            neighbors.append((row, col + 1))
        return neighbors
