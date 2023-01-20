class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_ar=0
        while l<r:
            if height[r] <= height[l]:
                A= (r-l) * height[r]
                r-=1
            elif height[r] > height[l]:
                A=(r-l)*height[l]
                l+=1
            print(height[l],height[r])
            max_ar=max(A,max_ar)

        return max_ar
