class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        max_=0
        nums.sort()
        while l<r:
            max_ = max(max_,(nums[l]+nums[r]))
            l+=1
            r-=1

        return max_
