class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        left = 0
        right = len(height) - 1
        left_max = height[0]
        right_max = height[-1]
        volume = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume