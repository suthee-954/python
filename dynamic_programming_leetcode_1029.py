class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        for i in range(0,len(costs)-1):
            for j in range (0,len(costs)-i-1):
                a1 = costs[j][0]
                a2 = costs[j][1]
                b1 = costs[j+1][0]
                b2 = costs[j+1][1]
                a= a1-a2
                b = b1-b2
                if(a>b):
                    temp=costs[j]
                    costs[j]=costs[j+1]
                    costs[j+1]=temp
        sum1 = 0
        for i in range(0,(len(costs)//2)):
            sum1 +=costs[i][0]
        for j in range((len(costs)//2),len(costs)):
            sum1 +=costs[j][1]

        return sum1    


                
        
