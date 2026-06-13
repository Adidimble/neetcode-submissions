import sys
max_int = sys.maxsize
class Solution:
    def eat_time(self,pile,eat_rate):
        time = 0
        for i in range(len(pile)):
            time += math.ceil(pile[i]/eat_rate)
        
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        output = {}

        sorted_piles = sorted(piles)
        mini_time = 0
        ans = max_int

        s= 1
        e= sorted_piles[-1]  #eating rate can be from the lowest number to max_number of bananas present in a pile
                             # [1,11,3,2] rate can be from 1 to 11 -> [1,2,3,4,5,6,7,8,9,10,11] 

        #we will check all the possible eating rate 
        while s<=e:
            mid = (s+e)//2
            current_time = self.eat_time(sorted_piles,mid)
            if current_time<=h and mid < ans:
                mini_time = current_time
                ans = mid
            if current_time > h:
                s = mid+1
            else:
                e = mid-1
        return ans



        