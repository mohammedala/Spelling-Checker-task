class Spelling_Checker:
    def __init__(self, path):
        # constructor of the class
        # path: path to the dictionary file
        # Space complexity: O(n), where n is the number of words in the dictionary file.
        # Time complexity: O(n), where n is the number of words in the dictionary file. 

        with open(path, errors='replace') as f:
            contents = f.read()
        self.dic = contents.split("\n")
    
    def __find_pos(self, query):
        # this method is a helper function
        # this method is not accessed outside the class
        # this method finds the index that the query would be in if it were in the dictionary
        # query: a word that is not in the dictionary 
        # Space complexity: O(1)
        # Time complexity: O(log n), where n is the number of words in the dictionary. 
        
        lower = len(self.dic)
        upper = 0
        mid = len(self.dic) //2
        while (True):
            if self.dic[mid] < query:
                upper = mid
                mid = (lower-upper) // 2 + upper

                if (lower-upper) == 2:
                    if self.dic[upper] < query and self.dic[upper+1] > query:
                        return(upper+1)
                    else:
                        return(lower)
                    
            elif self.dic[mid] > query:
                lower = mid
                mid = (lower-upper) // 2

                if (lower-upper) == 2:
                    if self.dic[upper] < query and self.dic[upper+1] > query:
                        return(upper+1)
                    else:
                        return(lower)

    def insert_word(self, query):
        # this method insert a query word in the dictionary in lexicographic order 
        # query: a word that is not in the dictionary 
        # Space complexity: O(1)
        # Time complexity: O(log n), where n is the number of words in the dictionary. 
        
        if query not in self.dic:
            pos = self.__find_pos(query)
            self.dic.insert(pos, query)
        else:
            print("word is already existed in the dictionary")
    
    def nearest_words(self, query):
        # this method return a list of nearest 4 words to query in the dictionary in lexicographic order 
        # query: a word that is not in the dictionary 
        # Space complexity: O(1)
        # Time complexity: O(log n), where n is the number of words in the dictionary. 

        if query not in self.dic:
            pos = self.__find_pos(query)
            return([self.dic[pos-1], self.dic[pos], self.dic[pos+1], self.dic[pos+2],])
        else:
            print("word is already existed in the dictionary")
