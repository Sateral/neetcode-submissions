class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(arr: List[int]):
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l + r) // 2
                if arr[m] == target:
                    return m
                elif arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            
            return -1

        n = len(nums)
        l, r = 0, n - 1
        # Find pivot point
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        x = binarySearch(nums[0:l])
        y = binarySearch(nums[l:])

        if y != -1:
            return y + l
        else:
            return x
        
        
        
        