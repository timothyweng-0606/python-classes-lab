class Game():
    def __init__(self,turn = 'X', tie = False, winner = None, 
    board ={
  'a1': None, 'b1': None, 'c1': None,
  'a2': None, 'b2': None, 'c2': None,
  'a3': None, 'b3': None, 'c3': None,
} ):
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = board

    def play_game(self):
        print('Welcome to the game')

    def print_board(self):
        b = self.board
        print(f"""
        A   B   C
    1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
        ----------
    2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
        ----------
    3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
  """)
        
    def print_message(self):
        if self.tie:
            print('Tie game!') 
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):  
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input("Enter a valid move (example: A1): ").lower()

            # Check if the move is valid
            if move in self.board and self.board[move] is None:
                self.board[move] = self.turn  # Update the board with the current player's move
                break  # Exit the loop as the input is valid
            else:
                print("Invalid move! Please try again.")

        # Optional: return the move if you need to use it outside the method
        return move

    def check_for_winner(self):
        b = self.board
        winning_combinations = [
            # Horizontal combinations
            ('a1', 'b1', 'c1'),
            ('a2', 'b2', 'c2'),
            ('a3', 'b3', 'c3'),
            # Vertical combinations
            ('a1', 'a2', 'a3'),
            ('b1', 'b2', 'b3'),
            ('c1', 'c2', 'c3'),
            # Diagonal combinations
            ('a1', 'b2', 'c3'),
            ('c1', 'b2', 'a3')
        ]

        for combo in winning_combinations:
            if b[combo[0]] and b[combo[0]] == b[combo[1]] == b[combo[2]]:
                self.winner = self.turn
                return True
        
        return False

    def check_for_tie(self):
        # Check if the board is full and there is no winner
        if all(value is not None for value in self.board.values()) and self.winner is None:
            self.tie = True
            return True
        return False


    def switch_turn(self):
        turn_lookup = {'X': 'O', 'O': 'X'}
        self.turn = turn_lookup[self.turn]

    def play_game(self):
        print("Shall we play a game?")
        while not self.winner and not self.tie:
            self.render()
            self.get_move()
            if self.check_for_winner():
                self.render()
                break
            if self.check_for_tie():
                self.render()
                break
            self.switch_turn()




game_instance = Game()
game_instance.play_game()
