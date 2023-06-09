#Trie implementation

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.word_count = 0

    def insert(self,key):
        curr_node = self

        for c in key:
            
            if curr_node.children[ord(c)-ord('a')] == None:
                print(f"{c} is inserted")
                
                new_node = TrieNode()

                curr_node.children[ord(c)-ord('a')] = new_node

            curr_node = curr_node.children[ord(c)-ord('a')]
        
        curr_node.word_count+=1
    
    def search_prefix(self,key):
        curr_node = self

        for c in key:
            if curr_node.children[ord(c)-ord('a')] == None:
                return False
            curr_node = curr_node.children[ord(c)-ord('a')]
        return True
    
    def search_word(self,key):
        curr_node = self
        for c in key:
            if curr_node.children[ord(c)-ord('a')] == None:
                return False
            curr_node = curr_node.children[ord(c)-ord('a')]
        
        return curr_node.word_count>0
    
    def delete(self,word):
        curr_node = self
        last_branch_node = None
        last_branch_char = 'a'

        for c in word:
            if curr_node.children[ord(c)-ord('a')] == None:
                return False
            else:
                count = 0

                for i in range(26):
                    if curr_node.children[i] != None:
                        count+=1
                
                if count>1:
                    last_branch_node = curr_node
                    last_branch_char = c
                curr_node = curr_node.children[ord(c)-ord('a')]
        
        count = 0
        for i in range(26):
            if curr_node.children[ord(c)-ord('a')] != None:
                count+=1
        
        if count>0:
            curr_node.word_count-=1
            return True
        if last_branch_node is not None:
            last_branch_node.children[ord(last_branch_char) - ord('a')] = None
            return True
        else:
            self.children[ord(word[0])-ord('a')]=None
            return True
    
    # def print_trie(self,node,pre,output):
    #     if node.is_word>0:
    #         output.append((pre+node))       

trie = TrieNode()
trie.insert("and")
trie.insert("ani")
trie.insert("dad")
trie.insert("dag")

print(trie.search_prefix('an'))
print(trie.search_prefix('da'))
print(trie.search_word('and'))
print(trie.search_word('ant'))
print(trie.search_word('t')) 
# if trie.delete("ant"):
#     print("ant deleted")
# else:
#     print("ant not in trie")