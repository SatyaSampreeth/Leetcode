class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            #print(i)
            #for j in range(i+1,len(numbers)):
            if target-numbers[i] in numbers[i+1:]:
                    #return [i+1,j+1]
                return [i+1,numbers[i+1:].index(target-numbers[i])+1+1+i]