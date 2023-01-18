class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums1)
        m=len(nums2)
        ret=[-1]*n
        for i in range(n):
            ind=nums2.index(nums1[i])
            for j in range(ind,m):
                if nums2[j]>nums1[i]:
                    ret[i]=nums2[j]
                    break
        return ret



