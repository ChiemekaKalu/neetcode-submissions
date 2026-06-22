class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for day, curTemp in enumerate(temperatures):
            while stack and curTemp > stack[-1][0]:
                oldTemp, oldDay = stack.pop()
                res[oldDay] = day - oldDay
            stack.append((curTemp, day))
        return res