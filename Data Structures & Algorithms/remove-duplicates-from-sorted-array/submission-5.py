class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l = 1
        for r in range(1, len(nums)):
            # l is 0 item, r is 1 item
            # if r is == l, thers a duplicate
            # want to take first non dup and replace r item

            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1

        return l