# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
# using all the original letters exactly once.
class Solution(object):
    def getSignature(self, str):
        char_counts = [0] * 26
        for character in str:
            char_counts[ord(character) - ord('a')] += 1
        return tuple(char_counts)

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group_anagrams = []
        group_indices = {}
        for str in strs:
            signature = self.getSignature(str)
            group_index = group_indices.get(signature, None) 
            if group_index != None:
                group_anagrams[group_index].append(str)
            else:
                group_anagrams.append([str])
                group_indices[signature] = len(group_anagrams) - 1
        return group_anagrams