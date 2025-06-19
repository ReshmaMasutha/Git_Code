class Solution:
    def twoSum(self, nums, target):
        length = 0
        # Find the length without using len()
        for _ in nums:
            length += 1
        
        i = 0
        while i < length:
            j = i + 1
            while j < length:
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1

# Example usage:
nums = [2, 7, 11, 15]
target = 9
sol = Solution()
result = sol.twoSum(nums, target)
print(result) 
 # Output: [0, 1]
