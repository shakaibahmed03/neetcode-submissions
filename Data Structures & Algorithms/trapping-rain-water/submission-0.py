class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)

        if n==0:
            return 0
        
        leftmax=[0]*n
        rightmax=[0]*n

        leftmax[0]=height[0]
        for i in range(1,n):
            leftmax[i]=max(height[i],leftmax[i-1])

        
        rightmax[n-1]=height[n-1]
        for j in range(n-2,-1,-1):
            rightmax[j]=max(height[j],rightmax[j+1])
        
        res=0

        for s in range(n):
            res+=min(leftmax[s],rightmax[s])-height[s]
        
        return res









        