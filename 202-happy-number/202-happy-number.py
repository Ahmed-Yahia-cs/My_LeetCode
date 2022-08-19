class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()

        
        while True:
            if n == 1:
                return True
            
            if n in visited:
                return False

            visited.add(n)
            
            temp = 0
            while n > 0:
                temp += (n % 10)**2
                n = n // 10     
            n = temp
        