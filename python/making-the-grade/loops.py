"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores: list[float | int]) -> list[int]:
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    for idx, student_score in enumerate(student_scores):
        student_scores[idx] = round(student_score)
    return student_scores


def count_failed_students(student_scores: list[int]) -> int:
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    failed = 0
    for student_score in student_scores:
        if student_score <= 40:
            failed += 1
    return failed


def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    return [student_score for student_score in student_scores if student_score >= threshold]


def letter_grades(highest: int) -> list[int]:
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    lowest = 41
    num_groups = 4
    group_size = round((highest - lowest) / num_groups)
    grades = []
    for idx, _ in enumerate(range(num_groups)):
        grades.append(idx * group_size + lowest)
    return grades


def student_ranking(student_scores: list[int], student_names: list[str]) -> list[str]:
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    rankings = []
    for idx, (student_score, student_name) in enumerate(zip(student_scores, student_names), start=1):
        rankings.append(f'{idx}. {student_name}: {student_score}')
    return rankings


def perfect_score(student_info: list[str]) -> list[str]:
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for student, score in student_info:
        if score == 100:
            return [student, score]
    return []
