{- Function #1
   Take as input an array, and return the list as a set (i.e. every item only is present once)
   Note we are doing this without using the set datatype that is implemented in Haskell (if interested, further reading is here: https://hackage.haskell.org/package/containers-0.6.6/docs/Data-Set.html)
-}

--arrayToSet :: Eq a => [a] -> [a] -> [a]



{- Function #2
   Take two arrays as input, convert them to sets, and then perform set union (find all unique items within both sets)
-}
--setUnion :: Eq a => [a] -> [a] -> [a]


{- Function #3
   Take two arrays as input, convert them to sets, and then perform set intersection (find all items found within both sets)
-}
--setIntersection :: Eq a => [a] -> [a] -> [a]

    
{- Function #4 
   In this function we will take as input an array of number arrays, and first compute the averages. We will then find the maximal average.
   Hint: Use helper functions!
-}
-- maxOfAverage :: (Fractional a, Ord a) => [[a]] -> a


showArray :: [[Double]] -> [Char] -> IO()
showArray [] to_print = putStrLn to_print
showArray (x:xs) to_print = showArray (xs) (to_print ++ (show x) ++ "\n")



array1 = [1,2,3,4,5,6,7,8,9,10]
array2 = [1,1,1,2,2,2,3,3,3]
array3 = [81, 42, 32, 53, 72, 13, 81, 9, 10, 27, 13, 13, 53, 42, 72, 53, 6]
array4 :: [[Double]]
array4 = [[1,2,3,4,5],[2,4,6,8,10,(-4),(-6)],[1,5,5,9,5,5,1],[(-3),6,(-9),12,(-15)],[9,5,3,1,2,8,6,2,4]]


main = do
  putStrLn "Welcome to practice #1 in Haskell!"
  putStrLn "In this we will be creating three methods, and testing them with the calls below!"
  putStrLn "Testing arrayToSet with the following arrays:\n[1,2,3,4,5,6,7,8,9,10]\n[1,1,1,2,2,2,3,3,3]\n[81, 42, 32, 53, 72, 13, 81, 9, 10, 27, 13, 13, 53, 42, 72, 53, 6]\n\n"
  -- putStrLn ("Array1 to set: " ++ show (arrayToSet array1 []))
  -- putStrLn ("Array2 to set: " ++ show (arrayToSet array2 []))
  -- putStrLn ("Array3 to set: " ++ show (arrayToSet array3 []))
  -- putStrLn "Using the arrays above, we will now perform set union!\n"
  -- putStrLn ("Arrays 1 and 2: " ++ show (setUnion array1 array2))
  -- putStrLn ("Arrays 1 and 3: " ++ show (setUnion array1 array3))
  -- putStrLn ("Arrays 3 and 2: " ++ show (setUnion array3 array2))
  -- putStrLn "Now for intersection with the above arrays!\n"
  -- putStrLn ("Arrays 1 and 2: " ++ show (setIntersection array1 array2))
  -- putStrLn ("Arrays 1 and 3: " ++ show (setIntersection array1 array3))
  -- putStrLn ("Arrays 3 and 2: " ++ show (setIntersection array3 array2))
  -- putStrLn ("Lastly we will find the max value of the averages from the following matrix:" )
  -- showArray array4 ""
  -- putStrLn ("The max value from the average of the matrix is: " ++ show(maxOfAverage array4))
  -- putStrLn ("The averages that the above was calculated from : " ++ show(makeAverage array4))