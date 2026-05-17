class Solution:
    def climbStairs(self, n: int) -> int:
        
        return self.mem(n, {})
    
    def mem(self, n, cache: dict):

        if n <= 2:
            cache[n] = n
            return cache[n]

        if n in cache:
            return cache[n]
        
        cache[n] = self.mem(n-1, cache) + self.mem(n - 2, cache)

        return cache[n]