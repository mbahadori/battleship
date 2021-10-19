import random
from Player import Player
class ComputerPlayer(Player):


    def __init__(self):
        super().__init__(self)
        self.shipKey = {
            "A": 5,
            "B": 4,
            "C": 3,
            "S": 3,
            "D": 2
        }

    # figures out if the ship is sunk
    # r : row of last shot
    # c : column of last shot
    # removes an available spot in the shipKey dictionary
    # returns True is ship is sunk, False if ship isnt sunk
    def isShipSunk(self, otherPlayer, r, c):
        ship = otherPlayer.gridShips.returnLocation(r, c)
        num = self.shipKey.get(ship)
        if ship in self.shipKey:
            self.shipKey.update({"ship": num-1})
            if num == 0:
                return True

    # ComputerPlayer randomly makes a shot,
    # Changes grid to have an M for miss and H for hit
    # says if player has won
    def takeTurn(self, otherPlayer):
        r = random.randint(0, 10)
        c = random.randint(0, 10)
        if otherPlayer.gridShips.isSpaceWater(r, c):  # if it is water
            self.gridShots.changeSingleSpace(r, c, "M")  # M = miss
        else:  # ship spot
            self.gridShots.changeSingleSpace(r, c, "H")  # H = hit
            if otherPlayer.isShipSunk():  # sunk a ship
                print(otherPlayer.gridShips[r][c] + " is sunk")
        self.gridShots.printGrid()
        if self.stillHasShips() == False:  # all ships are sunk
            print("You have sunk all ships, you win!")

    # Places the ships in valid places
    # fills the shipGrid
    def placeShip(self, ship, size):
        x = False
        count = 0
        rStart = 0
        cStart = 0
        while x == False:  # run through until points are valid
            rStart = random.randint(0, 10)
            cStart = random.randint(0, 10)
            direction = random.randint(0, 4)
            if self.gridShips.isSpaceWater(rStart, cStart):
                # 0 = down, 1 = up, 2 = right, 3 = left
                if direction == 0:  # down
                    if self.gridShips.isSpaceWater(rStart, (cStart+size)):
                        count += 1
                if direction == 1:  # up
                    if self.gridShips.isSpaceWater(rStart, (cStart-size)):
                        count += 1
                if direction == 2:  # right
                    if self.gridShips.isSpaceWater((rStart + size), cStart):
                        count += 1
                if direction == 3:  # left
                    if self.gridShips.isSpaceWater((rStart - size), cStart):
                        count += 1
                if count == 2: # both points are legal
                    x = True

        if direction == 0: # down
            self.gridShips.changeCol(cStart, ship, rStart, size)
        if direction == 1: # up
            self.gridShips.changeCol(cStart-size, ship, rStart, size) # end at rStart
        if direction == 2: # right
            self.gridShips.changeRow(cStart, ship, rStart, size)
        if direction == 3: # left
            self.gridShips.changeRow(cStart, ship, rStart-size, size) # end at cStart


    # this method will determine if the Player's ship grid still
    # has ships or not
    # If they have no ships left, the other player wins
    # This method returns true if they still have ships
    # This method returns false if they don't have ships
    def stillHasShips(self):
        for x in self.shipKey:  # traverse dictionary
            if self.shipKey[x] == 0:  # ship is sunk
                pass
            else:  # ship is not sunk - player hasn't won
                return True
        return False  # all ships are sunk













