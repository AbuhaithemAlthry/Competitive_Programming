class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while stack and k and i < stack[-1]:
                stack.pop()
                k-=1
            stack.append(i)
            print(stack)
        stack = stack[:len(stack) - k]
        res = "".join(stack)
        return str(int(res)) if res else "0"
