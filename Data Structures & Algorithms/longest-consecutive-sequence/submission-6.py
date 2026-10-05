class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        new_nums = set(nums)
        for i in new_nums:
            if i-1 not in new_nums:
                local_len = 1
                while i+1 in new_nums:
                    i = i+1
                    local_len+=1
                if local_len > best:
                    best = local_len
    
        return(best)
