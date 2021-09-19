from typing import List


def add(num1: int, num2: int):
    return num1 + num2


def contains_duplicates(nums: List[int]) -> bool:
    snums = sorted(nums)
    return any(snums[i] == snums[i + 1] for i in range(len(snums) - 1))
