class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        d={"++X":1,"X++":1,"--X":-1,"X--":-1}
        c=0
        for i in operations:
            c+=d[i]
        return c