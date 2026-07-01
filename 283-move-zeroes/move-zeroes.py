class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = []

        for i in nums:
            if i != 0:
                ans.append(i)
        
        while len(ans) < len(nums):
            ans.append(0)

        for i in range(len(nums)):
            nums[i] = ans[i]
        