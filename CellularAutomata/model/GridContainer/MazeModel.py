import numpy as np
from CellularAutomata.model.GridContainer.CellularAutomataModel import CellularAutomatonModel
from CellularAutomata.model.GridContainer.GridContainer import GridContainer
from CellularAutomata.util.initialization.GridInitializer import GridInitializer
from CellularAutomata.util.rules.Rules import Rules
from CellularAutomata.util.filling.RegionFiller import RegionFiller
from CellularAutomata.util.filling.FloodFill import flood_fill
import random


class MazeModel(GridContainer):
    def __init__(self, rows: int, cols: int):
        super().__init__(rows, cols)
        self.start = (0, 0)
        self.goal = (0, 0)
        self.reachable = None

    def initialize(self, cells=None):
        if cells is not None:
            super().set_cells(np.array(cells))
            for row in range(self.grid.shape[0]):
                for col in range(self.grid.shape[1]):
                    if self.grid[row][col] == 2:
                        self.start = (row, col)
                    if self.grid[row][col] == 3:
                        self.goal = (row, col)
            return
        # Initialize with CA and Flood Fill
        ca = CellularAutomatonModel(self.rows, self.cols)
        ca.set_cells(GridInitializer.initialize_random((ca.rows, ca.cols)))
        # Fill CA with Majority rule as estimate of the map
        ca.become_stagnant(Rules.MAJORITY)
        # Fill all unreachable spots
        self.reachable = flood_fill(ca.grid, 0, 0)
        self.set_cells(RegionFiller.fill_region(ca.grid, 0, 0, flood_c=self.reachable))
        self.initialize_start_goal()

    def initialize_start_goal(self):
        assert self.reachable is not None
        self.start = random.choice(self.reachable)
        self.goal = random.choice(self.reachable)
        self.grid[self.start[1]][self.start[0]] = 2
        self.grid[self.goal[1]][self.goal[0]] = 3

    def set_start(self, x, y):
        self.start = (x, y)
        self.grid[y][x] = 1

    def set_goal(self, x, y):
        self.goal = (x, y)
        self.grid[y][x] = 2

    def get_neighbors(self, row, col):
        neighbors = super().get_neighbors(row, col)
        for x, y in neighbors:
            if self.grid[y][x] == 1:
                neighbors.remove((x, y))
        return neighbors
