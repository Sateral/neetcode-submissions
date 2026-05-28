class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)

        for s in strs:
            letterCount = [0] * 26 # a ... z

            for c in s: # Get key based on number of letters
                letterCount[ord(c) - ord("a")] += 1
            
            dict[tuple(letterCount)].append(s)
        
        return dict.values()
            
