class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights) + 1):
            current_height = heights[i] if i < len(heights) else 0

            while stack and heights[stack[-1]] > current_height:
                height = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area