import random
from Player import Player
class ComputerPlayer (Player):


    def __init__(self):
        self.location
        self.guess

    def takeTurn(self):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        changeRow(x)
        changeCol(y)

    def placeShip(self, ship, size):
        xStart = random.randint(0, 10)
        yStart = random.randint(0, 10)
        direction = random.randint(0, 4)
        # 0 = down, 1 = up, 2 = right, 3 = left
        if direction == 0 :
            if  (direction + size) < 10:
                # add ship
            else:
                direction = 1
        if direction == 1:
            if  (direction - size) > -1:
                #add ship
            else:
                direction = 0 # won't ever reach this
        if direction == 2:
            if (direciton + size) > 10:
                # add ship

