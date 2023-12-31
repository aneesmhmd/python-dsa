class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

    def check_word(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_word

    def starts_with(self, prefix):
        curr = self.root
        words = []
        for char in prefix:
            if char not in curr.children:
                return []
            curr = curr.children[char]
        self._dfs(curr, prefix, words)
        return words

    def _dfs(self, node, prefix, words):
        if node.is_word:
            words.append(prefix)
        for char, children in node.children.items():
            self._dfs(children, prefix+char, words)


obj = Trie()
wordLists = ['Anees', 'Ajmal', 'Aflah', 'Naira', 'Nahna', 'Ishra']
for i in wordLists:
    obj.insert(i)
print(obj.starts_with('A'))