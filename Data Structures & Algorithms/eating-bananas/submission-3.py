import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getHours(rate: int) -> int:
            total = 0
            for n in piles:
                total += math.ceil(n / rate)

            return total

        
        l, r = 1, max(piles)

        result = (0,0)
        while l < r:
            m = (l + r) // 2
            if getHours(m) <= h:
                r = m
            else:
                l = m + 1

        return l