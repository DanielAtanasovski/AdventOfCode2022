"""
Day 1

Provided a list of calories, inventories seperated by a blank line,
calculate which group has the most calories

https://adventofcode.com/2022/day/1
"""

import os

def perform_task():
    """Entrypoint for task"""

    # Grab input file relative to this file
    dirname: str = os.path.dirname(__file__)
    filename: str = os.path.join(dirname, 'input')

    # Create dictionary of { total_calories : [ calories ] }
    results: dict = {}
    with open(filename, encoding='utf-8') as file:
        values : list[int] = []
        values_sum : int = 0
        for line in file:
            if line.strip() == '':
                results[values_sum] = values.copy()
                values_sum = 0
                values.clear()
            else:
                values.append(int(line))
                values_sum += int(line)

    # Part A
    sorted_list: list[tuple[int, list[int]]] = sorted(results.items(), reverse=True)
    print(f"Largest Elf Calories = {sorted_list[0][0]}")

    # Part B
    largest_3 = sorted_list[0][0] + sorted_list[1][0] + sorted_list[2][0]
    print(f"Largest 3 Elf Calories = {largest_3}")

#  Entry
if __name__ == '__main__':
    perform_task()
