class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            middle = (top + bottom) // 2
            if matrix[middle][-1] < target:
                top = middle + 1
            elif matrix[middle][0] > target:
                bottom = middle - 1
            else:
                top = middle
                break
        
        if top >= len(matrix):
            return False
            
        left = 0
        right = len(matrix[top]) - 1
        row = matrix[top]

        while left <= right:
            middle = (left + right) // 2
            if row[middle] < target:
                left = middle + 1
            elif row[middle] > target:
                right = middle - 1
            else:
                return True
        
        if matrix[top][left] == target:
            return True
        return False
