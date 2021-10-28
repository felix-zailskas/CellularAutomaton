import numpy as np
from CellularAutomata.util.filling.FloodFill import flood_fill


class RegionFiller:
    """
    Class to fill unreachable regions of a grid given starting points.
    """
    @staticmethod
    def fill_region(grid: [[int]], row: int, col: int, flood_c: [(int, int)] = None):
        """
        Fills a region of a grid with 1's. If the cells to flood are not given a flood
        filling algorithm will be used to determine the cells to flood.

        :param grid: Grid which should be filled
        :param row: Row of the starting point for the reachable cells
        :param col: Column of the starting point for the reachable cells
        :param flood_c: Cells that should be flooded
        :return: Flooded grid
        """
        flooded_cells = flood_fill(grid, row, col) if flood_c is None else flood_c
        result_cells = np.zeros((grid.shape[0], grid.shape[1]), dtype=int)
        for y in range(grid.shape[0]):
            for x in range(grid.shape[1]):
                if not (y, x) in flooded_cells:
                    result_cells[y][x] = 1
        return result_cells
