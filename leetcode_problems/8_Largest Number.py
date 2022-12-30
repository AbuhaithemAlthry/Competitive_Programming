class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        for i in xrange(len(nums), 0, -1):
            for j in xrange(i-1):
                if not self.compare(nums[j], nums[j+1]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return str(int("".join(map(str, nums))))

    def compare(self, n1, n2):
        return str(n1) + str(n2) > str(n2) + str(n1)
