class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up:
        dp = {}
        dp[1] = 1
        dp[2] = 2 # 1+1, 2

        if n == 1 or n == 2:
            return dp[n]

        # for a number, count how mnay ways it can be added
        # if number alreayd in dp, skip, subtract it, cont
        for i in range(1, n+1):
            
            if i not in dp.keys():
                dp[i] = dp[i-2] + dp[i-1]

        return dp[n]