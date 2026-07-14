class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            completor = target - n
            if completor in seen:
                return [seen[completor], i]
            else:
                seen[n] = i
                #The value at key n becomes i