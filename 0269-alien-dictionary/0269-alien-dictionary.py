class Solution:
    def alienOrder(self, words: List[str]) -> str:
        beforeCount = {}
        visited = set()
        lettersBefore = {}
    
        if len(words) == 1:
            notRepeatedLetters = set()
            for letter in words[0]:
                notRepeatedLetters.add(letter)
            return "".join(letter for letter in notRepeatedLetters)
        for i in range(len(words)):
            for j in range(i + 1,len(words)):
                index = 0
                if i != j:
                    foundAfter = False
                    while index < len(words[i]) and index < len(words[j]):
                        if words[i][index] != words[j][index]:
                            if words[i][index] not in lettersBefore:
                                lettersBefore[words[i][index]] = []
                            lettersBefore[words[i][index]].append(words[j][index])
                            if words[j][index] not in beforeCount:
                                beforeCount[words[j][index]] = 0
                            beforeCount[words[j][index]] += 1
                            foundAfter = True
                            break
                        else:
                            index += 1
                    if not foundAfter and len(words[i]) > len(words[j]):
                        return ""
                    for letter in words[i]:
                        if letter not in lettersBefore:
                            lettersBefore[letter] = []
                    for letter in words[j]:
                        if letter not in lettersBefore:
                            lettersBefore[letter] = []
                        
        q = []
        sol = ""
        
        for letter in lettersBefore:
            if letter not in beforeCount:
                q.append(letter)
        
        
        while q:
            letter = q.pop(0)
            if letter not in visited:
                if letter in lettersBefore:
                    for nLetter in lettersBefore[letter]:
                        beforeCount[nLetter] -= 1
                        if beforeCount[nLetter] == 0:
                            q.append(nLetter)
                visited.add(letter)
                sol += letter
        print(sol, len(lettersBefore))
        if len(sol) != len(lettersBefore):
            return ""
        return sol
      
                                
                            
                
        
        
            
        
    
    
        
        
        
        