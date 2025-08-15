class Solution(object):

    def fizzBuzz(self, n):

        result = []
        for i in range(1, n+1):

            if (i % 5 == 0) and (i % 3 == 0):
                result.append("FizzBuzz")

            elif i % 5 == 0:
                result.append("Buzz")
            elif i % 3 == 0:
                result.append("Fizz")
            else:
                result.append(f"{i}")
        return result


sol = Solution()

print(sol.fizzBuzz(50))
