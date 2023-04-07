from dataclasses import dataclass, field
from typing import Any
from abc import ABC, abstractmethod


class Board(ABC):
    @abstractmethod
    def print(self):
        pass


class ErrorHandler(ABC):
    @abstractmethod
    def print_error(self):
        pass


class ValueErrorPrint(ErrorHandler):
    def print_error(self):
        print(">>>>Please enter the number of integer coordinates e.g. 1,1!<<<<")


@dataclass
class IndexErrorPrint(ErrorHandler):
    board_size: int = field()

    def print_error(self):
        print(f">>>>The board's range is {self.board_size}!<<<<")
        print(">>>>Min is 1, max is 3!<<<<")
        print(">>>>Allowed coordinates:\n 1,1 ; 1,2 ; 1,3 ;\n 2,1 ; 2,2 ; 2,3 ;\n 3,1 ; 3,2 ; 3,3 ;<<<<")


@dataclass
class OtherExceptionPrint(ErrorHandler):
    exception: Exception = field()

    def print_error(self):
        print(f">>>>{self.exception}<<<<")


@dataclass
class DrawBoard(Board):
    board_size: int = field()
    board: list[list[str]] = field(default_factory=list)

    def print(self):
        for i in range(self.board_size):
            print(" ---" * self.board_size)
            for j in range(self.board_size):
                print(f"| {self.board[i][j]} ", end="")
            print("|")
        print(" ---" * self.board_size)


@dataclass
class DrawInstruction(Board):
    coordinates: str = field(init=False)

    def print(self):
        self.coordinates = """
  ---   ---   ---  
| 1,1 | 1,2 | 1,3 |
  ---   ---   ---
| 2,1 | 2,2 | 2,3 |
  ---   ---   ---
| 3,1 | 3,2 | 3,3 |
  ---   ---   ---
"""
        print(f"Coordinates: {self.coordinates}")


@dataclass(slots=True)
class TicTacToe:
    BOARD_SIZE: int = field(init=False, default=3)
    winner: int = field(init=False)

    player_1_name: str = field(init=False)
    player_2_name: str = field(init=False)
    who_now: str = field(init=False)
    message_player_1_win: str = field(init=False)
    message_player_2_win: str = field(init=False)

    board: list[list[str]] = field(default_factory=list)
    player_1_coordinates: list = field(default_factory=list)
    player_2_coordinates: list = field(default_factory=list)
    added_coordinates: list = field(default_factory=list)
    win_vertical: list = field(default_factory=list)
    win_horizontally: list = field(default_factory=list)

    def __post_init__(self) -> None:
        self.winner = 0
        self.player_1_name = 'player_1'
        self.player_2_name = 'player_2'
        self.message_player_1_win = f"{self.player_1_name} win!"
        self.message_player_2_win = f"{self.player_2_name} win!"
        self.who_now = self.player_1_name
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]

    def coordinates_processing(self) -> Any:
        if self.who_now == self.player_1_name:
            self.player_1_coordinates.clear()
        elif self.who_now == self.player_2_name:
            self.player_2_coordinates.clear()

        coordinates = input(f"Enter coordinates for {self.who_now}: ").strip().split(",")

        for coordinate in coordinates:
            index_error_term: bool = (int(coordinate) < 1 or int(coordinate) > 3) or (coordinate is str) or (len(coordinates) > 2)
            if self.who_now == self.player_1_name:
                self.player_1_coordinates.append(coordinate)
                if index_error_term:
                    raise IndexError()
            elif self.who_now == self.player_2_name:
                self.player_2_coordinates.append(coordinate)
                if index_error_term:
                    raise IndexError()

        exception_message: str = "Please enter other coordinates!"
        if self.who_now == self.player_1_name and (self.player_1_coordinates in self.added_coordinates):
            raise Exception(exception_message)
        elif self.who_now == self.player_2_name and (self.player_2_coordinates in self.added_coordinates):
            raise Exception(exception_message)

    def check_vertically(self) -> None:
        for v_i in range(self.BOARD_SIZE):
            for v_j in range(self.BOARD_SIZE):
                if self.board[v_i][v_j] == 'X':
                    self.win_vertical.append(1)
                elif self.board[v_i][v_j] == 'O':
                    self.win_vertical.append(2)
                elif self.board[v_i][v_j] == ' ':
                    self.win_vertical.append(0)

                if len(self.win_vertical) == 3 and self.win_vertical[0] == 1 and self.win_vertical[1] == 1 and self.win_vertical[2] == 1:
                    print(self.message_player_1_win)
                    self.winner = 1
                    break
                elif len(self.win_vertical) == 3 and self.win_vertical[0] == 2 and self.win_vertical[1] == 2 and self.win_vertical[2] == 2:
                    print(self.message_player_2_win)
                    self.winner = 2
                    break
                elif len(self.win_vertical) == 3:
                    if (1 and 2 in self.win_vertical) or (0 in self.win_vertical):
                        self.win_vertical.clear()
            else:
                continue
            break

    def check_horizontally(self) -> None:
        for h_i in range(self.BOARD_SIZE):
            for h_j in range(self.BOARD_SIZE):
                if self.board[h_j][h_i] == 'X':
                    self.win_horizontally.append(1)
                elif self.board[h_j][h_i] == 'O':
                    self.win_horizontally.append(2)
                elif self.board[h_j][h_i] == ' ':
                    self.win_horizontally.append(0)

                if len(self.win_horizontally) == 3 and self.win_horizontally[0] == 1 and self.win_horizontally[1] == 1 and self.win_horizontally[2] == 1:
                    print(self.message_player_1_win)
                    self.winner = 1
                    break
                elif len(self.win_horizontally) == 3 and self.win_horizontally[0] == 2 and self.win_horizontally[1] == 2 and self.win_horizontally[2] == 2:
                    print(self.message_player_2_win)
                    self.winner = 2
                    break
                elif len(self.win_horizontally) == 3:
                    if (1 and 2 in self.win_horizontally) or (0 in self.win_horizontally):
                        self.win_horizontally.clear()
            else:
                continue
            break

    def _player_1_win_diagonal(self) -> None:
        print(self.message_player_1_win)
        self.winner = 1

    def _player_2_win_diagonal(self) -> None:
        print(self.message_player_2_win)
        self.winner = 2

    def check_diagonal(self) -> None:
        if self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X':
            self._player_1_win_diagonal()
        elif self.board[0][2] == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X':
            self._player_1_win_diagonal()
        elif self.board[0][0] == 'O' and self.board[1][1] == 'O' and self.board[2][2] == 'O':
            self._player_2_win_diagonal()
        elif self.board[0][2] == 'O' and self.board[1][1] == 'O' and self.board[2][0] == 'O':
            self._player_2_win_diagonal()

    def _coordinate_processing_for_player_1_or_player_2(self, player, x_or_o):
        self.board[int(player[0]) - 1][int(player[1]) - 1] = x_or_o
        self.added_coordinates.append([player[0], player[1]])
        player.clear()

    def _coordinate_processing_during_game(self) -> None:
        self.coordinates_processing()

        if self.who_now == self.player_1_name:
            self._coordinate_processing_for_player_1_or_player_2(self.player_1_coordinates, 'X')
        elif self.who_now == self.player_2_name:
            self._coordinate_processing_for_player_1_or_player_2(self.player_2_coordinates, 'O')

        board = DrawBoard(self.BOARD_SIZE, self.board)
        board.print()

    def game(self) -> None:
        DrawInstruction().print()

        while True:
            try:
                if self.who_now == self.player_1_name:
                    self._coordinate_processing_during_game()

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

                    self.who_now = self.player_2_name

                elif self.who_now == self.player_2_name:
                    self._coordinate_processing_during_game()

                    self.check_vertically()
                    if self.winner == 2:
                        break

                    self.check_horizontally()
                    if self.winner == 2:
                        break

                    self.check_diagonal()
                    if self.winner == 2:
                        break

                    self.who_now = self.player_1_name

                    print("=" * 40)

            except ValueError:
                ValueErrorPrint().print_error()
            except IndexError:
                IndexErrorPrint(self.BOARD_SIZE).print_error()
            except Exception as exception:
                OtherExceptionPrint(exception).print_error()


if __name__ == '__main__':
    tic_tac_toe: TicTacToe = TicTacToe()
    tic_tac_toe.game()
