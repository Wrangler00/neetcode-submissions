class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lcs = 0
        hashMap : dict[int,int] = {}

        for val in nums:
            if val not in hashMap:
                hashMap[val] = 1
            
            if val-1 in hashMap:
                hashMap[val] = hashMap[val-1]+1
            
            i = 1
            
            while (val+i) in hashMap:
                hashMap[val+i] = hashMap[val+i-1]+1
                i += 1

        for key,val in hashMap.items():
            lcs = max(lcs,val)


        return lcs