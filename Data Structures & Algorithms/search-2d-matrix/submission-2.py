class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def findRow(matrix, target):
            low = 0
            high = len(matrix) - 1
            while low <= high:
                mid = (low + high) // 2
                if matrix[mid][0] <= target <= matrix[mid][-1]: #if target within 1st and last elem
                     return mid
                elif target > matrix[mid][0]:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        def binarySearchRow(matrix, target, row):
            if row == -1:
                return False
            low = 0
            high = len(matrix[0]) - 1
            while low <= high:
                mid = (low + high) // 2
                if matrix[row][mid] == target:
                    return True 
                elif target > matrix[row][mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            return False

        searchRow = findRow(matrix, target)
        return binarySearchRow(matrix, target, searchRow)
                    
                
        