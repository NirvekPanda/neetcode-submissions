class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # return index of 2 numbers that add to target
        seen = {} # key = number, value = index

        for i, n in enumerate(nums): 
            goal = target - n

            if (goal in seen.keys()):
                # seen[goal] = position of diff item

                return [seen[goal], i]
            else: 
                seen[n] = i


        