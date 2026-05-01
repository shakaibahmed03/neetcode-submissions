class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # order matters [2,1]=[1,2]

        res=[]
        n=len(nums)
        used=[False]*n

        def backtrack(path):
            if len(path)==n:
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i]) 
                used[i]=True        #  O(n^2 * n)
                                            # O(n *n)
                backtrack(path)
                path.pop()
                used[i]=False

        
        backtrack([])
        return res


        