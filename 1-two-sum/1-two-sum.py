class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        visited = list()
        
        for idx in range(len(nums)):
            wanted = target - nums[idx]
            
            if wanted in visited:
                return [idx, visited.index(wanted)]
                
            visited.append(nums[idx])
                
        return results
        