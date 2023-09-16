"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist_order_matches_superlist(sublist: list, superlist: list) -> bool:
    i, j = 0, 0

    while i < len(superlist) and j < len(sublist):
        if superlist[i] == sublist[j]:
            j += 1
        i += 1

    return j == len(sublist)


def sublist(list_one: list, list_two: list):
    if list_one == list_two:
        return EQUAL
    if all(item in list_one for item in list_two):
        if sublist_order_matches_superlist(list_two, list_one):
            return SUPERLIST
    if all(item in list_two for item in list_one):
        if sublist_order_matches_superlist(list_one, list_two):
            return SUBLIST
    return UNEQUAL
