#jeoinc
class nat():
    def __init__(self,n):
        if self.__isValidFromInt(n):
            raise ValueError("nat can not have value that is negative")
        else:
            self.val = n

    def __isValidFromInt(self,num):
        result = True
        if num < 0:
        return result