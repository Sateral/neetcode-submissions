class Solution:
    def __init__(self):
        self.idxs = []

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            self.idxs.append(len(s))
            encoded += s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        offset = 0
        for i in self.idxs:
            res.append(s[offset:offset + i])
            offset += i
        return res
