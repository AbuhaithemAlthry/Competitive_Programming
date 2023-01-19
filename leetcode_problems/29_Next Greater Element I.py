class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        tempDict = {}
        for i in nums2:
            while stack and stack[-1] < i:
                poppedNum = stack.pop()
                tempDict[poppedNum] = i
                print(tempDict)
            stack.append(i)
            print(stack,tempDict)
            
        for i in range(len(nums1)):
            if nums1[i] in tempDict:
                nums1[i] = tempDict[nums1[i]]
                
            else:
                nums1[i] = -1
        
        return nums1
