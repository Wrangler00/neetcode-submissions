import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap : defaultdict[int,int] = defaultdict(int)

        for val in nums:
            hashMap[val] += 1
        
        topK = heapq.nlargest(
            k,
            hashMap.items(),
            key=lambda item: item[1]
        )

        return [item[0] for item in topK]


        