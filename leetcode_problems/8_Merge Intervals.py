class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        output = [intervals[0]]
        for x , y in intervals:
            if output[-1][1] >= x:
                output[-1][1]= max(output[-1][1],y)
            else:
                output.append([x,y])
        return output
