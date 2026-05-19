class Solution:
    def isanagram(self,str1,str2):
        if len(str1) != len(str2):
            return False
        
        map1 ={}
        map2 ={}
        for char1,char2 in zip(str1,str2):
            if char1 in map1:
                map1[char1] +=1
            else:
                map1[char1] =1

            if char2 in map2:
                map2[char2] +=1
            else:
                map2[char2] =1
        if map1 != map2:
            return False
        
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        raw_strs = [value for value in strs]
        result = []

        #sort the list length wise
        sorted_raw_strs = sorted(raw_strs,key = len)
        #raw_strs.sort(key=len) another way
        print(sorted_raw_strs)
        for sorted_char in sorted_raw_strs:
            if result != []:
                for result_list in result:
                    if self.isanagram(result_list[0],sorted_char):
                        result_list.append(sorted_char)
                        break
                else:
                    result.append([sorted_char])
            else:
                result.append([sorted_char])
        
        return result

