class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for i in range(len(strs)):
            split =tuple(sorted(str(strs[i])))
            # print(split)
            if split in dict.keys():
                dict[split].append(str(strs[i]))
            else:
                dict[split]=[str(strs[i])]
        return(dict.values())
        