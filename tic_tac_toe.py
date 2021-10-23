from typing import Any


class TicTacToe:
    def __init__(self):
        self.size: int = 3
        self.winner: int = 0
        self.who_now: str = 'player_1'
        self.board: list = [[' ', ' ', ' '],
                            [' ', ' ', ' '],
                            [' ', ' ', ' ']]
        self.c_player_1: list = []  # player_1's coordinates
        self.c_player_2: list = []  # players_2's coordinates
        self.added_coordinates: list = []
        self.win_v: list = []   # win_vertical
        self.win_h: list = []   # win_horizontally

    def instruction(self) -> None:
        print("Coordinates:")
        for i in range(self.size):
            print("  --- " * self.size)
            for j in range(self.size):
                print(f"| {i + 1},{j + 1} ", end="")
            print("|")
        print("  --- " * self.size)

    def draw(self) -> None:
        for i in range(self.size):
            print(" ---" * self.size)
            for j in range(self.size):
                print(f"| {self.board[i][j]} ", end="")
            print("|")
        print(" ---" * self.size)

    def coordinates_player_1(self) -> Any:
        self.c_player_1.clear()
        coordinates_player_1 = input("Enter coordinates for player 1: ")
        coordinates_player_1_strip = coordinates_player_1.strip()
        coordinates_player_1_split = coordinates_player_1_strip.split(",")
        for i in coordinates_player_1_split:
            self.c_player_1.append(i.strip())
            if (int(i) < 1 or int(i) > 3) or (i is str) or (len(coordinates_player_1_split) > 2):
                raise IndexError()
        if self.c_player_1 in self.added_coordinates:
            raise Exception("Please enter other coordinates!")

    def coordinates_player_2(self) -> Any:
        self.c_player_2.clear()
        coordinates_player_2 = input("Enter coordinates for player 2: ")
        coordinates_player_2_strip = coordinates_player_2.strip()
        coordinates_player_2_split = coordinates_player_2_strip.split(",")
        for i in coordinates_player_2_split:
            self.c_player_2.append(i.strip())
            if int(i) < 1 or int(i) > 3 or (i is str) or (len(coordinates_player_2_split) > 2):
                raise IndexError()
        if self.c_player_2 in self.added_coordinates:
            raise Exception("Please enter other coordinates!")

    def check_vertically(self) -> None:
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

    def check_horizontally(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[j][i] == 'X':
                    self.win_h.append(1)
                elif self.board[j][i] == 'O':
                    self.win_h.append(2)
                elif self.board[j][i] == ' ':
                    self.win_h.append(0)

                if len(self.win_h) == 3 and self.win_h[0] == 1 and self.win_h[1] == 1 and self.win_h[2] == 1:
                    print("Win player 1!")
                    self.winner = 1
                    break
                elif len(self.win_h) == 3 and self.win_h[0] == 2 and self.win_h[1] == 2 and self.win_h[2] == 2:
                    print("Win player 2!")
                    self.winner = 2
                    break
                elif len(self.win_h) == 3:
                    if (1 and 2 in self.win_h) or (0 in self.win_h):
                        self.win_h.clear()
            else:
                continue
            break

    def check_diagonal(self):
        if self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X':
            print("Win 1!")
            self.winner = 1
        elif self.board[0][2] == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X':
            print("Win 1!")
            self.winner = 1
        elif self.board[0][0] == 'O' and self.board[1][1] == 'O' and self.board[2][2] == 'O':
            print("Win 2!")
            self.winner = 2
        elif self.board[0][2] == 'O' and self.board[1][1] == 'O' and self.board[2][0] == 'O':
            print("Win 2!")
            self.winner = 2

    def game(self):
        self.instruction()
        while True:
            try:
                if self.who_now == 'player_1':
                    self.coordinates_player_1()
                    self.board[int(self.c_player_1[0]) - 1][int(self.c_player_1[1]) - 1] = 'X'
                    self.added_coordinates.append([self.c_player_1[0], self.c_player_1[1]])
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

                    if len(tic_tac_toe.added_coordinates) == 9:
                        print("Tie!")
                        break

                    self.who_now = 'player_2'

                elif self.who_now == 'player_2':
                    self.coordinates_player_2()
                    self.board[int(self.c_player_2[0]) - 1][int(self.c_player_2[1]) - 1] = 'O'
                    self.added_coordinates.append([self.c_player_2[0], self.c_player_2[1]])
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
                print(">>>>Please enter a integer coordinates number e.g. 1,1 !<<<<")
            except IndexError:
                print(f">>>>Range a board is {self.size}!<<<<")
                print(">>>>Min is a 1, max is a 3!<<<<")
                print(">>>>Allow coordinates: 1,1 ; 1,2 ; 1,3 ; 2,1 ; 2,2 ; 2,3 ; 3,1 ; 3,2 ; 3,3<<<<")
            except Exception as exception:
                print(f">>>>{exception}<<<<")


if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    tic_tac_toe.game()
