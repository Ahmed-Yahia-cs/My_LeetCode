class Solution:
    def countBits(self, n: int) -> List[int]:
        
        result = list()
        
        for num in range(n+1):
            ones_count = self.count_ones(num)
            result.append(ones_count)
            
        return result
    
    def count_ones(self, num):
        ones = 0
        while num:
            ones += num % 2
            num = num >> 1
            
        return ones
        