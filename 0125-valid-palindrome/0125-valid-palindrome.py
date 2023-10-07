class Solution:
    def isPalindrome(self, s: str) -> bool:
        # l, r = 0, len(s) - 1
        # while l < r:
        #     while l < r and not s[l].isalnum():
        #         l += 1
        #     while l < r and not s[r].isalnum():
        #         r -= 1
        #     if s[l].lower() != s[r].lower():
        #         return False
        #     l += 1
        #     r -= 1
        # return True
#         s = [i for i in s.lower() if i.isalnum()]
    	
#         return s == s[::-1]
    
        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[~i] for i in range(len(s)//2))