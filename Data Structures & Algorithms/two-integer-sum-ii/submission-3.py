class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        i = 0
        found = False
        compl = 0
        while found == False:
            compl = target - numbers[i]
            left = i + 1
            right = len(numbers) - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == compl:
                    found = True
                    res = [i + 1, mid + 1]
                    break
                if numbers[mid] < compl:
                    left = mid + 1
                else: 
                    right = mid - 1
            i += 1
        return res