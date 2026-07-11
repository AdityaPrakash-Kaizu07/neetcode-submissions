class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if target - numbers[i] in numbers[i + 1:]:
                j = numbers.index(target - numbers[i], i + 1)
                return [i + 1, j + 1]