class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        s=set(nums)

        for num in s:
            current=num
            if num-1 not in s:
                current=num
                length=1
                while current+1 in s:
                    current+=1
                    length+=1
                longest=max(longest,length)
        return longest
        