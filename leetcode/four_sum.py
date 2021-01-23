class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        results = []

        for i in range(len(nums) - 3):

            for j in range(i + 1, len(nums) - 2):

                left, right = j + 1, len(nums) - 1

                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    # print(nums[i], nums[j],nums[left],nums[right] )

                    if sum < target:
                        left += 1
                    elif sum > target:
                        right -= 1
                    else:
                        if [nums[i], nums[j], nums[left], nums[right]] not in results:
                            results.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

        return results