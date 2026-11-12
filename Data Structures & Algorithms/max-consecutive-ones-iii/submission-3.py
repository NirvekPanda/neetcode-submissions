class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        l, res = 0, 0
        count = k

        for r in range(len(nums)):
            if nums[r] == 0:
                count -= 1

            while count < 0:
                if nums[l] == 0:
                    count += 1
                l += 1

            res = max(res, r - l + 1)

        return res
