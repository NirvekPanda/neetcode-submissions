import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # maxHeap

        negStones = [-s for s in stones]

        heapq.heapify(negStones)

        while len(negStones) > 1:
            # top
            x = heapq.heappop(negStones)
            y = heapq.heappop(negStones)

            if x == y:
                continue
            elif x < y:
                heapq.heappush(negStones, x-y)

        if not negStones:
            negStones.append(0)    
        
        return abs(negStones[-1])