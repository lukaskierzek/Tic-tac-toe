from typing import Any


class TicTacToe:
    def __init__(self) -> None:
        self.size: int = 3  # Board's size
        self.winner: int = 0  # Winner's number. When Player 1 is the winner, then 'self.winner = 1'

        self.who_now: str = 'player_1'  # Whose turn is it now

        self.board: list[list[str]] = [[' ', ' ', ' '],
                                       [' ', ' ', ' '],
                                       [' ', ' ', ' ']]  # Game broad
        self.c_player_1: list[str] = []  # Player 1's coordinates
        self.c_player_2: list[str] = []  # Player 2's coordinates
        self.add_coordinates: list[str] = []  # Coordinates given during the game

        self.win_v: list[int] = []  # List of numbers when checking vertically. See function 'check_vertically'
        self.win_h: list[int] = []  # List of numbers when checking horizontally. See function 'check_horizontally'

    def instruction(self) -> None:
        """Drawing the broad game with possible coordinates to enter:"""
        print("Coordinates:")
        for i in range(self.size):
            print("  --- " * self.size)
            for j in range(self.size):
                print(f"| {i + 1},{j + 1} ", end="")
            print("|")
        print("  --- " * self.size)

    def draw(self) -> None:
        """Drawing the broad game with entered 'X' or 'O'"""
        for i in range(self.size):
            print(" ---" * self.size)
            for j in range(self.size):
                print(f"| {self.board[i][j]} ", end="")
            print("|")
        print(" ---" * self.size)

    def coordinates_player_1(self) -> Any:
        """Player 1 enters the coordinates that are process"""
        self.c_player_1.clear()

        coordinates_player_1: str = input("[Player 1] Enter the coordinates: ")
        coordinates_player_1_strip: str = coordinates_player_1.strip()
        coordinates_player_1_split: list[str] = coordinates_player_1_strip.split(",")

        for i in coordinates_player_1_split:
            self.c_player_1.append(i.strip())
            if (int(i) < 1 or int(i) > 3) or (i is str) or (len(coordinates_player_1_split) > 2):
                raise IndexError()

        if self.c_player_1 in self.add_coordinates:
            raise Exception("Please enter other coordinates!")

    def coordinates_player_2(self) -> Any:
        """Player 2 enters the coordinates that are process"""
        self.c_player_2.clear()

        coordinates_player_2: str = input("[Player 2] Enter the coordinates: : ")
        coordinates_player_2_strip: str = coordinates_player_2.strip()
        coordinates_player_2_split: list[str] = coordinates_player_2_strip.split(",")

        for i in coordinates_player_2_split:
            self.c_player_2.append(i.strip())
            if int(i) < 1 or int(i) > 3 or (i is str) or (len(coordinates_player_2_split) > 2):
                raise IndexError()

        if self.c_player_2 in self.add_coordinates:
            raise Exception("Please enter other coordinates!")

    def check_vertically(self) -> None:
        """Check vertically if Player 1 or Player 2 is winning"""
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 'X':
                    self.win_v.append(1)
                elif self.board[i][j] == 'O':
                    self.win_v.append(2)
                elif self.board[i][j] == ' ':
                    self.win_v.append(0)

                if len(self.win_v) == 3 and self.win_v[0] == 1 and self.win_v[1] == 1 and self.win_v[2] == 1:
                    print("Win player 1!")
                    self.winner = 1
                    break
                elif len(self.win_v) == 3 and self.win_v[0] == 2 and self.win_v[1] == 2 and self.win_v[2] == 2:
                    print("Win player 2!")
                    self.winner = 2
                    break
                elif len(self.win_v) == 3:
                    if (1 and 2 in self.win_v) or (0 in self.win_v):
                        self.win_v.clear()
            else:
                continue
            break

    def check_horizontally(self) -> None:
        """Check horizontally if Player 1 or Player 2 is winning"""
        for j in range(self.size):
            for k in range(self.size):
                if self.board[k][j] == 'X':
                    self.win_h.append(1)
                elif self.board[k][j] == 'O':
                    self.win_h.append(2)
                elif self.board[k][j] == ' ':
                    self.win_h.append(0)

                if len(self.win_h) == 3 and self.win_h[0] == 1 and self.win_h[1] == 1 and self.win_h[2] == 1:
                    print("Player 1 is the winner!")
                    self.winner = 1
                    break
                elif len(self.win_h) == 3 and self.win_h[0] == 2 and self.win_h[1] == 2 and self.win_h[2] == 2:
                    print("Player 2 is the winner!")
                    self.winner = 2
                    break
                elif len(self.win_h) == 3:
                    if (1 and 2 in self.win_h) or (0 in self.win_h):
                        self.win_h.clear()
            else:
                continue
            break

    def check_diagonal(self) -> None:
        """Check diagonal if Player 1 or Player 2 is winning"""
        if self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X':
            print("Player 1 is the winner!")
            self.winner = 1
        elif self.board[0][2] == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X':
            print("Player 1 is the winner!")
            self.winner = 1
        elif self.board[0][0] == 'O' and self.board[1][1] == 'O' and self.board[2][2] == 'O':
            print("Player 2 is the winner!")
            self.winner = 2
        elif self.board[0][2] == 'O' and self.board[1][1] == 'O' and self.board[2][0] == 'O':
            print("Player 2 is the winner!")
            self.winner = 2

    def game(self) -> None:
        """Main function with the code game"""
        self.instruction()
        while True:
            try:
                if self.who_now == 'player_1':
                    self.coordinates_player_1()

                    # Assign the letter 'X' to the board according to player_1's coordinates
                    self.board[int(self.c_player_1[0]) - 1][int(self.c_player_1[1]) - 1] = 'X'

                    # Add player_1's coordinates to 'add_coordinates' variable
                    self.add_coordinates.append([self.c_player_1[0], self.c_player_1[1]])

                    self.c_player_1.clear()
                    self.draw()

                    self.check_vertically()
                    if self.winner == 1:
                        break

                    self.check_horizontally()
                    if self.winner == 1:
                        break

                    self.check_diagonal()
                    if self.winner == 1:
                        break

                    if len(tic_tac_toe.add_coordinates) == 9:
                        print("Tie!")
                        break

                    self.who_now = 'player_2'

                elif self.who_now == 'player_2':
                    self.coordinates_player_2()

                    # Assign the letter 'X' to the board according to player_2's coordinates
                    self.board[int(self.c_player_2[0]) - 1][int(self.c_player_2[1]) - 1] = 'O'

                    # Add player_2's coordinates to 'add_coordinates' variable
                    self.add_coordinates.append([self.c_player_2[0], self.c_player_2[1]])

                    self.c_player_2.clear()
                    self.draw()

                    self.check_vertically()
                    if self.winner == 2:
                        break

                    self.check_horizontally()
                    if self.winner == 2:
                        break

                    self.check_diagonal()
                    if self.winner == 2:
                        break

                    self.who_now = 'player_1'

                    print("=" * 40)

            except ValueError:
                print(">>>>Enter the number of integer coordinates e.g. 1,1 !<<<<")
            except IndexError:
                print(f">>>>The board's range is {self.size}!<<<<")
                print(">>>>The minimum value is 1, the maximum is 3!<<<<")
                print(">>>>Allowed coordinates: 1,1 ; 1,2 ; 1,3 ; 2,1 ; 2,2 ; 2,3 ; 3,1 ; 3,2 ; 3,3<<<<")
            except Exception as exception:
                print(f">>>>{exception}<<<<")


def main() -> None:
    tic_tac_toe = TicTacToe()
    tic_tac_toe.game()


if __name__ == '__main__':
    main()
