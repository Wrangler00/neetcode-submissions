class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq1 = [0] * 26
        freq2 = [0] * 26
        for x in s:
            freq1[ord(x) - ord('a')] += 1

        for x in t:
            freq2[ord(x) - ord('a')] += 1

        for i in range(26):
            if freq1[i] != freq2[i]:
                return False
        
        return True
        