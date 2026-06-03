class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        n = len(nums)
        res = 0

        starts = []

        # convert to set of O(1) lookup
        for n in nums:
            seen.add(n)
        
        # Get possible starts
        for n in seen:
            if n-1 not in seen:
                starts.append(n)

        for start in starts:
            temp = 1
            while (start+1 in seen):
                temp += 1
                start += 1
            res = max(res, temp)

        return res
