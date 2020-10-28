#!/usr/bin/env python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on
an N×N chessboard
"""
from typing import List, Generator


def position_Generator(n: int = 4) -> Generator[List[int], None, None]:
    """
    generator to sent back a position [0, 0]
    :param n: number of queens
    :return: yields a position in the chess
    """
    return ([i, j] for i in range(0, n) for j in range(0, n))


def horizontal_attack(pos: List[int], h_queens: int) -> List[List[int]]:
    """
    attack the position horizontally and sends back a list of death
    :param h_queens: number of queens
    :param pos: position to attack from with the queen
    :return: list of deaths
    """
    list_deaths = []
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
    return list_deaths


def vertical_attack(pos: List[int], v_queens: int) -> List[List[int]]:
    """
    attack the position vertically and sends back a list of death
    :param v_queens: number of queens
    :param pos: position to attack from with the queen
    :return: list of deaths
    """
    list_deaths = []
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
    return list_deaths


def diagonal_attack(pos: List[int], d_queens: int) -> List[List[int]]:
    """
    attack the position diagonal and sends back a list of death
    :param d_queens: number of queens
    :param pos: position to attack from with the queen
    :return: list of deaths
    """
    list_deaths = []
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
    return list_deaths


def has_horse_distance(pos: List[int], temp_queens: List[List[int]],
                       queens: int) \
        -> bool:
    """
    check if current sqaure if a horse movement distance from last queen
    :param queens: number of queen to accommodate
    :param pos: current position
    :param temp_queens: previous queen position
    :return: false if not a distance of horse else true
    """
    pre_queen = temp_queens[-1]
    if pre_queen[1] == queens - 3 and pos[1] != queens - 1:
        return False

    for queen in temp_queens:

        if pos == queen:
            return True
        if pos[0] - 1 == queen[0] and pos[1] - 2 == queen[1]:
            return True
        elif pos[0] - 2 == queen[0] and pos[1] - 1 == queen[1]:
            return True
        elif pos[0] - 2 == queen[0] and pos[1] + 1 == queen[1]:
            return True
        elif pos[0] - 1 == queen[0] and pos[1] + 2 == queen[1]:
            return True
        elif pos[0] + 1 == queen[0] and pos[1] + 2 == queen[1]:
            return True
        elif pos[0] + 2 == queen[0] and pos[1] + 1 == queen[1]:
            return True
        elif pos[0] + 2 == queen[0] and pos[1] - 1 == queen[1]:
            return True
        elif pos[0] + 1 == queen[0] and pos[1] - 2 == queen[1]:
            return True
    return False




if __name__ == '__main__':
    queens = 6

    for chance in range(0, queens * queens):
        queen_positions = []
        it = position_Generator(queens)
        list_death = []
        if chance == 0:
            pass
        else:
            for k in range(0, chance):
                try:
                    next(it)
                except StopIteration:
                    break

        while True:
            try:
                square = next(it)
            except StopIteration:
                break

            if not queen_positions:
                queen_positions.append(square)
            print(queen_positions)

            if is_horse_distance(square, queen_positions, queens):

                if square not in list_death:
                    for dead in horizontal_attack(square, queens):
                        list_death.append(dead)

                    for dead in vertical_attack(square, queens):
                        list_death.append(dead)

                    for dead in diagonal_attack(square, queens):
                        list_death.append(dead)

                    if square not in queen_positions:
                        queen_positions.append(square)

        # if len(queen_positions) == queens:
        #     print(queen_positions)
        # print(queen_positions)
