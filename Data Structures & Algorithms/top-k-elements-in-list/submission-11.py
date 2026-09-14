class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # negative min heap
        h = []

        for n in count.keys(): 
            heapq.heappush(h, (count[n], n))

            # keep only k most freq
            if len(h) > k:
                heapq.heappop(h)

        res = []
        for i in range(k):
            # h[0] = occurances_of_num, h[1] = num
            res.append(heapq.heappop(h)[1])

        return res