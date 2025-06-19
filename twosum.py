class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # Check numbers after i
                if nums[i] + nums[j] == target:  # If their sum is the target
                    return [i, j]  # Return their indices

# Example usage:
nums = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target))  # Output: [0, 1]


