class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            idx = (left + right) // 2
            if nums[idx] == target:
                return idx
            elif nums[idx] > target:
                right = idx - 1
            else:
                left = idx + 1
        return -1
