class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset = defaultdict(list)
        for s in strs:
            sorted_s = ''.join(sorted(s))
            hashset[sorted_s].append(s)

        return list(hashset.values())