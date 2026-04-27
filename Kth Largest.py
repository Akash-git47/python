import heapq

def find_kth_largest(nums, k):
    # min-heap of size k; top = kth largest
    heap = nums[:k]
    heapq.heapify(heap)
    for n in nums[k:]:
        if n > heap[0]:
            heapq.heapreplace(heap, n)
    return heap[0]

print(find_kth_largest([3,2,1,5,6,4], 2))  # 5
# No full sort — heap stays size k throughout