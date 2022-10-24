class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        res=1
        o=1
        nums=list(sorted(set(nums)))
        for i in range(len(nums)-1):
            print(res,o)
            if nums[i+1]==nums[i]+1:
                res+=1
            else:
                if res>o:
                    o=res
                res=1
        if res>o:
            return res
        return o
    