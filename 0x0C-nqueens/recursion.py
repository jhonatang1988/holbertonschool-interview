def max_recur(lst):
    """find the maximum value in a list"""
    if len(lst) == 1:
        return lst[0]

    if lst[0] > lst[-1]:
        return max_recur(lst[:-1])
    else:
        return max_recur(lst[1:])


print(max_recur([-1, 4, 7, -129, 3424, 394]))
