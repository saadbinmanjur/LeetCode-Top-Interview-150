class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_grp = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_grp[sorted_word].append(word)
        return list(anagram_grp.values())