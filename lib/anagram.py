class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, possible_anagrams):
        matches = []
        for candidate in possible_anagrams:
            if sorted(candidate.lower()) == sorted(self.word.lower()):
                matches.append(candidate)
        return matches
