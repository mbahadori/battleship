import random
from Player import Player

class HumanPlayer(Player):
    def __init__(self):
        super().__init__(self)
        self.ShipKey = {
         "A": 5,
         "B": 4,
         "C": 3,
         "S": 3,
         "D": 2
        }

  def placeShip(self, ship, size):
      #make sure legal inputs with loop
      while True:
          column = int(input("Please enter a column number:"))
          row = int(input("Please enter a row number:"))
          direction = str(input("Please enter a direction - horizontal or vertical:"))
          if "horizontal" in direction:  # place horizontally
              for x in range(size):
                  row = row + 1
                  if self.gridShips.isSpaceWater(row, column) == False: #you cannot place the ship
                     break #break out of for loop and since while True still runs, it will ask for new inputs
                  if x == size - 1:
                     self.gridShips.changeRow(row, ship, column, size)
          elif "vertical" in direction:  #place vertically
              for x in range(size):
                  column = column + 1
                  if self.gridShips.isSpaceWater(row, column) == False: #you cannot place the ship
                      break
                  if x == size - 1:
                      self.gridShips.changeCol(column, ship, row, size)

  def isShipSunk(self, otherPlayer, row, column ):
      val = otherPlayer.gridShips[row][column]
      if val in self.ShipKey:
          self.ShipKey.update({"val": self.ShipKey[val] - 1}) #subtracts one from ShipKey
          if self.ShipKey[val] == 0:
              return True
          else: #the ship has not been sunk yet
              return False

  def takeTurn(self, otherPlayer): #Taking your shots - should I be using otherPlayer.gridShots? is that the right?
      column = int(input("Please enter a column number:"))
      row = int(input("Please enter a row number:"))
      if otherPlayer.gridShips.isSpaceWater(row, column) == False: #not water - you have hit a ship!
          self.gridShots.changeSingleSpace(row, column, "H")
          return "You got a hit!"
      elif self.isShipSunk(otherPlayer, row, column) == True: #if all spots of ship has been sunk
          return "The ship has been sunk"
      else:#you hit water
          return "You missed!"


 # this method will determine if the Player's ship grid still has ships or not
    # If they have no ships left, the other player wins
    # This method returns true if they still have ships
     # This method returns false if they don't have ships
  def stillHasShips(self):
      sum = 0
      for x in self.ShipKey.keys():
          sum = sum + (x, self.ShipKey[x])
      if sum == 0: #there is no ships left
         return False
      else: #if they still have ships
          return True


