class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sets = set(nums)
        longest = 0
        for n in nums:
            length = 0
            if n-1 not in sets:
                while n + length in sets:
                    length += 1
                longest = max(length, longest)
        return longest
