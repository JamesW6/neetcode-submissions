class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        input: mxn sorted matrix, m is rows, n is columns, can be any size with min 
        rows and cols at 1, and a target integer that we are looking for in matrix
        output: boolean for if the target int is in the matrix or not

        approach: treat the 2d matrix as one very large 1d array, and convert back
        and forth between the two

        loop through, while left is less than right, divide by two,
        simple binary search stuff
        '''

        left = 0
        right = len(matrix) * len(matrix[0]) - 1 
        div = len(matrix[0])
        while left <= right:
            mid = (right+left) // 2
            if matrix[mid//div][mid%div] == target:
                return True
            elif matrix[mid//div][mid%div]>target:
                right=mid-1
            else:
                left=mid+1
        return False