"""
Day 3

Provided a list of rucksacks, sort and provide
the values of the common items

-- Values --
a-z = 1-26
A-Z = 27-52

https://adventofcode.com/2022/day/3
"""

import os
import string

def perform_task() -> None:
    """Entrypoint for task"""

    # Grab input file relative to this file
    dirname: str = os.path.dirname(__file__)
    filename: str = os.path.join(dirname, 'input')

    total_sack_value: int = 0
    total_badge_value: int = 0
    BADGE_SACK_COUNT = 3

    with open(file=filename, encoding='utf-8') as file:
        collection_of_sacks: list[str] = []

        for line in file:
            # Part 1
            split : int = int(len(line)/2)
            # Split RuckSack
            set_a: list[str] = line[:split]
            set_b: list[str] = line[split:]
            print(f"setA({len(set_a)}): {set_a.strip()},  setB({len(set_a)}): {set_b.strip()}")

            # Find Common value and assign score
            common_between_sets: list[str] = list(set(set_a).intersection(set_b))
            total_sack_value += get_score(common_between_sets[0])
            print(f"Common Item: {common_between_sets[0]}")

            # Part 2
            collection_of_sacks.append(line.strip())
            if len(collection_of_sacks) >= BADGE_SACK_COUNT:
                # Find common value
                common_badge: list[str] = list(set(collection_of_sacks[0])
                                    .intersection(collection_of_sacks[1])
                                    .intersection(collection_of_sacks[2]))
                badge_score: int = get_score(common_badge[0])
                print(f"Common Badge with previous sacks '{common_badge[0]}' = {badge_score}")
                total_badge_value += badge_score
                collection_of_sacks.clear()
                print("---------------------")

    # Part 1 Result
    print(f"Sum of priorities: {total_sack_value}")
    # Part 2 Result
    print(f"Sum of badge priorities: {total_badge_value}")

def get_score(item: str) -> int:
    """Given a character, return the appropriate item value"""
    score: int = 0
    if item in string.ascii_lowercase:
        score += string.ascii_lowercase.index(item) + 1
    else:
        score += string.ascii_uppercase.index(item) + 27
    return score

#  Entry
if __name__ == '__main__':
    perform_task()
