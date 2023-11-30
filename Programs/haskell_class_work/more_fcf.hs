{- 
   Dr Michaels
   more_fcs.hs
   This file contains more examples of first class functions.
-}

{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use map" #-}
{-# HLINT ignore "Redundant bracket" #-}
{- In our introduction to FCF we noted that
   the "Driver" function will look very 
   similar across many cases, it is the input
   function(s) that provide the differences in 
   execution. This comes from Haskell's functional
   nature.
   Let's examine a few more cases of driver 
   functions. First, we'll look at a driver 
   which will take a matrix and return an array.
   It will therefore need a function which returns
   a single value from an input array.
-}

-- Why wouldn't we want to do this with an array
-- input only? Why the matrix?
-- Even though this is "reducing/folding" the input
-- we are still following the normal map style
-- as our return value is an array.
testMatrix :: ([a] -> b) -> [[a]] -> [b]
testMatrix _ []     = []
testMatrix f (x:xs) = (f x) : (testMatrix f xs)


{- A function to pass a character array into checkParen to determine if the array is "balanced".
   Note that it allows us to run checkParen on an array with ease above!
-}
balancedParen :: [Char] -> Bool
balancedParen x = checkParen x []

checkParen :: [Char] -> [Char] -> Bool
checkParen [] [] = True
checkParen [] ('(':_) = False
checkParen (')':_) [] = False
checkParen ('(':xs) ys = checkParen xs ('(':ys)
checkParen (')':xs) ('(':ys) = checkParen xs ys
checkParen (_:_) _ = False
checkParen _ (_:_) = False

makeAverage :: (Fractional a) => [a] -> a
makeAverage x = (sum x) / (fromIntegral (length x))

{- Now what if we wished to apply functions to a
   matrix that return a matrix? There are
   several considerations to make here, including
   what type of transformation do we want?
   Should the function be [[a]] -> [[b]]?
   Or should it be [a] -> [b]
-}
-- If we take in a matrix to matrix function, there
-- is no recursion here, the input function handles
-- it all.
transformMatrix :: ([[a]] -> [[b]]) -> [[a]] -> [[b]]
transformMatrix _ [] = []
transformMatrix f x  = f x

transformMatrix2 :: ([a] -> [b]) -> [[a]] -> [[b]]
transformMatrix2 _ []     = []
transformMatrix2 f (x:xs) = (f x) : (transformMatrix2 f xs)


{- In this function we call quicksort on the concatenation of our input matrix.
   We then will use the makeMatric function defined below to divide it into equal sized
   subarrays.
-}
concatAndSort :: Ord a => [[a]] -> [[a]]
concatAndSort x = makeMatrix (quickSort y) (length y `div` length x)
                  where
                    y = concat x

quickSort :: Ord a => [a] -> [a]
quickSort []     = []
quickSort (p:xs) = (quickSort lesser) ++ [p] ++ (quickSort greater)
    where
        lesser  = filter (< p) xs
        greater = filter (>= p) xs

{-
   A function to transform an array into a matrix composed of arrays of size x
   Where x is an int. A negative value will cause an infinite loop as nothing 
   will be taken or dropped. 
-}
makeMatrix :: [a] -> Int -> [[a]]
makeMatrix [] _    = []
makeMatrix x count = take count x : makeMatrix (drop count x) count

{- For the last function to look at today, let's
   consider the task of reducing a matrix to a single
   datapoint, much like a fold function. In the path we'll 
   take today, we're going to use two functions, the first 
   to transform a matrix into a 1D array, the second to 
   transform the array into a singular value. 
-}

compressMatrix :: ([[a]] -> [b]) -> ([b] -> c) -> [[a]] -> c
compressMatrix f1 f2 x = f2 (f1 x)

getMinMaxPair :: Ord a => [[a]] -> [(a,a)]
getMinMaxPair []     = []
getMinMaxPair (x:xs) = (minimum x, maximum x) : getMinMaxPair xs

getBestPair :: (Num a, Ord a) => [(a,a)] -> (a,a)
getBestPair [] = (0,0)
getBestPair [(x,y)] = (x,y)
getBestPair ((x,y):(a,b):xs)
 | (y - x) >= (b - a) = getBestPair ((x,y):xs)
 | otherwise          = getBestPair ((a,b):xs)

showArray :: (Show a) => [[a]] -> [Char] -> IO()
showArray [] to_print = putStrLn to_print
showArray (x:xs) to_print = showArray (xs) (to_print ++ (show x) ++ "\n")


test_paren :: [String]
test_paren = ["((()))", "((())","(()))","(()()()((())))()"]
test_nums :: [[Double]]
test_nums = [[1,2,3,4,5],[7,5,3,1,2,4,6],[10,12,14,11,13,16],[1,3,5,7,9,8,6,4,2],[6,4,2,6,4,2],[10,10,10,10,11,10,10,10,10],[4,1,2,4,6,8,5,3,2,4]]

main :: IO ()
main = do
  print (test_paren)
  print (testMatrix balancedParen test_paren)
  print (testMatrix makeAverage test_nums)
  print("\nTransformMatrix call one")
  showArray (transformMatrix concatAndSort test_paren) []
  print("\n\nTransformMatrix call two")
  showArray (transformMatrix concatAndSort test_nums) []
  print("\n\nTransformMatrix call three")
  showArray (transformMatrix2 quickSort test_nums) []
  print(compressMatrix getMinMaxPair getBestPair test_nums)