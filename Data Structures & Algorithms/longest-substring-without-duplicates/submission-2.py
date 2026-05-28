class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        'ajegnavjgnw'
        i = 0
        j = 0
        r = 0
        while i <= len(s) - 1:
            print(seen)
            if s[i] in seen:
                r = max(r, len(seen))
                while s[i] in seen:
                    seen.remove(s[j])
                    j += 1
            seen.add(s[i])
            i += 1
        
        return max(r, len(seen))