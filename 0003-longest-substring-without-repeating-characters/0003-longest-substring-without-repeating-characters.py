class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # window = ''
        # result = 0
        # for c in s:
        #     window = window[window.find(c)+1:] + c
        #     result = max(result, len(window))
        # return result
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res