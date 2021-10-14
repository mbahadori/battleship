from Player import Player

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
                  if self.gridShips.isSpaceWater(self, row, col) == False: #you cannot place the ship
                     break #recall the method
                  if x == size - 1 :
                     self.gridShips.changeRow(self, row, ship, column, size)
          elif "vertical" in direction:  #place vertically
          for x in range(size):
              column = column + 1
              if self.gridShips.isSpaceWater(self, row, col) == False: #you cannot place the ship - it is not water
                    self.placeShip(self, ship, size) #recall the method
              else: #you can place the ship (all areas are open)
                    self.gridShips.changeColumn(self, column, ship, row, size)





def takeTurn(self): #Taking your shots, returns True (if they can keep playing) or False(if they have won)
        inputA = int(input("Please enter a column number:"))
        inputB = int(input("Please enter a row number:"))
        stringDir= str(input("Please enter a direction:")) #hoz. or vertical
        inputShip = str(input("Please enter a ship:"))

        if "horizonal"in stringDir: #ship is placed horizonaly
            if isPlacementLegal(self, )

            #if inputShip in ShipKey:
                #self.changeRow(self,
                # else:#ship is placed vertically

        #changeRow and changeColumn


    #write takeTurn and still has ships

