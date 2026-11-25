class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) < 3:
            return max(nums[0], nums[-1])

        best = [0] * len(nums)
        best[0] = nums[0]
        best[1] = max(nums[0], nums[1])

        print("nums", nums)

        for i in range(2, len(nums)):
            best[i] = max(best[i-2] + nums[i], best[i-1])
            print("best:", best)

        return best[-1]