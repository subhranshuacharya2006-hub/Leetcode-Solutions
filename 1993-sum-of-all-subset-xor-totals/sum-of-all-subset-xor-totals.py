class Solution:
    def subsetXORSum(self, nums):
        def solve(i, xor):
            if i == len(nums):
                return xor

            return solve(i + 1, xor) + solve(i + 1, xor ^ nums[i])

        return solve(0, 0)