class WordDictionary(object):

    def __init__(self):
        self.root = {}

    def addWord(self, word):
        node = self.root

        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]

        node["#"] = True

    def search(self, word):
        def dfs(node, index):
            if index == len(word):
                return "#" in node

            ch = word[index]

            if ch == ".":
                for key in node:
                    if key != "#" and dfs(node[key], index + 1):
                        return True
                return False

            if ch not in node:
                return False

            return dfs(node[ch], index + 1)

        return dfs(self.root, 0)