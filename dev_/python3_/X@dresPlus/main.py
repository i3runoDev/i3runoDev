# Chess Game - www.101computing.net/chess
import turtle
from chess import *

board = [["bR","bN","bB","bQ","bK","bB","bN","bR"],
         ["bP","bP","bP","bP","bP","bP","bP","bP"],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["wP","wP","wP","wP","wP","wP","wP","wP"],
         ["wR","wN","wB","wQ","wK","wB","wN","wR"]]


drawChessboard() 
displayPieces(board)

challenge = input("Pick a challenge: enter a number between 1 and 5.")

if challenge=="1":
   board = [["  ","  ","  ","  ","  ","  ","bK","  "],
            ["bR","  ","  ","  ","  ","bP","bP","bP"],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","bB","  ","  ","  "],
            ["bP","  ","  ","  ","  ","  ","  ","  "],
            ["wP","  ","  ","  ","  ","  ","  ","wP"],
            ["  ","  ","  ","  ","  ","wP","wP","  "],
            ["  ","  ","  ","wR","  ","  ","wK","  "]]
   refreshBoard(board,0) 

   #Black's Turn
   board[1][0]="  "
   board[1][1]="bR"
   refreshBoard(board,2) #Update screen after 2 seconds
   
   #White's Turn - 1 move to win
   print("Update the code from line 38 to make a white move and win the game!")
   #...
   #...
   #...
   
elif challenge=="2":
   board = [["bR","  ","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","  ","bP","bP","bP"],
            ["  ","  ","bN","  ","  ","  ","  ","  "],
            ["  ","  ","  ","wQ","  ","  ","  ","  "],
            ["  ","  ","wB","  ","wP","  ","  ","wP"],
            ["  ","  ","  ","  ","  ","  ","wP","  "],
            ["wP","wB","  ","  ","  ","wP","  ","  "],
            ["wR","wN","  ","  ","wK","  ","wN","wR"]]   

   refreshBoard(board,0) 

   #Black's Turn
   board[0][6]="  "
   board[2][5]="bN"
   refreshBoard(board,2) #Update screen after 2 seconds
   
   #White's Turn - 1 move to win
   print("Update the code from line 61 to make a white move and win the game!")
   #...
   #...
   #...

elif challenge=="3":
   board = [["bR","bK","  ","bQ","  ","bB","  ","bR"],
            ["  ","bP","bP","bN","  ","bP","bP","bP"],
            ["bP","  ","bN","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","wN","  ","  ","wB","  "],
            ["  ","wQ","  ","  ","wP","  ","wP","  "],
            ["wP","wB","  ","  ","  ","wP","  ","wP"],
            ["wR","wN","  ","  ","wK","  ","wN","wR"]]   

   refreshBoard(board,0) 

   #Black's Turn
   board[1][3]="  "
   board[2][5]="bN"
   refreshBoard(board,2) #Update screen after 2 seconds
   
   #White's Turn - 1 move to win
   print("Update the code from line 84 to make a white move and win the game!")
   #...
   #...
   #...

elif challenge=="4":
   board = [["  ","  ","wB","  ","  ","bR","  ","bB"],
            ["  ","  ","  ","bQ","  ","wR","  ","  "],
            ["bP","  ","  ","  ","  ","  ","bP","  "],
            ["  ","bP","  ","  ","  ","  ","wP","  "],
            ["  ","wP","  ","wN","bP","  ","  ","  "],
            ["  ","  ","wP","  ","  ","wP","  ","bK"],
            ["wP","  ","  ","  ","  ","wB","  ","  "],
            ["wR","wN","  ","  ","  ","wK","  ","  "]]   

   refreshBoard(board,0) 

   #Black's Turn
   board[0][7]="  "
   board[4][3]="bB"
   refreshBoard(board,2) #Update screen after 2 seconds
   
   #White's Turn - 1 move to win
   print("Update the code from line 107 to make a white move and win the game!")
   #...
   #...
   #...   
   
elif challenge=="5":
   board = [["bR","  ","bQ","bR","  ","bB","  ","  "],
            ["  ","wR","  ","  ","  ","bN","bK","bP"],
            ["bN","  ","  ","  ","  ","  ","bP","wN"],
            ["bP","bP","  ","wP","bP ","  ","wQ","  "],
            ["bB","  ","  ","  ","wP","  ","  ","  "],
            ["  ","  ","  ","  ","wP","  ","wN","wP"],
            ["wP","wB","wB","wP","  ","  ","wP","  "],
            ["  ","  ","  ","  ","  ","wR","wK","  "]]   

   refreshBoard(board,0) 

   #Black's Turn
   board[2][0]="  "
   board[3][2]="bN"
   refreshBoard(board,2) #Update screen after 2 seconds
   
   #White's Turn - 1 move to win
   print("Update the code from line 130 to make a white move and win the game!")
   #...
   #...
   #...    