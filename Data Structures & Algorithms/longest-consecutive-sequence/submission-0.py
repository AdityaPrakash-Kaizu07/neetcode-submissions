class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()

        m = 1
        res = 1

        while m < len(nums):
            n = 1
            p = m

            while p < len(nums):
                if nums[p] == nums[p - 1]:
                    p += 1
                    continue

                if nums[p] == nums[p - 1] + 1:
                    n += 1
                    p += 1
                else:
                    break

            res = max(res, n)
            m = p + 1

        return res