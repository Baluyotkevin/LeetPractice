class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # gives a dict where its a counter of how much a word appears
        words_dict = Counter(words)
        # turns the dict into an array with counter as the first ele and word as the second
        items = words_dict.items()
        # sorts the array of words/numbers from desc to asc
        sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
        # now we just want the words and since they are sorted from desc to asc
        sorted_keys = [x[0] for x in sorted_items]
        # we now return the array of sorted keys up til however many k wants
        return sorted_keys[:k]