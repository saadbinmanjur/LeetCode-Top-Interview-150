class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        iter = (x // 2) + 2 
        for i in range(1,iter):
            if i**2 == x:
                return i
            if i*i > x:
                return i - 1