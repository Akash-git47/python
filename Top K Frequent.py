from collections import Counter
import heapq

def top_k_frequent(nums, k):
    freq = Counter(nums)
    # min-heap of (count, val) — size k
    return heapq.nlargest(k, freq.keys(), key=freq.get)

print(top_k_frequent([1,1,1,2,2,3], 2))  # [1, 2]

# Manual heap version (for interview clarity):
def top_k_manual(nums, k):
    freq = Counter(nums)
    heap = []
    for val, cnt in freq.items():
        heapq.heappush(heap, (cnt, val))
        if len(heap) > k:
            heapq.heappop(heap)
    return [v for _, v in heap]
