class Solution:
    def singleNumber(self, a: List[int]) -> int:
        d={}
        for i in range(len(a)):
            if a[i] not in d:
                d[a[i]]=1
            else:
                d[a[i]]+=1
        for key,value in d.items():
            if value==1:
                return key
