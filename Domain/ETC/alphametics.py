# alphametics.py
import re
import itertools

def solve(puzzle):
    words = re.findall('[A-Z]+', puzzle.upper())
    unique_characters = set(''.join(words))
    assert len(unique_characters) <= 10, 'Too many letters'
    first_letters = {word[0] for word in words}
    n = len(first_letters)
    sorted_characters = ''.join(first_letters) + \
        ''.join(unique_characters - first_letters)
    characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(c) for c in '0123456789')
    zero = digits[0]
    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:n]:
            equation = puzzle.translate(dict(zip(characters, guess)))
            if eval(equation):
                return equation

if __name__ == '__main__':
    puzzles = ["HAWAII + IDAHO + IOWA + OHIO == STATES"]
    # puzzles = ["I + LOVE + YOU == DORA"]  # 주석을 제거해서 다른 식으로도 해보세요
    # puzzles = ["SEND + MORE == MONEY"]
    for puzzle in puzzles:
        print(puzzle)
        solution = solve(puzzle)
        if solution:
            print(solution)