class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_dicts = []
        anagrams = []

        for word in strs:
            temp_dict = {}
            for letter in word:
                temp_dict[letter] = temp_dict.get(letter, 0) + 1
            
            if (temp_dict in all_dicts):
                index = all_dicts.index(temp_dict)
                anagrams[index].append(word)
            else:
                all_dicts.append(temp_dict)
                anagrams.append([word])
        return anagrams
