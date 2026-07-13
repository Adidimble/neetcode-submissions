class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        valid_nums = set(nums)
        # print(valid_nums)
        max_seq = 0

        for num in valid_nums:
            count = 1
            prev_num = num-1
            while prev_num in valid_nums:
                count+=1
                prev_num-=1
            if max_seq < count:
                max_seq = count
        
        return(max_seq)
        
                