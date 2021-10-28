from AdvancedComputerPlayer import AdvancedComputerPlayer
from ComputerPlayer import ComputerPlayer

# StillHasShips false --> game is over

A1 = AdvancedComputerPlayer() #check if this works
A1.createShipGrid()
A1.findOptionSpots()
A1.printGrids()


C1 = ComputerPlayer() #check if this works
C1.createShipGrid()
C1.printGrids()
#print this out

while A1.stillHasShips() == True or C1.stillHasShips() == True: #while player's ships are not sunk
    A1.printGrids()
    A1.takeTurn(C1)
    if A1.stillHasShips() == False: # H1 has no more ships -- C1 won
        print("Computer Player has won!")
        break
    C1.printGrids()
    C1.takeTurn(A1)
    if C1.stillHasShips() == False: # C1 has no more ships -- H1 won
        print("Advanced Computer Player has won!")
        break