class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        idxs = list()
        for i,ch in enumerate(s):
            if ch == goal[0]:
                idxs.append(i)
                
        for idx in idxs:
            if goal == s[idx:] + s[:idx]:
                return True
        
        return False