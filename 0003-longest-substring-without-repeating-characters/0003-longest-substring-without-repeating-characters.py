class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # res =0
        # dic = collections.defaultdict(set)
        # if len(s)==1:
        #     return 1
        # l =0
        # r = 1
        # while r < len(s):
        #     dic[l].add(s[l])
        #     if s[r] not in dic[l]:
        #         dic[l].add(s[r])
        #         r += 1
        #     else:
        #         l+=1
        #         r=l+1
        # for a,i in enumerate(dic.values()):
        #     print(i)
        #     res =max(res, len(i))
        # return res
        ss =set()
        l, r = 0, 0
        res= 0
        for r in range(len(s)):
            while s[r] in ss:
                ss.remove(s[l])
                l+=1
            ss.add(s[r])
            res= max(res, r-l+1)
        return res






        # r, l =0, 0
        # ss =set()
        # res=0
        # for r in range(len(s)):
        #     while s[r] in ss:
        #         ss.remove(s[l])
        #         l+=1
        #     ss.add(s[r])
        #     res=max(res, r-l +1)
        # return res
