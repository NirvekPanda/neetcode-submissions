import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cnt = Counter(nums)
        res = []
        for key, val in cnt.most_common(k):
            res.append(key)

        return res