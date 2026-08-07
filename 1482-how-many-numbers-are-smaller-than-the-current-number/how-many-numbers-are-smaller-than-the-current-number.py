class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lists=[]
        
        for i in nums:
            count=0
            for j in nums:
                if j<i:
                    count+=1
            lists.append(count)
        return lists