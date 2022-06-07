class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bag = dict()
        for index, value in enumerate(nums):
            diff = target - value
            if diff in bag:
                return [bag[diff] , index ]
            bag[value] = index