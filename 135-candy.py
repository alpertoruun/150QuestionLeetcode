class Solution:
    def candy(self, ratings):
        candy=[1 for _ in range(len(ratings))]
        for i in range(0,len(ratings)-1):
            if ratings[i+1] > ratings[i] and not(candy[i+1] > candy[i]):
                candy[i+1]=candy[i]+1

        for i in range(len(ratings)-1,0,-1):
            if ratings[i-1] > ratings[i] and not(candy[i-1] > candy[i]):
                candy[i-1]=candy[i]+1
                
        return sum(candy)




            
            

        
        