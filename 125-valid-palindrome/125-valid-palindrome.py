class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s_new = ""
        for ch in s:
            if ch.isalnum():
                s_new += ch.lower()
        
        return s_new == s_new[::-1]
        