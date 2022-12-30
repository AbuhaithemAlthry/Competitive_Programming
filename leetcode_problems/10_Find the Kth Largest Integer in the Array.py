class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i in range(len(nums)):
            nums[i] = -int(nums[i])
        heapq.heapify(nums)
        result = 0
        for i in range(k):
           result = heapq.heappop(nums)
        return str(-result)
