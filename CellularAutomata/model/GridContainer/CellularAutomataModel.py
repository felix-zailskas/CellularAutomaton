from CellularAutomata.util.rules.Rules import Rules
from CellularAutomata.model.GridContainer.GridContainer import GridContainer
from CellularAutomata.util.rules.RuleApplication import RuleApplication
import numpy as np


class CellularAutomatonModel(GridContainer):
    """
    Extends the GridContainer class.
    Model representing a Cellular Automaton. A 2D numpy array is
    used to keep track of all current cells in the Automaton.
    Alive cells are coded as a 1, dead cells are coded as a 0.
    """
    def __init__(self, rows: int, cols: int, elementary: bool = False):
        """
        Initializes a Cellular Automaton.

        :param rows: Amount of rows
        :param cols: Amount of columns
        :param elementary: True if an elementary Automaton should be initialized
        """
        super().__init__(rows, cols)
        self.is_stagnating = False
        self.is_elementary = elementary
        self.generation = 0

    def print_generation(self):
        """
        Prints the current generation of the Automaton.

        :return:
        """
        print("Current Generation: ", self.generation)

    def update_cells(self, rule: Rules = Rules.GAME_OF_LIFE, rule_idx: int = 0, offset: (int, int) = (1, 0),
                     carry_over: bool = True):
        """
        Updates the cells of this automaton according to a given rule. If the cells did not change with the update,
        the automaton is set to be stagnating and prints the generation in which the final position has been reached.

        :param rule: Rule to apply
        :param rule_idx: Index of elementary rule to apply
        :param offset: Offset for the OFFSET rule
        :param carry_over: True if elements should wrap around the edges of the grid
        :return: None
        """
        new_cells = RuleApplication.apply_rule(self, rule, rule_idx=rule_idx, offset=offset, carry_over=carry_over)
        if self.check_stagnating(new_cells):
            self.is_stagnating = True
            print(f"Final Position reached after {self.generation} generations.")
        else:
            self.is_stagnating = False
            self.grid = np.array(new_cells, dtype=int)
            self.generation += 1

    def copy(self):
        """
        Returns a copy of this automaton.

        :return: Copy of self
        """
        copy = CellularAutomatonModel(self.rows, self.cols, elementary=self.is_elementary)
        copy.set_cells(self.grid)
        return copy

    def become_stagnant(self, rule: Rules):
        """
        Applies a rule to the automaton until it is stagnating.

        :param rule: Rule to apply
        :return: None
        """
        while not self.is_stagnating:
            self.update_cells(rule)

    def check_stagnating(self, new_cells: [[int]]):
        """
        Checks if the automaton is stagnating given the new cells it would update to.

        :param new_cells: Cells that the automaton would have in the next generation
        :return: True if no change happened between the current and the given cells, False otherwise
        """
        if self.is_elementary:
            return np.array_equal(self.grid[self.rows - 1], new_cells[self.rows - 1])
        return np.array_equal(self.grid, new_cells)

    def get_live_neighbors(self, center_row: int, center_col: int):
        """
        Calculates the amount of alive neighbors around a given position in the grid. The following cells are
        considered: (x-1, y-1), (x-1, y), (x-1, y+1), (x+1, y-1), (x+1, y), (x+1, y+1), (x, y-1), (x, y+1)
        Cells outside of the scope of the grid of this automaton are considered dead.

        :param center_row: Row of the cell to check
        :param center_col: Column of the cell to check
        :return: Amount of neighbors alive
        """
        row_neg_off = -1 + (center_row == 0)
        row_pos_off = 1 + (center_row != self.rows - 1)
        col_neg_off = -1 + (center_col == 0)
        col_pos_off = 1 + (center_col != self.cols - 1)
        return np.sum(self.grid[center_row + row_neg_off:center_row + row_pos_off,
                      center_col + col_neg_off:center_col + col_pos_off]) - self.grid[center_row, center_col]

    def get_row_neighbors(self, center_row: int, center_col: int):
        """
        Returns a bit pattern of the two direct neighbors in the same row as a given cell. The following neighbors are
        considered: (x-1, y), (x, y), (x+1, y)
        An arrangement like: (alive, alive, dead) would result in the pattern 110
        Cells outside of the scope of the grid of this automaton are considered dead.

        :param center_row: Row of the cell to check
        :param center_col: Column of the cell to check
        :return: Bit pattern of the row neighbors
        """
        pattern = ''
        for j in range(-1, 2):
            if center_col + j < 0 or center_col + j >= self.cols:
                pattern += '0'
                continue
            pattern += str(int(self.grid[center_row][center_col + j]))
        return pattern
