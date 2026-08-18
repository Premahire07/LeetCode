class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = nums.count(0)
        
        for num in nums:
            if num != 0:
                total_product *= num
                
        ans = []
        for num in nums:
            if zero_count > 1:
                ans.append(0)
            elif zero_count == 1:
                ans.append(total_product if num == 0 else 0)
            else:
                ans.append(total_product // num)
                
        return ans
