class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m=0
        for i in range(len(s)):
            l=[]
            j=i
            while(j<len(s) and s[j] not in l):
                l.append(s[j])
                j+=1
            if len(l)>m:m=len(l)
        return m


       
