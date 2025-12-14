class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        cost = 0
        i=j=0
        while(i<=len(g)-1 and j <= len(s)-1):
            if(s[j]>=g[i]):
                cost+=1
                i+=1
                j+=1
            elif( s[j]<g[i]):
                j+=1
            else:
                i+=1  

        return cost            

        
