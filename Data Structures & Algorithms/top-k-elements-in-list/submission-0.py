class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicts = {}
        for i in nums:
            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1
                
        sorted_dict = dict(sorted(dicts.items(), key=lambda item: item[1], reverse=True))

        result = list(sorted_dict.keys())[:k]
        print(sorted_dict)
        return result