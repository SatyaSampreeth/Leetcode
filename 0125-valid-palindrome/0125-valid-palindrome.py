class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=''
        for i in s:
            if i.isalnum():
                res+=i.lower()
        if res[::-1]==res:
            return True
        return False