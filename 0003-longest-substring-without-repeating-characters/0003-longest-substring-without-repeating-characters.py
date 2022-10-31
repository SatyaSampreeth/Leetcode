class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # l=0
        # res=0
        # if s=='':
        #     return len(s)
        # temp=[s[l]]
        # for i in range(1,len(s)):
        #     if s[i]!=s[l] and s[i] not in temp:
        #         temp.append(s[i])
        #         print(temp)
        #     else:
        #         l=i
        #         res=max(res,len(temp))
        #         temp=[s[l]]
        # return res
        sub = set()
        j, l, m = 0, 0, 0

        while j < len(s):
            while s[j] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[j])
            m = max(m, j - l + 1)
            j += 1
        return m