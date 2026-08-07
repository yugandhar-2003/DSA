class Solution:
    def countElements(self, nums: List[int]) -> int:
        count=0
        mini=min(nums)
        maxi=max(nums)
        for i in range(len(nums)):
            if nums[i]>mini and nums[i]<maxi:
                count+=1 
        return count

        