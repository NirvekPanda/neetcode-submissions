class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        # Three 0's in a row per n:
        # edge cases: left and right edge

        flowers = [0] + flowerbed + [0]
        res = 0
        # first item to second last item in original
        for f in range(1, len(flowers) - 1):

            if flowers[f-1] == 0 and flowers[f] == 0 and flowers[f + 1] == 0:
               res += 1 
               flowers[f] = 1

        return n <= res

    