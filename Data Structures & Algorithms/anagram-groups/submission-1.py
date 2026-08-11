
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans : List[List[str]] = []
        
        hashMap : dict[str,List[str]] = defaultdict(list)
        freqMap : [int]

        for st in strs:
            freqMap = [0]*26
            for ch in st:
                freqMap[ord(ch)-ord('a')] += 1
            temp: str = ""
            for i in range(26):
                temp += chr(freqMap[i])

            hashMap[temp].append(st)

        return list(hashMap.values());
        