from lab6 import *

def plus(x,y):
    return x+y
def minus(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

f = open("input.txt",'r+')

if __name__ == '__main__':
    mainstack = Stack()
    for char in f.readline():
        print(char)
        if char =='exit':
            break
        elif char == " ":
            pass
        elif char == "+" or char == "-" or char == "*" or char == "/":
            top = mainstack.top()
            mainstack.pop()
            below = mainstack.top()
            mainstack.pop()
            new = 0
            if char == "+":
                new = plus(top,below)
            elif char == "-":
                new = minus(top,below)
            elif char == "*":
                new = multiply(top,below)
            elif char == "/":
                new = divide(top,below)
            mainstack.push(new)
        elif char == int(char):
            mainstack.push(char)
        else:
            pass
        
    print(mainstack)
f.close()