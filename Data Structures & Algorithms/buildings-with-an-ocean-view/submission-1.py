class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        res = []
        stack = []
        res.append(len(heights)-1)

        for i in reversed(range(len(heights))):
            # 1 < 2 
            if stack and stack[-1] < heights[i]:
                stack.pop()
                res.append(i)
            elif stack and stack[-1] > heights[i]:    
                continue
            
            stack.append(heights[i])
        

        return [r for r in reversed(res)]