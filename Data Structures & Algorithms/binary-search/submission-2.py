class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        res = -1
        count = 10
        while l <= r:
            m = int(l + (r - l) / 2)
            if nums[m] == target:
                res = m 
                break
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return res