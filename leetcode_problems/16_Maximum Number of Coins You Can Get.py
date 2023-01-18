class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l=0
        r=len(piles)-1
        arr=[]
        sumz = 0
        while l < r:
            ar = []
            ar.append(piles[l])
            l+=1
            ar.append(piles[r])
            ar.append(piles[r-1])
            sumz+=piles[r-1]
            r-=2
        return sumz
