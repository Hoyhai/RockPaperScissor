import random

class RockPaperScissors:
    def __init__(self):
        self.moves = ["rock", "paper", "scissors"]
        self.my_move = ""
        self.opponent_move = ""
        self.result = ""

    def play(self) -> None:
        print("Type your move: rock, paper, or scissors")
        self.my_move = input().lower()
        self.opponent_move = random.choice(self.moves)

        print(f"Opponent move is {self.opponent_move}")
        self.check_result()

    def check_result(self) -> None:
        if self.my_move == self.opponent_move:
            self.result = "draw"
        elif (
            (self.my_move == "rock" and self.opponent_move == "scissors") or
            (self.my_move == "paper" and self.opponent_move == "rock") or
            (self.my_move == "scissors" and self.opponent_move == "paper")
        ):
            self.result = "win"
        else:
            self.result = "lose"

        print(f"You {self.result}!")
        print()

    def play_again(self) -> bool:
        print("Do you want to play again? (yes/no)")
        play_again_input = input().lower()

        return play_again_input == "yes"

if __name__ == "__main__":
    game = RockPaperScissors()
    play_again = True

    while play_again:
        game.play()
        play_again = game.play_again()

    print("Thank you for playing!")
