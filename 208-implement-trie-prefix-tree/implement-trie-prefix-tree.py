class TrieNode:
    def __init__(self):
        # Maps a character to its corresponding TrieNode
        self.children = {}
        # True if a word ends at this node
        self.is_end_of_word = False

class Trie(object):

    def __init__(self):
        """
        Initializes the trie object.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts the string word into the trie.
        :type word: str
        :rtype: None
        """
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        """
        Returns true if the string word is in the trie, and false otherwise.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def startsWith(self, prefix):
        """
        Returns true if there is a previously inserted string word 
        that has the prefix prefix, and false otherwise.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
