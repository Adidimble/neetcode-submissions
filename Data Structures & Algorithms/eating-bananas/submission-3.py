import sys
max_int = sys.maxsize
class Solution:
    def eat_time(self,pile,eat_rate):
        time = 0
        # print(pile)
        for i in range(len(pile)):
            # print('i',i)
            time += math.ceil(pile[i]/eat_rate)
            # print(time)
        
        return time



    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        output = {}

        sorted_piles = sorted(piles)
        # print(sorted_piles)
        mini_time = 0
        ans = max_int

        s= 1
        e= sorted_piles[-1]

        while s<=e:
            mid = (s+e)//2
            current_time = self.eat_time(sorted_piles,mid)
            print('mid',mid)
            print('current_time',current_time)
            print(' ')
            if current_time<=h and mid < ans:
                mini_time = current_time
                ans = mid
            if current_time > h:
                s = mid+1
            else:
                e = mid-1
        return ans



        