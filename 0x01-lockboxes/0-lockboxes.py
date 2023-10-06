#!/usr/bin/python3
"""
The variable N represents number of boxes
The Boxes are arranged sequentially from'
0 to n-1 and each box may contain keys to othe boxes
"""


def canUnloackAll(boxes):
    """
    a function that determines if all the boxes can be opened

    :param boxes:
    :return: True or False
    """

    if not boxes or type(boxes) is not in list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes(n):
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return false
