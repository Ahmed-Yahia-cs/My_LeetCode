class Solution:
    def reverse(self, x: int) -> int:
        max_valid = 2**31
        reversed_num = 0
        
        # Handeling sign
        sign = 1 if x >= 0 else -1
        x = x if x >= 0 else x * -1
        
        # Handeling the number 
        while x > 0:
            remander = x % 10
            x = x // 10
            
            if max_valid - (reversed_num * 10) < remander:
                return 0
            
            reversed_num = (reversed_num * 10) + remander
            
        
        ans = sign * reversed_num
        return ans