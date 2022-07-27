class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        level = 1
        
        while True:
            
            cost = level *(level + 1) / 2
            
            if cost <= n:
                level += 1
            
            else:
                break
                
        return level - 1