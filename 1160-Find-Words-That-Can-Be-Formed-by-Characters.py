class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charCounter = Counter(chars)
        return sum([len(word) for word in words if Counter(word) <= charCounter])
