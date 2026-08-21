class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm=defaultdict(list)
        for word in strs:
            alphabets=[0]*26
            for letter in word:
                alphabets[ord(letter)-ord('a')]+=1
            hm[tuple(alphabets)].append(word)
        return list(hm.values())
            
            