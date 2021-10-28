from CellularAutomata.util.filling.RegionFiller import RegionFiller
from CellularAutomata.model.GridContainer.CellularAutomataModel import CellularAutomatonModel
from CellularAutomata.GUI.GridContainerCanvas import GridContainerCanvas
from CellularAutomata.util.initialization.GridInitializer import GridInitializer
from CellularAutomata.util.rules.Rules import Rules
from tkinter import *


master = Tk()
rows = 100
cols = 100
resolution = 5

# initializing the CA
filled_ca = CellularAutomatonModel(rows, cols)
filled_ca.set_cells(GridInitializer.initialize_random(filled_ca))
# Fill CA with Majority rule as estimate of the map
filled_ca.become_stagnant(Rules.MAJORITY)
majority_ca = filled_ca.copy()
# Fill all unreachable spots
filled_ca.set_cells(RegionFiller.fill_region(filled_ca.cells, 0, 0))

c1 = GridContainerCanvas(master, filled_ca.rows, filled_ca.cols, filled_ca.cells, resolution)
c2 = GridContainerCanvas(master, majority_ca.rows, majority_ca.cols, majority_ca.grid, resolution)

c1.pack(side="left", fill="both", expand=True)
c2.pack(side="right", fill="both", expand=True)
c1.update(filled_ca.cells)
c2.update(majority_ca.grid)
mainloop()
