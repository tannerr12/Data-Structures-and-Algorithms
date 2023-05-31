class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.tableCount = defaultdict(int)
        self.table = defaultdict(dict)
        
        #for i in range(len(names)):
        #    self.table[names[i]] = names[i]
        #    self.table[names[i]]['size'] = columns[i]

    def insertRow(self, name: str, row: List[str]) -> None:
        self.table[name][self.tableCount[name]] = row
        self.tableCount[name] +=1

    def deleteRow(self, name: str, rowId: int) -> None:
        del self.table[name][rowId-1]
        

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        
        return self.table[name][rowId-1][columnId-1]


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)