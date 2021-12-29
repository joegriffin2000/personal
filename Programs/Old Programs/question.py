#CS 172
#Drexel University 2018
#Joe Griffin

class Question():
    
    #Initializing and setting variable values
    def __init__(self,i):
        self.__question = ""
        self.__pa1 = ""
        self.__pa2 = ""
        self.__pa3 = ""
        self.__pa4 = ""
        self.__answer = ""
        self.setQ(i)
        self.setPA1(i)
        self.setPA2(i)
        self.setPA3(i)
        self.setPA4(i)
        self.setCorrect(i)
        
        #Setting the Question
    def setQ(self,i):
        List = [
            "Which of the following is a valid variable name?",
            "What is the version of Python taught in class?",
            "How many professors are signed up to teach this course?",
            "What can Python code NOT do for you?",
            "What is an IDE for coding with python?",
            "What is not a variable type in python?",
            "What word can be used to bring in scripts and modules to be used within a program?",
            "Which is not a way to loop lines of code?",
            "When it comes to classes what is a mandatory function for priming variables?",
            "What is the name for the function used in classes to overload the '+' sign"
            ]
        self.__question = List[i]
        
        #Setting the First Possible Answer
    def setPA1(self,i):
        List = [
            "3rdQuarter",
            "Python 1.3",
            "Only 1",
            "Create Games",
            "Thonny",
            "String",
            "Place",
            "For Loop",
            "__init__",
            "__add__"
            ]
        self.__pa1 = List[i]
        
        #Setting the Second Possible Answer
    def setPA2(self,i):
        List = [
            "quarter#3",
            "Python 3.0",
            "2",
            "Calculate Taxes",
            "NetBeans",
            "Integer",
            "Bringin",
            "While Loop",
            "__main__",
            "__plus__"
            ]
        self.__pa2 = List[i]
        
        #Setting the Third Possible Answer
    def setPA3(self,i):
        List = [
            "quarter_3",
            "Python 4.2",
            "3",
            "Teach You Karate",
            "Eclipse",
            "Video",
            "Cast",
            "Recursive Functions",
            "__add__",
            "__cont__"
            ]
        self.__pa3 = List[i]
        
        #Setting the Fourth Possible Answer
    def setPA4(self,i):
        List = [
            "quarter-3",
            "Python 2.0",
            "4",
            "Interface with your computer",
            "Atom",
            "Object",
            "Import",
            "If Statements",
            "__name__",
            "__main__"
            ]
        self.__pa4 = List[i]
        
        #Locating the number of the Correct Answer
    def setCorrect(self,i):
        List = [3,2,2,3,1,3,4,4,1,1]
        self.__answer = List[i]
        
    #Getting Everything over to the main
    def getQ(self):
        return self.__question
    def getPA1(self):
        return self.__pa1
    def getPA2(self):
        return self.__pa2
    def getPA3(self):
        return self.__pa3
    def getPA4(self):
        return self.__pa4
    def getCorrect(self):
        return self.__answer
    
#quick testing no big deal
if __name__ == "__main__":
    p1 = Question(0)
    print(p1)