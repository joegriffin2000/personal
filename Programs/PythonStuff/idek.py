# file for testing storing function calls into a dictionary
# run the file for a quick UI and see it work

def useless(x):
    if x.isidentifier():
        print('useful')
    else:
        return
    
def printer(x):
    if x.isalpha():
        print(x)
    else:
        return

def mod2(x):
    if x.isdigit():
        print(int(x)%2)
    else:
        return

if __name__ == "__main__":
    dictionary = dict()
    dictionary[0] = useless
    dictionary[1] = printer
    dictionary[2] = mod2
    
    print('Enter your input:')
    user = input('').strip()
    
    for i in dictionary:
        dictionary[i](user)