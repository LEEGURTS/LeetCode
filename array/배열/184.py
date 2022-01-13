nums = [-1, 0, 1, 2, -1, -4]


def findZero(n: list[int]) -> list[list[int]]:
    n.sort()
    result = []
    for i in range(len(n)-2):
        left = i+1
        right = len(n)-1
        while left < right:
            sum = n[i] + n[left] + n[right]
            if sum == 0:
                result.append([n[i], n[left], n[right]])
                break
            elif sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
    return result

print(findZero(nums))


