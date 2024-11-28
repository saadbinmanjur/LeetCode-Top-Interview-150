class Node:

    def __init__(self):
        self.children = [None] * 26
        self.ended = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        current = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if not current.children[index]:
                current.children[index] = Node()
            current = current.children[index]
        current.ended = True

    def search(self, word: str) -> bool:
        def find(index: int, node: Node(), word: str) -> bool:
            if index == len(word):
                return node.ended

            if word[index] != '.':
                i = ord(word[index]) - ord('a')
                node = node.children[i]
                if not node:
                    return False
                return find(index + 1, node, word)
            else:
                for i in range(26):
                    if (not node.children[i]):
                        continue
                    if find(index + 1, node.children[i], word):
                        return True
                return False
        return find(0, self.root, word)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)