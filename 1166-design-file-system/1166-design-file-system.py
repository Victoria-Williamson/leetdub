class FileSystem:
    def __init__(self):
        self.system = {}

    def createPath(self, path: str, value: int) -> bool:
        current = self.system
        missingParents = False
        alreadyInSystem = False
        
        paths =  path.split("/")[1:]
        
        for i in range(len(paths)):
            if i + 1 != len(paths) and paths[i] not in current:
                return False
            if i + 1 == len(paths) and paths[i] in current:
                return False
            current.setdefault(paths[i], {})
            current = current[paths[i]]
        
       
        current["value"] = value
        return True
        
       
        
        
    def get(self, path: str) -> int:
        current = self.system
        
        for p in path.split("/")[1:]:
            if p in current:
                current = current[p]
            else:
                return -1
        
        if "value" in current:
            return current["value"]
        return -1
        
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)