#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        minIdx = i
        minVal = arr[i]
        
        #Index got shifted by -i in enumerate
        for index, val in enumerate(arr[i:]):
            if val < minVal: 
                minIdx = index + i 
                minVal = val 
        return minIdx
            
    
    def selectionSort(self, arr,n):
        #code here
        for index, val in enumerate(arr):
            minIdx = self.select(arr, index)
            arr[index], arr[minIdx] = arr[minIdx], arr[index]
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
