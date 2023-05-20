class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        set2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        set3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}

        result = []
        for word in words:
            wordset = set(word.lower())
            if (wordset & set1 == wordset) or (wordset & set2 == wordset) or (wordset & set3 == wordset):
                result.append(word)
        
        return result
