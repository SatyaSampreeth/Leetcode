class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)==0:
            return [[""]]
        
        cnt = defaultdict(list)
        
        for word in strs:
            key = ''.join(sorted(word))
            cnt[key].append(word)
        return list(cnt.values())
        