class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        num_int = len(height)
        area = 0
        for i in range(num_int):
            for j in range(i + 1, num_int):
                min_height = min(height[i], height[j])
                area = max(area, min_height * (j - i))

        return area


class Solution2(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_water = 0

        left = 0

        right = len(height) - 1

        while (left < right):
            max_water = max(max_water, min(height[left], height[right]) * (right - left))

            if height[left] < height[right]:
                left += 1

            else:
                right -= 1
        return max_water