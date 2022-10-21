class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        a=1
        for i in nums:
            
            res.append(a)
            a*=i
        a=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=a
            a*=nums[i]
        return res
            