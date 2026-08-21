class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for num in nums: 
            hm[num]=hm.get(num,0)+1
        freq=[]
        for num,count in hm.items():
            freq.append([count,num])
        freq.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(freq[i][1])
        return res