class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [0, nums[0]]

        for num in nums[1:]:
            temp = max(dp[-1], dp[-2] + num)
            dp.append(temp)
            
        return dp[-1]
        
        