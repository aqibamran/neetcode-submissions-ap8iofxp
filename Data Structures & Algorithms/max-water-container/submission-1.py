class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        res = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i == j:
                    area = 0
                elif heights[i] < heights[j]:
                    area = heights[i] * abs(j-i)
                else:
                    area = heights[j] * abs(j-i)
        
                if area > res:
                    res = area
        return res
                