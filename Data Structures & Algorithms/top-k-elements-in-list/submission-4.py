class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        buckets = []

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for i in range(len(nums) + 1):
            buckets.append([]) 
        
        for num, freq in count.items():
            buckets[freq].append(num)

        toTake = k
        res = []
        N = len(buckets) - 1
        while toTake != 0:
            if len(buckets[N]) == 0:
                N -= 1
            else:
                for val in buckets[N]:
                    res.append(val)
                    toTake -= 1
                N -= 1
        
        return res


        
        


