from CellularAutomata.model.GridContainer.CellularAutomataModel import CellularAutomatonModel
import numpy as np


class GridInitializer:
    """
    Class that initializes different grid types.
    """
    @staticmethod
    def initialize_with_preset(size: (int, int), preset: [[int]], pos: (int, int) = (0, 0)):
        """
        Initializes a grid with all zeros and places a smaller preset grid inside of the grid.
        Only adds the preset if it fits into the grid.

        :param size: Row and Column size of the grid
        :param preset: Preset to be added to the grid
        :param pos: Top left position of where the preset should be placed
        :return: Initialized grid
        """
        x, y = pos
        rows, cols = size
        try:
            assert rows >= preset.shape[0] + y and cols >= preset.shape[1] + x
        except AssertionError:
            print("Preset is too large for Automaton or placed to close to the edge!")
            return np.zeros((rows, cols))
        cells = np.zeros((rows, cols))
        cells[y:preset.shape[0] + y, x:preset.shape[1] + x] = preset
        return cells

    @staticmethod
    def initialize_random(size: (int, int)):
        """
        Initializes a grid with random values of either 0 or 1.

        :param size: Row and Column size of the grid
        :return: Initialized grid
        """
        rows, cols = size
        return np.around(np.random.rand(rows, cols)).astype(int)

    @staticmethod
    def initialize_random_row(size: (int, int), row: int):
        """
        Initializes one row of a grid with random values of either 0 or 1.

        :param size: Row and Column size of the grid
        :param row: Row to initialize
        :return: Initialized grid
        """
        rows, cols = size
        cells = np.zeros((rows, cols))
        cells[row] = np.around(np.random.rand(cols)).astype(int)
        return cells

    @staticmethod
    def initialize_cell(size: (int, int), row: int, col: int):
        """
        Initializes a grid as all 0's except for one cell which is initialized as a 1.

        :param size: Row and Column size of the grid
        :param row: Row of the cell to initialize as 1
        :param col: Column of the cell to initialize as 1
        :return: Initialized grid
        """
        rows, cols = size
        cells = np.zeros((rows, cols))
        cells[row][col] = 1
        return cells

    @staticmethod
    def initialize_lines(size: (int, int), horizontal: bool = True, vertical: bool = False):
        """
        Initializes a grid with horizontal and/or vertical lines.

        :param size: Row and Column size of the grid
        :param horizontal: True if horizontal lines should be initialized
        :param vertical: True if vertical lines should be initialized
        :return: Initialized grid
        """
        rows, cols = size
        cells = np.empty((rows, cols))
        for i in range(rows):
            if vertical:
                cells[i] = np.ones(cols, dtype=int) if i % 2 == 0 else np.zeros(cols, dtype=int)
            if horizontal:
                for j in range(cols):
                    cells[i][j] = 1 if (j + 1) % 2 == 0 else cells[i][j]
        return cells

    @staticmethod
    def initialize_checkered(size: (int, int)):
        """
        Initializes a checkered grid.

        :param size: Row and Column size of the grid
        :return: Initialized grid
        """
        rows, cols = size
        cells = np.empty((rows, cols))
        for i in range(rows):
            for j in range(cols):
                cells[i][j] = 1 if (j + i) % 2 == 0 else 0
        return cells

