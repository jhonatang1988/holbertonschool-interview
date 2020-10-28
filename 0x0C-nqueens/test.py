from typing import List

list1 = [[[['0', '0']], [['0', '1']], [['0', '2']]]]
list2 = [[[['1', '0']], [['1', '1']], [['1', '2']]]]
chess = list1 + list2

listas = []


def chess_positions(n: int = 4) -> [List[int]]:
    """
    generator to sent back a position [0, 0]
    :param n: number of queens
    :return: yields a position in the chess
    """
    return [[[[i, j]] for i in range(0, n)] for j in range(0, n)]


def permu(lists, prefix):
    if not lists:
        listas.append(prefix)
        return
    first = lists[0]
    rest = lists[1:]
    for letter in first:
        permu(rest, prefix + letter)


# print(chess_positions(6))
permu(chess_positions(6), [])
print(listas)
