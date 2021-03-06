from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer

# StillHasShips false --> game is over

H1 = HumanPlayer() #check if this works
H1.createShipGrid()
H1.printGrids()


C1 = ComputerPlayer() #check if this works
C1.createShipGrid()
C1.printGrids()
#print this out

while H1.stillHasShips() == True or C1.stillHasShips() == True: #while player's ships are not sunk
    H1.printGrids()
    H1.takeTurn(C1)
    if H1.stillHasShips() == False: # H1 has no more ships -- C1 won
        print("Computer Player has won!")
    C1.printGrids()
    C1.takeTurn(H1)
    if C1.stillHasShips() == False: # C1 has no more ships -- H1 won
        print("Human Player has won!")

#H1.takeTurn(C1)
#C1.takeTurn(H1)
#if H1.stillHasShips() = false or C1.stillHasShips() = false - maybe seperate these statements but idea
#if H1.stillHasShips() = false: "Computer Player has won!

#Step 3 - allow a human player to play against a computer player
  #Take turns and play until some player wins or loses
  #Each player has one turn - you do not go again if you miss or hit a ship

  #1. Create human player and computer player
  #2. Create ship grids for both players (use the self.createShip grid method)
  #3. Create a loop that constantly takes turn until one player loses or wins
      #call the stillhasShip method to determine W or L



