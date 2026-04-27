def two_sum(nums, target):
    seen = {}  # val → index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i
    return []

# Test
print(two_sum([2,7,11,15], 9))  # [0, 1]