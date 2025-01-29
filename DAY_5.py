class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=sorted(s)
        t1=sorted(t)
        a=t1==s1
        return a
                
