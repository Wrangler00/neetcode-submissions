
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans : List[List[str]] = []
        
        hashMap : dict[tuple[int,...],List[str]] = defaultdict(list)
        freqMap : list[int]

        for st in strs:
            freqMap = [0]*26
            
            for ch in st:
                freqMap[ord(ch)-ord('a')] += 1

            hashMap[tuple(freqMap)].append(st)

        return list(hashMap.values());
        