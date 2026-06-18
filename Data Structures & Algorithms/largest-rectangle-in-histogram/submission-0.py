class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        current_h = 0
        max_area = heights[0]
        
        for i in range(1,len(heights)):
            current_h = heights[i]
            count =1
            area = count * current_h
            if max_area < area:
                max_area = area

            for j in range(i-1,-1,-1):
                # print('max_area',max_area)
                # print('count',count)
                # print('')
                # # print('area',area)
                count  +=1

                if current_h >= heights[j]:
                    current_h = heights[j]

                area = count * current_h
                if max_area < area:
                    max_area = area

        return(max_area)



