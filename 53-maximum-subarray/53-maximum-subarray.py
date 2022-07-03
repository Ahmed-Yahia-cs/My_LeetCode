class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        
        prev_sum = nums[0]
        for num in nums[1:]:
            
            curr_sum = prev_sum + num
            
            if curr_sum <= num:
                max_sum = max(num, max_sum)
                prev_sum = num
                
            else:
                max_sum = max(curr_sum, max_sum)
                prev_sum = curr_sum
                
                


                
        return max_sum
        