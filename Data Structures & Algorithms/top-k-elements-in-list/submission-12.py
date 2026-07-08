class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ele_count = {}
        output = []
        for num in nums:
            ele_count[num] = ele_count.get(num,0) +1
        
        sorted_dict = dict(sorted(ele_count.items(),key = lambda items: items[1]))
        print(sorted_dict)

        for i in range(k):
            element,count = sorted_dict.popitem()
            output.append(element)
        return(output)