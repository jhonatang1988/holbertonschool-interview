#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on
an N×N chessboard
"""
import sys

combination_list = []


def position_Generator(n: int = 4):
    """
    generator to sent back a position [0, 0]
    :param n: number of queens
    :return: yields a position in the chess
    """
    return ([i, j] for i in range(0, n) for j in range(0, n))


def chess_positions(n: int = 4):
    """
    generator to sent back a position [0, 0]
    :param n: number of queens
    :return: yields a position in the chess
    """
    return [[[[i, j]] for i in range(0, n)] for j in range(0, n)]


def chess_permutations(lists, combination):
    if not lists:
        combination_list.append(combination)
        return
    first = lists[0]
    rest = lists[1:]
    for letter in first:
        chess_permutations(rest, combination + letter)


def horizontal_attack(combs, h_queens: int) -> bool:
    """
    attack the position horizontally and sends back a list of death
    :param combs:
    :param h_queens: number of queens
    :return: list of deaths
    """
    list_deaths = []

    for pos in combs:
        pos_gen = position_Generator(h_queens)
        while True:
            try:
                new_pos = next(pos_gen)
            except StopIteration:
                break
            if pos == new_pos:
                continue
            if pos[0] == new_pos[0]:
                list_deaths.append(new_pos)

    for pos in combs:
        if pos in list_deaths:
            return False
    return True


def vertical_attack(combs, v_queens: int) -> bool:
    """
    attack the position vertically and sends back a list of death
    :param combs:
    :param v_queens: number of queens
    :return: list of deaths
    """
    list_deaths = []
    for pos in combs:
        pos_gen = position_Generator(v_queens)
        while True:
            try:
                new_pos = next(pos_gen)
            except StopIteration:
                break
            if pos == new_pos:
                continue
            if pos[1] == new_pos[1]:
                list_deaths.append(new_pos)

    for pos in combs:
        if pos in list_deaths:
            return False
    return True


def diagonal_attack(combs, d_queens: int) -> bool:
    """
    attack the position diagonal and sends back a list of death
    :param combs:
    :param d_queens: number of queens
    :param pos: position to attack from with the queen
    :return: list of deaths
    """
    list_deaths = []
    for pos in combs:
        pos_gen = position_Generator(d_queens)
        while True:
            try:
                new_pos = next(pos_gen)
            except StopIteration:
                break
            if pos == new_pos:
                continue
            if pos[0] + pos[1] == new_pos[0] + new_pos[1]:
                list_deaths.append(new_pos)
            if pos[0] - new_pos[0] == pos[1] - new_pos[1]:
                list_deaths.append(new_pos)
    for pos in combs:
        if pos in list_deaths:
            return False
    return True


if __name__ == '__main__':
    try:
        n_queens = int(sys.argv[1])
        if not isinstance(n_queens, int):
            print('N must be a number')
            exit(1)
        if n_queens < 4:
            print('N must be at least 4')
            exit(1)
    except IndexError:
        print('Usage: nqueens N')
        exit(1)
    except ValueError:
        print('N must be a number')
        exit(1)

    chess_permutations(chess_positions(n_queens), [])
    winners = []
    for combination in combination_list:
        is_winner_horizontal = horizontal_attack(combination, n_queens)
        if is_winner_horizontal:
            is_winner_vertical = vertical_attack(combination, n_queens)
            if is_winner_vertical:
                is_winner_diagonal = diagonal_attack(combination, n_queens)
                if is_winner_diagonal:
                    winners.append(combination)

    for winner in winners:
        print(winner)
