class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in set(nums):
            d[i]=nums.count(i)
        l = sorted(d, key=d.get, reverse=True)
        res = []
        for i in range(k):
            res.append(l[i])
        return res