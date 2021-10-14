import random
from Player import Player
class ComputerPlayer (Player):


    def __init__(self):
        super().__init__(self)

    def takeTurn(self, otherPlayer):
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        if self.otherPlayer.gridShips.isSpaceWater(x, y):  # if it is water
            self.gridShots.changeSingleSpace(x, y, "M")  # M = miss
        else:
            self.gridShots.changeSingleSpace(x, y, "H")  # H = hit
            if self.otherPlayer.gridShips.isSpaceWater(x, y) and self.otherPlayer:  # sunk a ship
            print("you hit a ship!")
        self.gridShots.printGrid()

    def placeShip(self, ship, size):
        x = False
        count = 0
        xStart = 0
        yStart = 0
        while x == False:
            xStart = random.randint(0, 10)
            yStart = random.randint(0, 10)
            direction = random.randint(0, 4)
            if self.gridShips.isSpaceWater(xStart, yStart):
                # 0 = down, 1 = up, 2 = right, 3 = left
                if direction == 0: # down
                    if self.gridShips.isSpaceWater(xStart, (yStart+size)):
                        count += 1
                if direction == 1: # up
                    if self.gridShips.isSpaceWater(xStart, (yStart-size)):
                        count += 1
                if direction == 2: # right
                    if self.gridShips.isSpaceWater((xStart + size), yStart):
                        count += 1
                if direction == 3: # left
                    if self.gridShips.isSpaceWater((xStart - size), yStart):
                        count += 1
                if count == 2: # both points are legal
                    x = True

        if direction == 0: # down
            self.gridShips.changeCol(yStart, ship, xStart, size)
        if direction == 1: # up
            self.gridShips.changeCol(yStart-size, ship, xStart, size) # end at yStart
        if direction == 2: # right
            self.gridShips.changeRow(xStart, ship, yStart, size)
        if direction == 3: # left
            self.gridShips.changeRow(xStart-size, ship, yStart, size) # end at xStart


    # this method will determine if the Player's ship grid still
    # has ships or not
    # If they have no ships left, the other player wins
    # This method returns true if they still have ships
    # This method returns false if they don't have ships
    def stillHasShips(self):
        hitCount = 0








