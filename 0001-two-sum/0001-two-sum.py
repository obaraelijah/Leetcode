from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        ans = []
        for i in range(len(nums)):
            secondNumber = target-nums[i]
            if(secondNumber in dict.keys()):
                secondIndex = nums.index(secondNumber)
                if(i != secondIndex):
                     return sorted([i, secondIndex])
            # Updates the dictionary with the current number and its index
            dict.update({nums[i]: i})    


# Example usage:
nums1 = [2, 7, 11, 15]
target1 = 13
solution = Solution()
print(solution.twoSum(nums1, target1)) 