class Solution:
    def search(self, nums: List[int], target: int) -> int:

        first = 0
        last = len(nums) - 1

        while first <= last:

            middle = last + ((first - last) // 2)

            if nums[middle] == target:
                return middle

            elif target > nums[middle]:
                first = middle + 1
            
            else:
                last = middle - 1
        
        return -1


        