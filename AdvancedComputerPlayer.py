import random
from Player import Player
class AdvancedComputerPlayer(Player):


    def __init__(self):
        super().__init__()
        self.shipKey = {
            "A": 5,
            "B": 4,
            "C": 3,
            "S": 3,
            "D": 2
        }
        self.lastHitR = 0
        self.lastHitC = 0
        self.gridOption()
        self.OddorEven = 0


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
            if num == 1: # all spots of the ship have been hit
                return True
        return False

    def findOptionSpots(self): #finding options to hit (every other board spot so you maximize hits)
        for i in range(10):
            for j in range(self.OddorEven, 10, 2): # 0-9 (when 0, columns = 0,2,4,6,8, when 1,columns = 1, 3, 5, 7, 9)
                gridOption.changeSingleSpace(i, j, "O")
            if self.OddorEven == 0: #hit (0,0), (0,2) (0,4) (0,6) then (0,8) next time you want to hit (1,1) (1,3), (1,5), (1,7), (1,9)
                self.OddorEven += 1
            else: #self.OddorEven = 1
                self.OddorEven -= 1

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
            for i in range(len(self.gridOption)): # traverse gridOption to see if theres an option
                for j in range(len(self.gridOption[j])): # traverse column
                    if self.gridOption[i][j] == "0": # if option spot is available
                        r = i
                        c = j
            for i in range(len(self.gridOption)): # traverse gridOption to see if theres an option
                for j in range(len(self.gridOption[j])): # traverse column
                    if self.gridOption[i][j] == "P": # if priority spot is available
                        r = i
                        c = j
            # priority loop is second to make sure that the ACP goes for P spots over O spots
            if otherPlayer.gridShips.isSpaceWater(r, c):  # if it is water
                self.gridShots.changeSingleSpace(r, c, "M")  # M = miss
                otherPlayer.gridShips.changeSingleSpace(r, c, "M")
                self.gridOption.changeSingleSpace(r, c, "M")
            else:  # ship is shot
                self.gridShots.changeSingleSpace(r, c, "H")  # H = hit
                self.lastHitR = r
                self.lastHitC = c
                self.hitShip(otherPlayer, self.lastHitR, self.lastHitC)

                if otherPlayer.isShipSunk(otherPlayer, r, c):  # sunk a ship
                    print(otherPlayer.gridShips.returnLocation(r, c) + " is sunk")
                otherPlayer.gridShips.changeSingleSpace(r, c, "H")
                self.gridOption.changeSingleSpace(r, c, "H")
            print(otherPlayer.shipKey)

    def hitShip(self, otherPlayer, r, c): # adds priority spots
        if self.gridOption.isSpaceWater(r+1, c): # open spot
            self.gridOption[r+1][c] = "P"
        if self.gridOption.isSpaceWater(r-1 , c): # open spot
            self.gridOption[r - 1][c] = "P"
        if self.gridOption.isSpaceWater(r, c+1): # open spot
            self.gridOption[r][c + 1] = "P"
        if self.gridOption.isSpaceWater(r, c-1): # open spot
            self.gridOption[r][c - 1] = "P"



    # Places the ships in valid places
    # fills the shipGrid
    # ship : type of ship
    # size : number of spots ship uses
    def placeShip(self, ship, size):
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
