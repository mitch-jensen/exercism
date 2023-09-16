def rows(letter: str) -> list[str]:
    possible_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letters = possible_letters[:possible_letters.index(letter) + 1]
    num_outside_spaces = len(letters) - 1
    num_outside_dots = 1
    diamond_rows = []
    first_row = True
    for letter in letters:
        if first_row:
            diamond_rows.append(num_outside_spaces * ' ' + letter + num_outside_spaces * ' ')
            first_row = False
        else:
            diamond_rows.append(
                num_outside_spaces * ' ' + letter + num_outside_dots * ' ' + letter + ' ' * num_outside_spaces)
            num_outside_dots += 2
        num_outside_spaces -= 1
    diamond_rows.extend(reversed(diamond_rows[:-1]))
    return diamond_rows
