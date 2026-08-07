class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #s and t should have the same freq and type of elements
        mapOfS = {}  
        mapOfT = {}
        if len(s) != len(t):
            return False

        for eleS, eleT in zip(s,t):
            # print(type(mapOfS))
            mapOfS[eleS] = mapOfS.get(eleS,1) + 1
            mapOfT[eleT] = mapOfT.get(eleT,1) + 1
        
        print("mapOfS",mapOfS)
        print("mapOfT",mapOfT)
        if mapOfS == mapOfT:
            return True
        return False