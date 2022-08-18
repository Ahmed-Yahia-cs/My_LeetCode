class Solution:
    def reverse(self, x: int) -> int:
        # Handeling sign
        sign = 1 if x >= 0 else -1
        x = x if x >= 0 else x * -1
        
        # Handeling the number 
        number_str = str(x)[::-1]
        
        ans = sign * int(number_str)
        
        # output checking
        if ans < -2**31 or ans > 2**31:
            ans = 0
        return ans