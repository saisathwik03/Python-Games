import random

class LudoGame:
    def __init__(self):
        self.board = [0] * 52  # Represents the Ludo board (0 to 51 positions)
        self.players = ["Player 1", "Player 2", "Player 3", "Player 4"]
        self.current_player = 0  # Index of the current player
        self.tokens = {"Player 1": [0, 0, 0, 0], "Player 2": [0, 0, 0, 0], "Player 3": [0, 0, 0, 0], "Player 4": [0, 0, 0, 0]}
        self.winner = None

    def roll_dice(self):
        return random.randint(1, 6)

    def move_token(self, player, token_index, steps):
        current_position = self.tokens[player][token_index]
        new_position = current_position + steps

        if current_position == 0 and steps == 6:
            self.tokens[player][token_index] = 1
        elif 1 <= current_position < 52:
            self.tokens[player][token_index] = new_position

    def is_valid_move(self, player, steps):
        for token_position in self.tokens[player]:
            if token_position == 0 and steps == 6:
                return True
            elif 1 <= token_position <= 51 and token_position + steps <= 52:
                return True
        return False

    def switch_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def check_winner(self):
        for player in self.players:
            if all(position == 52 for position in self.tokens[player]):
                self.winner = player

    def play(self):
        while not self.winner:
            player = self.players[self.current_player]
            input("Press Enter to roll the dice...")
            steps = self.roll_dice()
            print(f"{player} rolled a {steps}")

            if self.is_valid_move(player, steps):
                token_index = int(input("Enter the index of the token to move (0-3): "))
                self.move_token(player, token_index, steps)
                print(f"{player} moved token {token_index} {steps} steps.")

                self.check_winner()
                self.switch_player()
            else:
                print("Invalid move. Switching to the next player.")

        print(f"Congratulations! {self.winner} wins the game.")

if __name__ == "__main__":
    game = LudoGame()
    game.play()
