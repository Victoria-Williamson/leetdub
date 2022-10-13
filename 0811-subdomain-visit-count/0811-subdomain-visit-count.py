class Solution:
    def __init__(self):
        self.domains = {}
    
    def addDomain(self, count, domain):
        current = self.domains
        for index in range(len(domain) - 1, -1, -1):
            if domain[index] == ".":
                if domain[index + 1:] in self.domains:
                    self.domains[domain[index + 1:]] += count
                else:
                    self.domains[domain[index + 1:]] = count
        
    
        if domain in self.domains:
            self.domains[domain] += count
        else:
            self.domains[domain] = count
                
 

            
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            self.addDomain(int(count), domain)
       
        sol = []
        for domain in self.domains.keys():
            sol.append(str(self.domains[domain]) + " " + str(domain))
        
        return sol
        
        
        
        
        
        