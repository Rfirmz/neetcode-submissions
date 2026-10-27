class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        sol, res = [], []

        def backtrack():


            if len(sol) == len(nums):
                res.append(sol[:])
                return

            
            for j in range(len(nums)):

                
                if nums[j] in sol:
                    continue
                
                sol.append(nums[j])
                backtrack()
                sol.pop()

        backtrack()
        return res
        
