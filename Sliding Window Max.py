from collections import deque

def sliding_window_max(nums, k):
    dq = deque()   # stores indices, decreasing order of value
    result = []
    for i, n in enumerate(nums):
        # remove indices outside window
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        # remove smaller elements from back
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

print(sliding_window_max([1,3,-1,-3,5,3,6,7], 3))
# [3, 3, 5, 5, 6, 7]