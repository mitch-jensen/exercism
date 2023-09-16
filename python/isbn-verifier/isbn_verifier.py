def is_valid(isbn: str) -> bool:
    # Invalid if isbn contains anything other than numbers, an 'X' or a '-'
    if len([char for char in isbn if not char.isnumeric() and char.upper() != 'X' and char != '-']) > 0:
        return False
    numbers = []
    for char in isbn:
        if char.isnumeric():
            numbers.append(int(char))
        elif char.upper() == 'X' and isbn[-1] == char:
            numbers.append(10)
    if len(numbers) != 10:
        return False
    isbn_sum = 0
    for idx, number in enumerate(reversed(numbers), start=1):
        isbn_sum += idx * number
    return isbn_sum % 11 == 0
