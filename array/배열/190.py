nums = [1, 4, 2, 3]


def findMinMax(n: list[int]) -> int:
    return sum(sorted(n)[::2])

print(findMinMax(nums))