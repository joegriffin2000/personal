# takes in a list of numbers and operators(as characters) and performs a math equation.
# operations need to be sorted from least to greatest priority before running or else it won't follow pemdas.

def math_solve(arr):
    #if the array comes in with no elements, then that means the input array ended in an operator so i just put a zero at the end to catch it
    if (len(arr) == 0):
        return 0
    #if the array comes in with 1 element, then its the end of the array so just send back the number and be done with it
    if (len(arr) == 1):
        return arr[0]
    
    if (arr[1] == "+"):
        res = arr.pop(0)
        arr.pop(0)
        return res + math_solve(arr)
    elif (arr[1] == "-"):
        res = arr.pop(0)
        arr.pop(0)
        return res - math_solve(arr)
    elif (arr[1] == "*"):
        res = arr.pop(0)
        arr.pop(0)
        return res * math_solve(arr)
    elif (arr[1] == "/"):
        res = arr.pop(0)
        arr.pop(0)
        return res / math_solve(arr)

if __name__ == "__main__":
    arr1 = [2,"+",2,"*",6]
    print(math_solve(arr1))