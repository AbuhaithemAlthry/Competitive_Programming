class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        dic=defaultdict(int)
        outp=[]
        changed.sort()
        for i in changed:
            dic[i] += 1
        for nums in changed:
            if nums !=0 and dic[nums]!=0 and dic[2*nums] != 0:
                dic[nums]-=1
                dic[2*nums]-=1
                outp.append(nums)
            elif nums == 0 and dic[nums]!=0 and dic[nums]%2 == 0:
                x = int(dic[nums]/2)
                s=[0 for i in range(x)]
                dic[nums]=0
                outp+=s
            elif nums!=0 and nums%2 ==0:
                if dic[nums]!=0 and dic[nums/2] != 0:
                    dic[nums]-=1
                    dic[nums/2]-=1
                    outp.append(nums/2)
        b = True
        for i in changed:
            if dic[i] != 0:
                b = False
                break
        if b:
            return outp
        return []
