"""
Day 4

Provided a list of rucksacks, sort and provide
the values of the common items

-- Values --
a-z = 1-26
A-Z = 27-52

https://adventofcode.com/2022/day/4
"""

import os


def perform_task() -> None:
    """Entrypoint for task"""

    # Grab input file relative to this file
    dirname: str = os.path.dirname(__file__)
    filename: str = os.path.join(dirname, 'input')

    fully_covered_count: int = 0
    partial_covered_count: int = 0
    with open(file=filename, encoding='utf-8') as file:

        for line in file:
            split_sections : str = line.strip().split(',')
            x_1: int = int(split_sections[0].split('-')[0])
            x_2: int = int(split_sections[0].split('-')[1])
            y_1: int = int(split_sections[1].split('-')[0])
            y_2: int = int(split_sections[1].split('-')[1])
            # Part 1
            if (x_1 <= y_1 and x_2 >= y_2) or (y_1 <= x_1 and y_2 >= x_2):
                print(f"found Covered instance: A({split_sections[0]}) = B({split_sections[1]})")
                fully_covered_count += 1
            # Part 2
            if (((x_1 < y_1 and x_2 >= y_1) or (x_1 <= y_2 and x_2 > y_2)) and
                (not (x_1 >= y_1 and x_2 <= y_2) and (x_1 != y_1 and x_2 != y_2)
                and not (x_1 <= y_1 and x_2 >= y_2))):
                print(f"found Partial instance: A({split_sections[0]}) <=> B({split_sections[1]})")
                partial_covered_count += 1
    print(f"Instances of fully covered assignments: {fully_covered_count}")
    print(f"Instances of Partial covered assignments: {partial_covered_count}")
    print(f"All Instances of covered assignments: {partial_covered_count + fully_covered_count}")


#  Entry
if __name__ == '__main__':
    perform_task()
