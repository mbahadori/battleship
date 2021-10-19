from Player import Player
from Grid import Grid
from HumanPlayer import HumanPlayer

g1 = Grid()
H1 = HumanPlayer()


H1.placeShip("A", 5)
H1.printGrids()

H1.placeShip("B", 4)
H1.printGrids()

H1.placeShip("C", 3)
H1.printGrids()

H1.placeShip("S", 3)
H1.printGrids()

H1.placeShip("D", 2)
H1.printGrids()

H1.printGrids()


