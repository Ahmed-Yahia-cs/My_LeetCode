class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list) #sorted_anagrames : list of original same anagrames
        for str in strs:
            chs = [0] * 26
            for ch in str:
                idx = ord(ch) - ord('a')
                chs[idx] += 1
            groups[tuple(chs)].append(str)

        return groups.values()
        