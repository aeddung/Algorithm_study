class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words) != len(pattern):
            return False

        letter_mapping = {}
        word_mapping = {}

        for letter, word in zip(pattern, words):
            if letter not in letter_mapping:
                letter_mapping[letter] = word
            elif letter_mapping[letter] != word:
                return False

            if word not in word_mapping:
                word_mapping[word] = letter
            elif word_mapping[word] != letter:
                return False
        return True
