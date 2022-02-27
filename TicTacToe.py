from Player import *
import random as rnd

class TicTacToe:
    def __init__(self, playerType):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        self.player1 = HumanPlayer('X') if rnd.randint(0, 1) else HumanPlayer('O')
        symbol = 'X' if self.player1.symbol == 'O' else 'O'
        
        if playerType == 1:
            self.player2 = ComputerPlayer(symbol)
        elif playerType == 2:
            self.player2 = AIPlayer(symbol)
        else:
            self.player2 = HumanPlayer(symbol)


    def draw(self):
        print("-------------")
        
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')
            print("-------------")
        
    
    def isMoveLeft(self):
        for row in self.board:
            for symbol in row:
                if symbol == " ":
                    return True

        return False

    def play(self):
        turn = rnd.randint(0, 1)

        print("-------------")
        
        for i in range(1, 9, 3):
            print('| ' + ' | '.join([str(i), str(i+1), str(i+2)]) + ' |')
            print("-------------")
        print('================================')

        while True:

            moves = self.getAvaliableMoves()

            if turn:
                print("Player 1's turn:")

                move = self.player1.makeMove(moves)
                self.board[move[0]][move[1]] = self.player1.symbol
                
                result = self.player1.checkForFinish(self.board)

                if result:
                    self.draw()
                    print('\Player 1 won the game!')
                    break

            else:
                print("Player 2's turn:")
                
                move = self.player2.makeMove(moves, self.board) if isinstance(self.player2, AIPlayer) else self.player2.makeMove(moves)
                self.board[move[0]][move[1]] = self.player2.symbol

                result = self.player2.checkForFinish(self.board)

                if result:
                    self.draw()
                    print('\Player 2 won the game!')
                    break
            
            self.draw()
            print('================================')

            turn = (turn+1) % 2

            if not self.isMoveLeft():
                print('\nIt is a Tie...')
                break
            
    def getAvaliableMoves(self):
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append([i,j])
        
        return moves


if __name__ == '__main__':

    print('Please select which type of opponent do you want?')
    print('1 - Computer Player\n2 - Smart Computer Player\n3 - Two player Mode\n')

    choice = input('>>>> ')

    if choice == '1':
        game = TicTacToe(1)
    elif choice == '2':
        game = TicTacToe(2)
    else:
        game = TicTacToe(3)

    game.play()