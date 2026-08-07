class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        lists=[]
        for i in range(len(nums)):
            lists.insert(index[i],nums[i])
        return lists