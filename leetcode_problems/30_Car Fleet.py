class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[[s,v] for s,v in zip(position,speed)]
        stack=[]
        for s,v in sorted(pair)[::-1]:
            stack.append((target-s)/v)
            if len(stack)>=2 and stack[-2] >= stack[-1]:
                stack.pop()
        return len(stack)
