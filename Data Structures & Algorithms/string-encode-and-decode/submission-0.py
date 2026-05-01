class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for chars in strs:
            res.append(str(len(chars))+"#"+chars)
        result=''.join(res)
        return result

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i

            while s[j]!='#':
                j+=1
            

            length=int(s[i:j])
            store=s[j+1:j+1+length]
            res.append(store)

            i=j+1+length
        return res
