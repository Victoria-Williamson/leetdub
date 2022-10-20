class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        groups = []
        levels = []
        
        lCount = 0
        tCount = 0
        lWords = []
        
        def addLevel(c, w,t):
           
            l = ""
            rem = (maxWidth - t) % (max(1,len(w) - 1))
            spaces =(maxWidth - t) // (max(1,len(w) - 1))
            print(c,w,t, spaces)
            for word in w[:-1]:
                if rem != 0:
                    l += word + (" "  * (spaces + 1))
                    rem -= 1
                else:
                    l += word + (" "  * (spaces))
            if len(w) == 1:
                l += w[-1] + (" "  * (spaces))
            else:
                l += w[-1]
            return l
                
            
        for word in words:
            if lCount + len(word) <= maxWidth:
                lWords.append(word)
                tCount += len(word)
                if lCount + len(word) + 1 < maxWidth:
                    lCount += len(word) + 1
                else:
                    lCount += len(word)
                    groups.append((lCount, lWords, tCount))
                    lCount = 0
                    tCount = 0
                    lWords = []
            else:
                groups.append((lCount - 1, lWords, tCount))
                lWords = [word]
                lCount = len(word) + 1
                tCount = len(word)
        if lCount > 0:
            groups.append((lCount - 1, lWords, tCount))
        
        for g in groups[:-1]:
            c, w, t = g
            levels.append(addLevel(c,w,t))
        
        temp = ""
       
        c, w, t = groups[-1]
        for word in w[:-1]:
            temp +=  word + " "

        temp += w[-1] + " " * (maxWidth - len(temp) - len(w[-1]))
        levels.append(temp)
        return levels
        
                
        