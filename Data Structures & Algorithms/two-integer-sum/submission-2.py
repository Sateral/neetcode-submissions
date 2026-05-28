class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        n = len(nums)

        for i in range(n):
            hashset[nums[i]] = i

        for i in range(n):
            j = target - nums[i]
            if j in hashset and hashset[j] != i:
                return [i, hashset[j]]