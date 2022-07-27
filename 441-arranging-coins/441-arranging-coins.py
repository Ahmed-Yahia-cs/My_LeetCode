class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        level = 1
        filled = 0
        
        while n > 0:
            
            n = n - level
            
            if n >= 0:
                filled += 1
                
            level += 1
        
        return filled