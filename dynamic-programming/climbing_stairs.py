class Solution:
    seen = {}
    def climbStairs(self, n: int) -> int:
        if n in self.seen:
            return self.seen[n]
        if n == 0 or n == 1:
            return 1
        else:
            result = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.seen[n] = result
        return result
