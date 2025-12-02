class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        halmaz = set()
        for num in nums:
            if num in halmaz:
                return True
            halmaz.add(num)
        return False