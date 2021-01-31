class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]: return False

        left = 0

        size_row = len(matrix)
        size_col = len(matrix[0])
        right = size_row * size_col
        while left < right:

            middle = left + (right - left) / 2
            if (matrix[middle / size_col][middle % size_col] == target):

                return True

            elif (matrix[middle / size_col][middle % size_col] > target):
                right = middle

            else:
                left = middle + 1

        return False

