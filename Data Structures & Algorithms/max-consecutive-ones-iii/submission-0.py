class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        res = 0
        l = 0

        for r in range(len(nums)):
            
            # check right edge, count number of 0s

            win = nums[l:r]

            if nums[r] == 0:
                k -= 1
            
            while k < 0:
                k += (1 if nums[l] == 0 else 0)
                l += 1
            res = max(res, r - l + 1)

        return res
            