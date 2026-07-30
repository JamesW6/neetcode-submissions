class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listOfAnnys=[]
        i=0
        while i<len(strs):
            map1={}
            thisList=[]
            thisList.append(strs[i])
            for letter in strs[i]:
                if letter in map1:
                    map1[letter]+=1
                else:
                    map1[letter]=1
            j=i+1
            while j<len(strs):
                map2={}
                for letter in strs[j]:
                    if letter in map2:
                        map2[letter]+=1
                    else:
                        map2[letter]=1
                if map1==map2:
                    thisList.append(strs[j])
                    del strs[j]
                else:
                    j+=1
            i+=1
            listOfAnnys.append(thisList)
        return listOfAnnys
                