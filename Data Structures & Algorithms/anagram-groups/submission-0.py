class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_list = []
        for i in range(len(strs)):
            value = strs[i]
            value = ''.join(sorted(value))
            row = []
            for j in range(len(strs)):
                v = strs[j]
                v = ''.join(sorted(v))
                if v == value:
                    row.append(strs[j])
            my_list.append(row)
        return list(map(list, set(map(tuple,my_list))))

        
        