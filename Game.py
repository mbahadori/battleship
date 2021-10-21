from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer


# StillHasShips false --> game is over


H1 = HumanPlayer()
H1.createShipGrid()  #can i do this or do i need to all the placeShip method from Human Player 5x
H1.printGrids() #can comment this out later

#Step 3 - allow a human player to play against a computer player
  #Take turns and play until some player wins or loses
  #Each player has one turn - you do not go again if you miss or hit a ship

  #1. Create human player and computer player
  #2. Create ship grids for both players (use the self.createShip grid method)
  #3. Create a loop that constantly takes turn until one player loses or wins
      #call the stillhasShip method to determine W or L



