class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            length=len(str(i))
            if length%2==0:
               count+=1
        return count

        