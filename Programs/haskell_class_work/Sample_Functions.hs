{- A simple function to subtract two numbers.
   The typing Int -> Int -> Int tells us that our input
   is two Ints (called x and y in line 10 of the function body)
   and the output is a single Int (x - y)
   This function importantly only works with Int datapoints
   If we give it FractionalInts, Doubles, Integers, etc
   the program will fail. -}

doSub :: Int -> Int -> Int
doSub x y = x - y


{- A simple funtion to add two numbers together
   The typing of Num a => a -> a -> a tells us that we are taking
   items of the Num attribute, which encompass multiple definitions
   More information about Num can be found here: https://www.haskell.org/tutorial/numbers.html
   By using the generic typing, we allow ourselves to take in 
   any class of numbers. 
   Importantly, we are stating that the numbers that are our input 
   and the output are of the same type. That means that if we call
   this with an Int and a Double, it will automatically translate 
   the Int into a Double (if possible)
-}
doAddition :: Num a => a -> a -> a 
doAddition x y = x + y


{- A recursive function to generate the xth fibonacci number
   The function takes as input a single Int, and returns an Int
   We have two base cases, if the function is called with an int of
   0 or 1. The recursive case calls fibonacci(x-1) + fibonacci(x-2)
   Note that we do not have safeguards to prevent the function 
   from infinitely looping if a negative number is entered.
-}
fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci x = fibonacci (x - 1) + fibonacci (x - 2)


{- A recursive function to generate x!
   The function takes as input a single Int and returns an Int
   In this function we see the use of Boolean Guards
   These guards allow us to evaluate the input values and execute
   different operations based on what the input is.
   In the case of this function, when we have an Int that is 1 or 
   lower, we return 1. Otherwise we call x * factorial(x-1) 
-}
factorial :: Int -> Int
factorial x
 | x <= 1 = 1 
 | x > 1  = x * factorial (x - 1)


{- A single line function that multiplies together two items
   that are input as an ordered pair, or tuple data type.
   Note that currently there is no header for this function.
   That will force the compiler of our program to "guess" 
   and generate a type binding of Num a => (a, a) -> a
   You may check the type of a variable or function in haskell
   in the GHCI interface through the use of the command :t 
   Sample Usage: ":t pairMul"
-}
pairMul (x, y) = x * y 


{- This function will iterate through a list of items with the 
   Ord attribute and return the minimal value. 
   Note that the Num attribute is not sufficient here.
   We must have Ord be a part of the type declaration.
   If we wish to ensure that only numbers are brought in, we can
   either go with a linked attribute status, such as (Num a, Ord a)
   or a more specific type such as Real a => [a] -> a
   (Real is a class containing both Num and Ord)
-}
findMin :: Real a => [a] -> a
findMin [x] = x
findMin (x:y:rest)
 | x <= y    = findMin (x:rest)
 | otherwise = findMin (y:rest)


{- A simple function which takes in an array of ints and returns an 
   array of Ints.
   This function will multiple pairs of adjacent elements and place
   that product into a result array. If there are an odd number of 
   items in the list, the last item in the list will be squared.
-}
someMethod :: [Int] -> [Int]
someMethod []         = []
someMethod [x]        = [x*x]
someMethod (x:y:rest) = (x * y) : (someMethod  rest)


{- A function that takes in a single Int and returns a Bool.
   The function will check and return if the input integer is 
   evenly divisible by 7 
-}
divisibleBySeven :: Int -> Bool
divisibleBySeven x
 | mod x 7 == 0 = True
 | mod x 7 /= 0 = False



forcedInt :: Int
forcedInt = 7

main = do
 print("Hello world!")
 putStrLn("Goodbye world!")
 print("The difference between 10 and 7 is: ", doSub 10 7)
 {- Note the above print statement outputs in parenthesis
    The reason for this is the print statement believes it is
    taking in a tuple instead of a string as input.
	In order to fight against this we will use array concatenation
	to combine strings together (recall Strings are char arrays).
	The show function is the equivalent of calling a toString.-}
 putStrLn("The difference between 10 and 7 is: " ++ show (doSub 10 7))
 putStrLn("Adding 7 and 9.01 is: " ++ show (doAddition 7 9.01))
 putStrLn("Adding 7 and 9.01 is: " ++ show (doAddition 7 9.01))
 --putStrLn("Adding 7 and 9.01 with 7 as an Int is: " ++ show (doAddition forcedInt 9.01))
 -- The above print statement will cause an error of typing
 putStrLn("The 9th fibonacci number is: " ++ show (fibonacci 9))
 putStrLn("9! is: " ++ show (factorial 9))
 putStrLn("-9! is: " ++ show (factorial (-9)))
 putStrLn("7 * 19 is: " ++ show (pairMul (7.1, 19)))
 putStrLn("The min value in [5,3,1,9,0,-5.1,8.3] is: " ++ show (findMin [5,3,1,9,0,-5.1,8.3]))
 print(someMethod [1,2,3,4,5,6,7])
 print("Is 14 divisible by 7: " ++ show (divisibleBySeven 14))
 print("Is 311 divisible by 7: " ++ show (divisibleBySeven 311))