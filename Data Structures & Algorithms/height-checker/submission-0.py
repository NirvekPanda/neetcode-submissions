class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        expected = sorted(heights)

        res = 0
        for h, e in zip(heights, expected):
            if h != e:
                res += 1

        return res