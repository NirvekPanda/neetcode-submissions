class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # max_area = (r-l) * min(heights[r],heights[l])

        l, r = 0, len(heights) - 1

        max_area = 0

        while l < r:
            new_area = (r-l) * min(heights[r], heights[l])    
            max_area = max(max_area, new_area)            

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1


        return max_area