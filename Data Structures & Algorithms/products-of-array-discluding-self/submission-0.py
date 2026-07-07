import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range (len(nums)):
            prod_left = math.prod(nums[:i])
            prod_right = math.prod(nums[i+1:])
            l.append(prod_left*prod_right)
        return l