import random
from Player import Player
class ComputerPlayer(Player):


    def __init__(self):
        super().__init__()
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
        if ship in self.shipKey: # ship in the game
            self.shipKey.update({ship: num-1})
            if num == 0: # all spots of the ship have been hit
                return True


    # ComputerPlayer randomly makes a shot,
    # Changes grid to have an M for miss and H for hit
    # says if player has won
    def takeTurn(self, otherPlayer):
        self.printGrids()
        if self.stillHasShips() == False:  # all ships are sunk
            print("You have sunk all ships, you win!")
        else:
            r = random.randint(0, 9)
            c = random.randint(0, 9)
            if otherPlayer.gridShips.isSpaceWater(r, c):  # if it is water
                self.gridShots.changeSingleSpace(r, c, "M")  # M = miss
                #self.printGrids()
            else:  # ship is shot
                self.gridShots.changeSingleSpace(r, c, "H")  # H = hit
                #self.printGrids()
                if otherPlayer.isShipSunk(otherPlayer, r, c):  # sunk a ship
                    print(otherPlayer.gridShips.returnLocation(r, c) + " is sunk")


    # Places the ships in valid places
    # fills the shipGrid
    # ship : type of ship
    # size : number of spots ship uses
    def placeShip(self, ship, size):
        self.printGrids()
        x = False
        count = 0
        rStart = 0
        cStart = 0
        while x == False:  # run through until points are valid
            rStart = random.randint(0, 9)
            cStart = random.randint(0, 9)
            direction = random.randint(0, 1)
            count = 0
            if self.gridShips.isSpaceWater(rStart, cStart):
                # 0 = down, 1 = up, 2 = right, 3 = left
                for y in range(size): # checks if all spots are valid
                    if direction == 0:  # down
                        if (rStart + size) <= 10 and self.gridShips.isSpaceWater(rStart+y, cStart):
                            count += 1
                    if direction == 1:  # right
                        if (cStart+size) <= 10 and self.gridShips.isSpaceWater(rStart , cStart+y):
                            count += 1
                if count == size:  # both points are legal
                    x = True

        if direction == 0: # down
            self.gridShips.changeCol(cStart, ship, rStart, size)
        if direction == 1: # right
            self.gridShips.changeRow(rStart, ship, cStart, size)



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













