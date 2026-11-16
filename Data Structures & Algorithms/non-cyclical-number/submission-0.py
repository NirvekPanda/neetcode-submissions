class Solution:
    def isHappy(self, n: int) -> bool:
        
        #fast-slow ptr chase, loop = cyclical

        def mlt(num):
            res = 0

            while num:
                digit = num % 10
                digit = digit**2
                res += digit
                num //= 10
            return res

        slow = n
        fast = mlt(n)

        while slow != fast:
            slow = mlt(slow)
            fast = mlt(fast)
            fast = mlt(fast)
        return fast == 1

