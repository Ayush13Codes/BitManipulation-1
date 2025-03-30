class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # T: O(n), S: O(1)
        result = 0
        for num in nums:
            result ^= num
        return result
