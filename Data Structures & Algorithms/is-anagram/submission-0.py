class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # number of characters should be same 
        return Counter(s) == Counter(t)


