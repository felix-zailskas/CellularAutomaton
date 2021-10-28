from tkinter import *
from CellularAutomata.model.GridContainer.CellularAutomataModel import CellularAutomatonModel
from CellularAutomata.GUI.GridContainerCanvas import GridContainerCanvas
from CellularAutomata.util.rules.Rules import Rules
from CellularAutomata.util.initialization.GridInitializer import GridInitializer
from CellularAutomata.util.initialization.Presets import Presets

if __name__ == "__main__":
    master = Tk()

    #random.seed(0)

    rows = 100
    cols = 100
    resolution = 5
    frame_frequency = 1

    #TODO: make GUI class
    #TODO: Let user choose between all variations and connect all execution to the GUI
    ca = CellularAutomatonModel(rows, cols)
    ca.set_cells(cells=GridInitializer.initialize_random((ca.rows, ca.cols)))

    eca = CellularAutomatonModel(rows, cols, elementary=True)
    eca.set_cells(cells=GridInitializer.initialize_random_row((eca.rows, eca.cols), eca.rows - 1))

    canvas = GridContainerCanvas(master, ca, resolution)
    canvas.pack()
    i = 0
    while True:
        if i == 0 and not ca.is_stagnating:
            ca.print_generation()
            canvas.update()
            ca.update_cells(Rules.MAJORITY)
        i = (i + 1) % frame_frequency
        master.update()
