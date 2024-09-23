class Solution:
    def findMedianSortedArrays(self, nums_1: List[int], nums_2: List[int]) -> float:
        i1, i2, i = 0, 0, 0
        res = [None] * (len(nums_1) + len(nums_2))
        while i1 < len(nums_1) and i2 < len(nums_2):
            if nums_1[i1] < nums_2[i2]:
                res[i] = nums_1[i1]
                i1 += 1
            else:
                res[i] = nums_2[i2]
                i2 += 1
            
            i += 1
        
        while i1 < len(nums_1):
            res[i] = nums_1[i1]
            i1 += 1
            i += 1

        while i2 < len(nums_2):
            res[i] = nums_2[i2]
            i2 += 1
            i += 1

        n = len(res)//2
        if len(res)%2 == 1:
            return res[n]
        else:
            return (res[n-1] + res[n])/2
