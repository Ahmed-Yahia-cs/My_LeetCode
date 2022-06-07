class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        char_bag = dict()
        for ch in s:
            char_bag[ch] = char_bag.get(ch, 0) + 1

        for ch in t:
            if char_bag.get(ch, 0):
                char_bag[ch] -= 1
            else:
                return False

        return True
        