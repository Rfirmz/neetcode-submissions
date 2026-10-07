class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search the first elements first

        lo, hi = 0, len(matrix) - 1
        row = None
            

        while lo <= hi:
            mid = (hi + lo) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[0]) - 1]:
                row = matrix[mid]
                break
            
            elif target < matrix[mid][0]:
                hi = mid - 1
            
            else:
                lo = mid + 1
        
        if row == None:
            return False
        
        lo, hi = 0, len(row) - 1

        while lo <= hi:
            mid = (hi + lo) // 2
            if target == row[mid]:
                return True
            elif target < row[mid]:
                hi = mid - 1
            else:
                lo = mid + 1

        return False