from Player import Player
class HumanPlayer(Player):
    def __init__(self): #constructor - initializes the gridsShip, gridShots, and ShipKey attributes of the class
        super().__init__(self)
        self.ShipKey = {
         "A": 5,
         "B": 4,
         "C": 3,
         "S": 3,
         "D": 2
        }

  def placeShip(self, ship, size): #This method uses human input to place ships
      while True: #This loop keeps running until the user is able to place their ship
          column = int(input("Please enter a column number:"))
          row = int(input("Please enter a row number:"))
          direction = str(input("Please enter a direction - horizontal or vertical:"))
          if "horizontal" in direction:  #if the user's input indicates they want to place the ship horizontally
              for x in range(size): #traverses through each spot the ship will take up determining if the ship can be placed or not
                  row = row + 1
                  if self.gridShips.isSpaceWater(row, column) == False: #if the space is not water - you cannot place the ship
                     break #break out of for loop and ask for new inputs
                  if x == size - 1: #if you can place the ship in each spot it will take up - you can place your ship.
                     self.gridShips.changeRow(row, ship, column, size)
          elif "vertical" in direction: #if the user's input indicates they want to place the ship vertically
              for x in range(size): #traverses through each spot the ship will take up determining if the ship can be placed or not
                  column = column + 1
                  if self.gridShips.isSpaceWater(row, column) == False: #the space is not water - you cannot place the ship
                      break #break out of loop and ask for new inputs
                  if x == size - 1: #if you can place the ship in each spot it will take up - you can place your ship.
                      self.gridShips.changeCol(column, ship, row, size)

  def isShipSunk(self, otherPlayer, row, column ):#this method determines if the other player's ship has been sunk or not
      val = otherPlayer.gridShips[row][column]
      if val in self.ShipKey: #if this value corresponds to a battleship,
          self.ShipKey.update({"val": self.ShipKey[val] - 1}) #subtracts one from ShipKey
          if self.ShipKey[val] == 0: #if all of the ship's "indexes" have been sunk
              return True
          else: #the ship has not been sunk yet
              return False

  def takeTurn(self, otherPlayer):#this method determines if you hit your opponent's ship
      column = int(input("Please enter a column number:"))
      row = int(input("Please enter a row number:"))
      if otherPlayer.gridShips.isSpaceWater(row, column) == False: #not water - you have hit a ship!
          self.gridShots.changeSingleSpace(row, column, "H")
          if self.isShipSunk(otherPlayer, row, column) == True: #if all spots of the opponent's ship have been sunk
              return "You got a hit and the ship has been sunk!"
          else: #if you hit a spot on the opponent's ship but it has not sunk
              return "You got a hit!"
      else:#you hit water
        return "You missed!"


  def stillHasShips(self): #this method determines if the Player's ship grid still has ships or not
      sum = 0
      for x in self.ShipKey.keys(): #This loop sums up the int values of ShipKey
          sum = sum + (x, self.ShipKey[x])
      if sum == 0: #if all ships have been sunk, the other player wins
         return False
      else: #if there is still ships that have not been sunk
          return True


