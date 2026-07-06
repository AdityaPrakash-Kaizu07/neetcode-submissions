from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for i in nums :
            dic[i]+=1
        sorted_items = sorted(dic.items(), key = lambda x : x[1], reverse=True)
        res = []
        for i in range (k):
            res.append(sorted_items[i][0])

        return res