import random as rnd
import math

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def makeMove(self):
        pass

    def checkForFinish(self, board):
        for row in board:
            if row[0] == row[1] and row[1] == row[2] and row[0] != ' ':
                return True
        
        for i in range(3):
            if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != ' ':
                return True
        
        if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' ':
            return True

        if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != ' ':
            return True

        return False 


class HumanPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)
    
    def makeMove(self, moves):

        while True:

            number = int(input("Please enter a number: "))
            
            try:
                move = [(number-1) // 3, (number-1) % 3]

                if move not in moves:
                    raise ValueError
                
                return move

            except ValueError:
                print('Invalid move!')
        

class ComputerPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)
    
    def makeMove(self, moves):
        while True:
            move = [rnd.randint(0,2), rnd.randint(0,2)]

            if move in moves:
                return move


class AIPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)
    
    def makeMove(self, moves, board):
        
        bestValue = math.inf
        bestMove = 0

        for move in moves:
            tempMoves = moves.copy()
            tempMoves.remove(move)
            board[move[0]][move[1]] = self.symbol

            value = self.minimax(board, tempMoves, True, 0)
            if value < bestValue:
                bestMove = move
                bestValue = value
            
            board[move[0]][move[1]] = ' '
        
        print('AI made move...')
        
        return bestMove


    def minimax(self, board, moves, isMaximizerPlayer, depth):

        result = self.checkForFinish(board)

        if result:
            if not isMaximizerPlayer:
                return 10 - depth
            else:
                return -10 + depth
        
        if not self.isMoveLeft(board):
            return 0

        if isMaximizerPlayer:
            bestValue = -math.inf

            for move in moves:
                board[move[0]][move[1]] = 'X' if self.symbol == 'O' else 'O'
                tempMoves = moves.copy()
                tempMoves.remove(move)

                value = self.minimax(board, tempMoves, False, depth+1)
                bestValue = max(bestValue, value)

                board[move[0]][move[1]] = ' '
            
            return bestValue

        else:
            bestValue = math.inf

            for move in moves:
                board[move[0]][move[1]] = self.symbol
                tempMoves = moves.copy()
                tempMoves.remove(move)

                value = self.minimax(board, tempMoves, True, depth+1)
                bestValue = min(bestValue, value)

                board[move[0]][move[1]] = ' '
            
            return bestValue


    def isMoveLeft(self, board):
        for row in board:
            for symbol in row:
                if symbol == ' ':
                    return True

        return False