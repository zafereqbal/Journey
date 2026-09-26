class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = {}
        for word in words:
            counts[word] = counts.get(word, 0) + 1

        unique_words = list(counts.keys())
        unique_words.sort(key=lambda w: (-counts[w], w))

        return unique_words[:k]