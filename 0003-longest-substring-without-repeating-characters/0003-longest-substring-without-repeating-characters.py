class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = ''
        result = 0
        for c in s:
            window = window[window.find(c)+1:] + c
            result = max(result, len(window))
        return result