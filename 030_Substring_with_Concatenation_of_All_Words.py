# You are given a string, s, and a list of words, words, that are all of the same length.
# Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once
# and without any intervening characters.
#
# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]
#
# You should return the indices: [0,9].
# (order does not matter).
#
# Tags: Hash Table, Two Pointers, String
# Difficulty: Hard

import collections


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words or not words[0]:
            return []

        word_len = len(words[0])
        max_index = len(s) - word_len
        substring_len = len(words) * word_len

        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        result = []
        for i in xrange(min(word_len, len(s) - substring_len + 1)):
            left = right = i
            count = {}

            while right <= max_index:
                word = s[right: right + word_len]
                right += word_len

                if word in word_count:
                    count[word] = count.get(word, 0) + 1

                    while count[word] > word_count[word]:
                        left_word = s[left: left + word_len]
                        count[left_word] -= 1
                        left += word_len

                    if right - left == substring_len:
                        result.append(left)

                else:
                    count.clear()
                    left = right

        return result

    def findSubstring1(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        words_size = len(words)
        word_len = len(words[0])

        word_count = collections.defaultdict(int)
        for word in words:
            word_count[word] += 1

        result = []
        for index in xrange(len(s) - word_len * words_size + 1):
            i = index
            w = 0
            count = collections.defaultdict(int)

            while w < words_size:
                start = i + w * word_len
                word = s[start: start + word_len]
                if word not in words:
                    break
                count[word] += 1
                if count[word] > word_count[word]:
                    break
                w += 1

            if w == words_size:
                result.append(index)

        return result


if __name__ == '__main__':
    print Solution().findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"])
