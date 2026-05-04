class Solution:
    def trap(self, height: List[int]) -> int:

        l,r=0,len(height)-1
        res=0
        leftmax,rightmax=0,0

        while l<r:

            if height[l]<height[r]:
                leftmax=max(height[l],leftmax)
                res+=leftmax-height[l]
                l+=1
                

            else:
                rightmax=max(height[r],rightmax)
                res+=rightmax-height[r]
                r-=1
        
        return res
                
        


    




        