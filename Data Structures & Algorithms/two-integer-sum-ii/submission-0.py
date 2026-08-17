class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans : List[int]
        n = len(numbers)
        left = 0
        right = n-1
        mid = 0

        while left<=right:
            mid = (left+right)/2
            tot = numbers[left] + numbers[right]
            if tot == target:
                return [left+1,right+1]

            if tot > target:
                right -= 1
            else:
                left += 1

        return []


        