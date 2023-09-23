class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)  # Sort the words by length to process shorter words first
        word_chain = defaultdict(int)  # Store the longest chain for each word

        for word in words:
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]
                word_chain[word] = max(word_chain[word], word_chain[prev_word] + 1)

        return max(word_chain.values())