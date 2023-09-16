def is_isogram(string: str) -> bool:
    cleaned_string = ''.join([char for char in string if char.isalpha()]).lower()
    return len(list(cleaned_string)) == len(set(cleaned_string))
