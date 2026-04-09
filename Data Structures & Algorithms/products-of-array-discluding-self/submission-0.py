class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        
        for i in range(len(nums)):

            
            holder = 1
            for j in range(len(nums)):
                if j != i:
                    holder *= nums[j]
            result.append(holder)

        return result