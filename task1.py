class Spelling_Checker:
    def __init__(self, path):
        with open(path, errors='replace') as f:
            contents = f.read()
        self.dic = contents.split("\n")
    
    def __find_pos(self, query):
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
        if query not in self.dic:
            pos = self.__find_pos(query)
            self.dic.insert(pos, query)
        else:
            print("word is already existed in the dictionary")
    
    def nearest_words(self, query):
        if query not in self.dic:
            pos = self.__find_pos(query)
            return([self.dic[pos-1], self.dic[pos], self.dic[pos+1], self.dic[pos+2],])
        else:
            print("word is already existed in the dictionary")

