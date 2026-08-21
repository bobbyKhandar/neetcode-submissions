class Solution:
    def encode(self, strs: List[str]) -> str:
        res=""
        for word in strs:
            for letter in word: 
                res+=str(ord(letter))
                res+="-"
            res+=str(256)
            res+="-"
        return res 

    def decode(self, s: str) -> List[str]:
        res=[]
        temp=""
        prev=""
        for letter in s:
            if letter=="-":
                if prev==str(256):
                    res.append(temp)
                    temp=""
                    prev=""
                else:
                    temp+=chr(int(prev))
                    prev=""
            else:
                prev+=letter
    
        return res