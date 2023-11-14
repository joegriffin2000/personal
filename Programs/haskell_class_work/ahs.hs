import Distribution.Simple.Utils (xargs)

doSub :: Int -> Int -> Int
doSub x y = x - y

{-
this is a comment
-}

doAddition :: Num a => a -> a -> a
doAddition x y = x + y


fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci x = fibonacci(x - 1) + fibonacci(x - 2)


findMin :: Real a => [a] -> a
findMin [x] = x
findMin (x:y:rest)
 | x <= y     = findMin(x:rest)
 | otherwise  = findMin(y:rest)

factorial :: Int -> Int
factorial x
 | x < 1 = 1
 | x > 1 = x * factorial(x-1)
 | otherwise = 1

betterFib :: Integer -> Integer
betterFib 0 = 0
betterFib 1 = 1
betterFib x 
 | x < 0 = -1
 | otherwise = doFib 0 1 1 x

doFib :: Integer -> Integer -> Integer -> Integer -> Integer
doFib fib1 fib2 curr target
 | curr < target = doFib fib2 (fib1+fib2) (curr+1) target
 | otherwise     = fib2


main = do
    putStrLn "4th Fibonacci Number" 
    print(betterFib 4)