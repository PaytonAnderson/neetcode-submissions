class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([[beginWord, 1]])
        while q:
            cur, length = q.popleft()
            if cur == endWord:
                return length
            adj = []
            for word in wordList:
                diff = 0
                for i in range(len(cur)):
                    if cur[i] != word[i]:
                        diff += 1
                        if diff > 1:
                            continue
                if diff == 1:
                    q.append([word, length + 1])
                    adj.append(word)
            for word in adj:
                wordList.remove(word)
        return 0