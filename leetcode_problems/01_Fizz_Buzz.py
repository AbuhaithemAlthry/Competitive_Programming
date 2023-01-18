class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        List = []
        for n in range(n):
            if (n+1)%3 == 0 and (n+1)%5 == 0:
                List.append("FizzBuzz")
            elif (n+1)%3==0:
                List.append("Fizz")
            elif (n+1)%5 == 0:
                List.append("Buzz")
            else:
                List.append(str(n+1))
        return List
