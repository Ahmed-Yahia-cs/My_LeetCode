class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        bag = set()
        for item in nums:
            if item in bag:
                return True
            bag.add(item)
        return False
        