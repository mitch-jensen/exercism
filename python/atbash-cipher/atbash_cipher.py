def alphabet() -> str:
    return 'abcdefghijklmnopqrstuvwxyz'


def encode(plain_text: str) -> str:
    plain_text = ''.join([char.lower() for char in plain_text if char.isalnum()])
    letters = alphabet()
    encoded = []
    group_size = 0
    for char in plain_text:
        group_size += 1
        if char in letters:
            index = letters.index(char)
            reversed_letter = letters[-index - 1]
            encoded.append(reversed_letter)
        else:
            encoded.append(char)
        if group_size == 5:
            encoded.append(' ')
            group_size = 0
    return ''.join(encoded).strip()


def decode(ciphered_text: str) -> str:
    ciphered_text = ciphered_text.lower()
    letters = alphabet()
    decoded = []
    for char in ciphered_text:
        if char in letters:
            index = letters.index(char)
            reversed_letter = letters[-index - 1]
            decoded.append(reversed_letter)
        elif char.isnumeric():
            decoded.append(char)
    return ''.join(decoded)
