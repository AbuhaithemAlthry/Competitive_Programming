class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)      
        print(cnt)
        num_freq = sorted(cnt.values(), reverse=True) 
        print(num_freq)   
        half_size = len(arr) // 2
        ans = 0
            
        while half_size > 0:
            half_size -= num_freq[ans]
            ans += 1
        print(half_size,ans)   
        return ans
