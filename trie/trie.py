class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_word = True

    def starts_with(self, prefix):
        current = self.root
        words = []
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]
        self._dfs(current, prefix, words)
        return words

    def _dfs(self, node, prefix, words):
        if node.is_word:
            words.append(prefix)
        for char, child in node.children.items():
            self._dfs(child, prefix+char, words)


obj = Trie()
wordLists = ['Anees', 'Ajmal', 'Aflah', 'Naira', 'Nahna', 'Ishra']
for i in wordLists:
    obj.insert(i)
print(obj.starts_with('A'))
