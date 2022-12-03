"""
Day 2

Provided a strategy guide for rock-paper-scissors,
first column being the opponents move and the second for our move,
calculate your score if the guide is followed.

-- Scoring --
X = A = Rock = 1 points
Y = B = Paper = 2 points
Z = C = Scissors = 3 points

Loss = 0 points
Draw = 3 points
Win = 6 points

# Part 2
X = Loss
Y = Draw
Z = Win

https://adventofcode.com/2022/day/2
"""

import os

# Move Map
ROCK = ['X', 'A']
PAPER = ['Y', 'B']
SCISSORS = ['Z', 'C']

# Condition Map
LOSS = ['X']
WIN = ['Z']

# Score Map
SCORE : dict[list[str], dict[str, int | str]] = {
    'ROCK': {
        'score': 1,
        'wins_against': 'SCISSORS',
        'loses_against': 'PAPER'
    },
    'PAPER': {
        'score': 2,
        'wins_against': 'ROCK',
        'loses_against': 'SCISSORS'
    },
    'SCISSORS': {
        'score': 3,
        'wins_against': 'PAPER',
        'loses_against': 'ROCK'
    },
}

def perform_task() -> None:
    """Entrypoint for task"""

    # Grab input file relative to this file
    dirname: str = os.path.dirname(__file__)
    filename: str = os.path.join(dirname, 'input')

    part_1: int = 0
    part_2: int = 0
    with open(file=filename, encoding='utf-8') as file:
        for line in file:
            characters = line.strip().split(' ')
            part_1 += get_points(get_move(characters[1]), get_move(characters[0]))
            part_2 += get_points_optimal(get_move(characters[0]), characters[1])

    # Results
    print(f"Part_1 score = {part_1}")
    print(f"Part_2 score = {part_2}")

def get_points(our_move: str, opponent_move: str) -> int:
    """Returns the points received after move combination"""
    # Get move points
    score: int = SCORE[our_move]["score"]

    # Determine win / loss / draw points
    if our_move == opponent_move:
        score += 3
    elif SCORE[our_move]["wins_against"] == opponent_move:
        score += 6
    return score

def get_points_optimal(opponent_move: str, condition: str) -> int:
    """Given opponent move and the desired match condition, return the points"""
    score: int = 0
    if condition in LOSS:
        # We want to lose
        score += SCORE[SCORE[opponent_move]['wins_against']]['score']
    elif condition in WIN:
        # We want to win
        score += SCORE[SCORE[opponent_move]['loses_against']]['score']
        score += 6
    else:
        # We want to draw
        score += SCORE[opponent_move]['score']
        score += 3
    return score

def get_move(move: str) -> str:
    """Given a letter, returns the move name"""
    if move in ROCK:
        return "ROCK"
    if move in PAPER:
        return "PAPER"
    if move in SCISSORS:
        return "SCISSORS"
    return ""

#  Entry
if __name__ == '__main__':
    perform_task()
