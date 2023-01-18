class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dq=[]
        res=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while dq and temp > temperatures[dq[-1]]:
                res[dq[-1]]= i-dq[-1]
                dq.pop()
            dq.append(i)
        return res
