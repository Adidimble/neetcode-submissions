class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lowest_h = -1
        max_water = 0
        s=0
        end= len(heights) -1
        while s<end:
            lowest_h = min(heights[s],heights[end])
            print('heights[s]',s)
            print('heights[end]',end)
            print('lowest_h',lowest_h )
            current_water = lowest_h * (end-s)
            print('current_water', current_water)
            print('max_water', max_water)
            if max_water < current_water:
                max_water = current_water
            elif heights[s] >heights[end]:
                end -=1
            else:
                s +=1
        
        return max_water
