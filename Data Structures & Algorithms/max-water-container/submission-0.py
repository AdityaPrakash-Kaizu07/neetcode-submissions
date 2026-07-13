class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        j=len(heights)-1
        i=0
        while i < j :
            tem=0
            tem = (j-i) * min(heights[i],heights[j])
            if area < tem:
                area = tem
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return area