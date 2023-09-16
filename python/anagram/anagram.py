def find_anagrams(word: str, candidates: list[str]) -> list[str | None]:
    anagrams = []
    if word.lower() in [candidate.lower() for candidate in candidates]:
        candidates.remove(word)
    for candidate in candidates:
        lower_case_word = word.lower()
        lower_case_candidate = candidate.lower()
        if sorted(lower_case_word) == sorted(lower_case_candidate):
            anagrams.append(candidate)
    return anagrams
