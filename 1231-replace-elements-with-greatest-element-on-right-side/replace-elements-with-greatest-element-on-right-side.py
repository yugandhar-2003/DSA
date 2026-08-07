class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxr=-1
        for i in range(len(arr)-1,-1,-1):
            curr=arr[i]
            arr[i]=maxr
            if curr>maxr:
                maxr=curr
        return arr