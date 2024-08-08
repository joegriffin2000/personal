class TextBox():
    def __init__(self,raw:str,width:int):
        self.__width__ = width
        self.__raw__ = raw
    
    def __getattribute__(self, name):
        return super().__getattribute__(name)
    def __delattr__(self, name):
        raise AttributeError(f"{type(self).__name__} doesn't support attribute deletion")
    def __setattr__(self, name, value):
        if name == '__width__':
            if not isinstance(value, int):
                raise TypeError(f'width must be of type int: not {type(value)}')
            if value <= 0:
                raise ValueError(f'width must be greater than zero: not {value}')
            super().__setattr__(name,value)
        elif name == '__raw__':
            if not isinstance(value, str | list):
                raise ValueError(f'raw must either be a string or a list of strings')
            if not isinstance(value, list) and not isinstance(value[0], str):
                raise ValueError(f'raw must either be a string or a list of strings')
            super().__setattr__(name,value)
        elif name == 'message':
            raise AttributeError(f'attribute {name} does not allow assignment.')
        else:
            raise AttributeError(f'attribute {name} does not exist.')
        
        if hasattr(self, '__raw__') and hasattr(self, '__width__'):
            super().__setattr__('message',self.generate())
    
    def generate(self): #essential dont mess this up
        message = [""]
        temp = self.seperate()
        
        #trimming each word and moving its carry to the following index (inserts right after the word with the carry)
        for i in range(len(temp)):
            if len(temp[i]) > self.__width__:
                swap = temp[i]
                temp[i] = swap[self.__width__:]
                temp.insert(i,swap[:self.__width__])
        
        #joining words where possible (also includes the carries from the previous loop)
        index = 0
        for i in temp:
            if len(message[index]) + len(i) + 1 <= self.__width__:
                message[index] += " "+i
            else:
                index+=1
                message.append(i)
            
            if temp.index(i) == 0: #for the extra whitespace on first line
                message[0] = message[0].strip()
            
        return message
    
    def seperate(self):
        #splits the raw string (or list of strings) into seperate words and returns the list containing everything
        temp = []
        if isinstance(self.__raw__,str):
            temp += self.__raw__.split()
        elif isinstance(self.__raw__,list):
            for i in self.__raw__:
                temp += i.split()
                
        return temp
    
    def setWidth(self,width):
        #allows you to change the width of the text box
        self.__width__ = width
    
    def setRaw(self,raw):
        #allows you to change the text of the text box
        self.__width__raw
    
    def copy(self):
        #returns a copy of the text box object
        return TextBox(self.__raw__,self.__width__)
    
    def __len__(self):
        return len(self.message)
    
    def __eq__(self,other):
        return self.message == other.message
    def __ne__(self,other):
        return self.message != other.message
    
    def __contains__(self,x):
        return x in self.message
    
    def __repr__(self):
        return self.message
    
    def __str__(self):
        return "\n".join(self.message)
    
if __name__ == "__main__":
    linespace = 3
    testbox = TextBox("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",50)
    print(testbox,end="\n"*linespace)
    
    testbox.__raw__ = ["This is a test message.","I was born in the 18th century.","I'm acutally a ghost who is possessing this 24 year olds body.","BOO"]
    testbox.__width__ = 40
    print(testbox)