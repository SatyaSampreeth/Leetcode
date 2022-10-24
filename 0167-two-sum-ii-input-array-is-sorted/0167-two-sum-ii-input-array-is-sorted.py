class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)-1):
        #     if target-numbers[i] in numbers[i+1:]:
        #         return [i+1,numbers[i+1:].index(target-numbers[i])+1+1+i]
        
        low=0
        high=len(numbers)-1
        while(low<high):
            sum = numbers[low]+numbers[high]
            if sum==target:
                return [low+1,high+1]
            elif sum<target:
                low+=1
            else:
                high-=1
        return [-1,-1]