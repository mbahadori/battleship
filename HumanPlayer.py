from Player import Player
class HumanPlayer(Player):
  def __init__(self): #constructor - initializes the gridsShip, gridShots, and ShipKey attributes of the class
        super().__init__()
        self.shipKey = {
         "A": 5,
         "B": 4,
         "C": 3,
         "S": 3,
         "D": 2
        }
  def placeShip(self, ship, size): #This method uses human input to place ships
      ##self.printGrids()
      while True: #This loop keeps running until the user is able to place their ship
          row = int(input("Please enter a row number:"))
          column = int(input("Please enter a column number:"))
          direction = str(input("Please enter a direction - horizontal or vertical:"))
          if (direction != "horizontal" and direction != "vertical"):
              print ("Please enter new input")
              continue

          if "horizontal" in direction:  #if the user indicates they want to place the ship horizontally
              if row > 9 or row < 0 or column + size > 9 or column < 0:
                  print("Please enter new input")
                  continue
              canPlaceShip = True
              for x in range(size): #traverses through each spot the ship will take up determining if the ship can be placed or not
                  if self.gridShips.isSpaceWater(row, column) == False: #if the space is occupied - you cannot place the ship
                     canPlaceShip = False
                     print ("Please enter new input - this space is occupied")
                     break #break out of for loop and ask for new inputs
                  column = column + 1
              if canPlaceShip: #if you can place the ship
                 self.gridShips.changeRow(row, ship, column-size, size)
                 return

          elif "vertical" in direction: #if the user indicates they want to place the ship vertically
              if row + size > 9 or row < 0 or column > 9 or column < 0:
                  print("Please enter new input")
                  continue
              canPlaceShip = True
              for x in range(size): #traverses through each spot the ship will take up determining if the ship can be placed or not
                  if self.gridShips.isSpaceWater(row, column) == False: #the space is occupied- you cannot place the ship
                      canPlaceShip = False
                      print("Please enter new input - this space is occupied")
                      break #break out of loop and ask for new inputs
                  row = row + 1
              if canPlaceShip: #if you can place the ship
                  self.gridShips.changeCol(column, ship, row-size, size)
                  return

  def isShipSunk(self, otherPlayer, r, c):
        ship = otherPlayer.gridShips.returnLocation(r, c)
        num = self.shipKey.get(ship)
        if ship in self.shipKey: # ship in the game
            self.shipKey.update({ship: num-1})
            if num == 1: # all spots of the ship have been hit
                return True
        return False

  def takeTurn(self, otherPlayer):#this method determines if you hit your opponent's ship
      column = int(input("Please enter a column number:"))
      row = int(input("Please enter a row number:"))
      if otherPlayer.stillHasShips() == False:  # all ships are sunk
          print("You have sunk all ships, you win!")
      if otherPlayer.gridShips.isSpaceWater(row, column) == False: #not water - you have hit a ship!
          self.gridShots.changeSingleSpace(row, column, "H")
          if otherPlayer.isShipSunk(otherPlayer, row, column) == True: #if all spots of the opponent's ship have been sunk
               print(otherPlayer.gridShips.returnLocation(row, column) + " is sunk")
          else: #if you hit a spot on the opponent's ship but it has not sunk
               print("You got a hit!")
          otherPlayer.gridShips.changeSingleSpace(row, column, "H")
      else:#you hit water
        self.gridShots.changeSingleSpace(row, column, "M")
        otherPlayer.gridShips.changeSingleSpace(row, column, "M")
        print("You missed!")
      print(otherPlayer.shipKey)


  def stillHasShips(self): #this method determines if the Player's ship grid still has ships or not
      sum = 0
      for x in self.shipKey: #This loop sums up the numerical values of ShipKey
          sum = sum + self.shipKey.get(x)
      if sum == 0: #if all ships have been sunk, the other player wins
         return False
      else: #if there is still ships that have not been sunk
          return True

