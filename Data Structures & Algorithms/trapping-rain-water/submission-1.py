class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0]*len(height)
        maxR = [0]*len(height)
        maxLeft = 0
        maxRight = 0
        total =0
        for i in range(len(height)):
            if maxL[i] < height[i]:
                if maxLeft < height[i]:
                    maxLeft = height[i]
            maxL[i] = maxLeft

        for i in range(len(height)-1,-1,-1):
            if maxR[i] < height[i]:
                if maxRight < height[i]:
                    maxRight = height[i]
            maxR[i] = maxRight

        count = 0
        for l,r in zip(maxL,maxR):
            total += min(l,r) - height[count]
            count+=1
        
        return total
            
            

        

            
            


