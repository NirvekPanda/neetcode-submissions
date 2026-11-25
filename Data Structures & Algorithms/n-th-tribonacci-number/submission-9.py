class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        # memoization
        T = [0] * (n + 1)
        T[0] = 0
        T[1] = 1
        T[2] = 1
        
        for i in range(3, n+1):
            T[i] = T[i-3] + T[i-2] + T[i-1]
            # print("i: ", i, "T: ", T[i])

        return T[n]