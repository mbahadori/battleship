from Player import Player
import Random

class HumanPlayer(Player):
    def __init__(self):
        super().__init__(self)

  def placeShip(self, ship, size):
      #make sure legal inputs with loop
      while True:
          column = int(input("Please enter a column number:"))
          row = int(input("Please enter a row number:"))
          direction = str(input("Please enter a direction - horizontal or vertical:"))
          if "horizontal" in direction:  # place horizontally
              for x in range(size):
                  row = row + 1
                  if self.gridShips.isSpaceWater(self, row, column) == False: #you cannot place the ship
                     break #break out of for loop and since while True still runs, it will ask for new inputs
                  if x == size - 1:
                     self.gridShips.changeRow(self, row, ship, column, size)
          elif "vertical" in direction:  #place vertically
              for x in range(size):
                  column = column + 1
                  if self.gridShips.isSpaceWater(self, row, column) == False: #you cannot place the ship
                      break
                  if x == size - 1:
                      self.gridShips.changeColumn(self, column, ship, row, size)


  def takeTurn(self, otherPlayer): #Taking your shots - should I be using otherPlayer.gridShots? is that the right?
      column = int(input("Please enter a column number:"))
      row = int(input("Please enter a row number:"))
      if self.otherPlayer.gridShips.isSpaceWater(self, row, column) == False: #not water - you have hit a ship!
          self.gridShots.changeSingleSpace(self, row, column, "H")
          return "You got a hit!"
      else:  # you hit water
          return "You missed!"


  def isShipSunk(self, otherPlayer, row, column ):
      ShipKey = {
          "A": 5,
          "B": 4,
          "C": 3,
          "S": 3,
          "D": 2,
      }
      val = self.otherPlayer.gridShips[row][column]
      if val in ShipKey:
          ShipKey.update({"val": ShipKey[val] - 1}) #subtracts one from ShipKey
          if ShipKey[val] == 0:
               return True #in the other code - "This Ship has been Sunk and it is a", + val





def takeTurn(self): #Taking your shots, returns True (if they can keep playing) or False(if they have won)
        inputA = int(input("Please enter a column number:"))
        inputB = int(input("Please enter a row number:"))
        stringDir= str(input("Please enter a direction:")) #hoz. or vertical
        inputShip = str(input("Please enter a ship:"))

        if "horizonal"in stringDir: #ship is placed horizonaly
            if isPlacementLegal(self, )

            # this method will determine if the Player's ship grid still
            # has ships or not
            # If they have no ships left, the other player wins
            # This method returns true if they still have ships
            # This method returns false if they don't have ships
            def stillHasShips(self):
                if



