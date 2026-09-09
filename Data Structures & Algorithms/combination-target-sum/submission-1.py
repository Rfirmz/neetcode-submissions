class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res, sol = [], []

        def backtrack(i, runSum):

            if runSum == target:
                res.append(sol[:])
                return
            
            if runSum > target or i == len(nums):
                return
            
            for j in range(i, len(nums)):
                sol.append(nums[j])
                backtrack(j, runSum + nums[j])
                sol.pop()

        backtrack(0, 0)
        return res