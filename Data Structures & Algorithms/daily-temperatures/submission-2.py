class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for index, currentTemp in enumerate(temperatures):
            while stack and currentTemp > stack[-1][1]:
                earlierIndex, earlierTemp = stack.pop()
                res[earlierIndex] = index - earlierIndex
            stack.append((index, currentTemp))

        return res