#!/usr/bin/env python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on
an N×N chessboard
"""
from typing import List, Generator


def listGenerator(n: int = 4) -> Generator[List[int], None, None]:
    """
    generator to sent back a position [0, 0]
    :param n: number of queens
    :return: yields a position in the chess
    """
    return ([i, j] for i in range(0, n) for j in range(0, n))


if __name__ == '__main__':
    queens = 6
    not_repeated_list = []

    for chance in range(0, queens * queens):
        it = listGenerator(queens)
        list_possibles = []
        if chance == 0:
            start_possible = next(it)
        else:
            for i in range(0, chance + 1):
                try:
                    start_possible = next(it)
                except StopIteration:
                    break
        list_possibles.append(start_possible)

        while True:
            try:
                new_possible = next(it)
            except StopIteration:
                break

            list_possibles.append(new_possible)

            # print(list_possibles)

            for possible in list_possibles:
                if possible == new_possible:
                    continue
                if new_possible[0] == possible[0]:
                    new_list = [alist for alist in list_possibles if
                                alist != new_possible]
                    list_possibles = new_list
                    break
                if new_possible[1] == possible[1]:
                    new_list = [alist for alist in list_possibles if
                                alist != new_possible]
                    list_possibles = new_list
                    break
                if new_possible[1] == list_possibles[-2][1] + 1:
                    new_list = [alist for alist in list_possibles if
                                alist != new_possible]
                    list_possibles = new_list
                    break
                if new_possible[1] == list_possibles[-2][1] - 1:
                    new_list = [alist for alist in list_possibles if
                                alist != new_possible]
                    list_possibles = new_list
                    break
                if new_possible[1] < list_possibles[-2][1]:
                    if list_possibles[-2][1] == 5 or list_possibles[-2][1] \
                            == 4:
                        continue
                    new_list = [alist for alist in list_possibles if
                                alist != new_possible]
                    list_possibles = new_list
                    break

        if len(list_possibles) == queens:
            print(list_possibles)
        # print(list_possibles)
