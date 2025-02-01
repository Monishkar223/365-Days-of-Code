class Solution:
    def maximumWealth(self, a: List[List[int]]) -> int:
        v=[]
        for i in range(len(a)):
            c=sum(a[i])
            v.append(c)
        k=max(v)
        return k
