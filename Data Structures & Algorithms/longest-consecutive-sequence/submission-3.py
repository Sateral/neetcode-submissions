class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        n = len(nums)
        res = 0

        starts = []
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
