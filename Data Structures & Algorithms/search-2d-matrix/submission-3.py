class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(nums: list[int]) -> bool:
            l, r = 0, len(nums) - 1

            while l <= r:
                m = (l + r) // 2

                if nums[m] == target:
                    return True
                elif target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            return False

        top, bot = 0, len(matrix) - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                return binarySearch(matrix[row])
        
        return False