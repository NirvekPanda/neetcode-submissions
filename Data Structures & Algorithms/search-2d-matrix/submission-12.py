class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
        # double bin search

        for row in matrix:

            if target > row[-1]:
                continue
            elif target < row[-1]:
                # target is in this row

                l, r = 0, len(row) -1
                while l <= r:
                    m = (l+r) //2

                    if row[m] == target:
                        return True
                    elif row[m] > target:
                        r = m - 1
                    else:
                        l = m + 1
            elif target == row[-1]:
                return True
        return False