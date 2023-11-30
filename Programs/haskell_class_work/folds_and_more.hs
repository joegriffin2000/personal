{-
    Dr Michaels
    folds_and_more.hs
    This file will contain several functions which use fold and zip to generate their results. 
    More information on folding can be found at: https://wiki.haskell.org/Fold
    More information on scanning can be found at: https://zvon.org/other/haskell/Outputprelude/scanl_f.html (click the related links for scanr and 1 versions)
    More information on zip can be found at: https://zvon.org/other/haskell/Outputprelude/zip_f.html (click related for zipwith and unzip)
-}
{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use camelCase" #-}
{-# HLINT ignore "Use sum" #-}

insert :: Ord t => t -> [t] -> [t]
insert x []     = [x]
insert x (h:t)
  | x <= h      = x:(h:t)
  | otherwise   = h:insert x t

data_one :: [Double]
data_one = [1,2,3,4,5,6,7,8,9,10]
data_two :: [Double]
data_two = [9,4,1,3,10,8,5,2,6,7]

main = do
    putStrLn "In this file we will present examples of folding and zipping, both inline and within functions"
    putStrLn "Let us first look at the differences between foldl and foldr"
    putStrLn "We have two arrays that are the ints 1-10. One is sorted, one is not"
    putStrLn "Foldl and Foldr of the two arrays with + and /"
    putStrLn ("Foldl + Array1: " ++ show (foldl (+) 0 data_one))
    putStrLn ("Foldl + Array2: " ++ show (foldl (+) 0 data_two))
    putStrLn ("Foldr + Array1: " ++ show (foldr (+) 0 data_one))
    putStrLn ("Foldr + Array2: " ++ show (foldr (+) 0 data_two) ++ "\n")
    -- putStrLn "Note that for all of the above calls we get the same answer, due to how addition works"
    -- putStrLn "Let us consider the case of division"
    -- putStrLn ("Foldl / Array1: " ++ show (foldl (/) 1 data_one))
    -- putStrLn ("Foldl / Array2: " ++ show (foldl (/) 1 data_two))
    -- putStrLn ("Foldr / Array1: " ++ show (foldr (/) 1 data_one))
    -- putStrLn ("Foldr / Array2: " ++ show (foldr (/) 1 data_two) ++ "\n")
    -- putStrLn "Note that while the two foldl gave us the same answer, the foldr gave us two different ones"
    -- putStrLn "Another note is that in both cases we are using a static value to start instead of one from the array"
    -- putStrLn "Let us call those same functions again, but with the first/last item of the array as the starting point"
    -- putStrLn ("Foldl / Array1: " ++ show (foldl (/) (head data_one) (tail data_one)))
    -- putStrLn ("Foldl / Array2: " ++ show (foldl (/) (head data_two) (tail data_two)))
    -- putStrLn ("Foldr / Array1: " ++ show (foldr (/) (last data_one) (init data_one)))
    -- putStrLn ("Foldr / Array2: " ++ show (foldr (/) (last data_two) (init data_two)) ++ "\n")
    -- putStrLn "For our two foldr calls, we get teh same answer, as the first division was the last item divided by 1"
    -- putStrLn "But we get something different in the second foldl call"
    -- putStrLn "Note we are also getting the suggestion, use fold(l/r)1. This function takes natively the first or last item and uses it"
    -- putStrLn "But let's take a careful look at the type signatures of each, and see why we don't always want to follow that suggestion"
    -- putStrLn "Consider the insert function, which is am approximation of insertion sort"
    -- putStrLn "We can call it with foldr, but it will give us errors with foldr1"
    -- putStrLn ("Foldr insert Array2: " ++ show (foldr insert [] data_two))
    -- --putStrLn ("Foldr insert Array2: " ++ show (foldr1 insert data_two))

    -- putStrLn "The next set of functions we will be looking at is the scan family"
    -- putStrLn "These functions are very similar to fold, except that they produce a list result of each step"
    -- putStrLn "Scanl and Scanr of the two arrays with + and /"
    -- putStrLn ("Scanl + Array1: " ++ show (scanl (+) 0 data_one))
    -- putStrLn ("Scanl + Array2: " ++ show (scanl (+) 0 data_two))
    -- putStrLn ("Scanr + Array1: " ++ show (scanr (+) 0 data_one))
    -- putStrLn ("Scanr + Array2: " ++ show (scanr (+) 0 data_two) ++ "\n")
    -- putStrLn ("Scanl / Array1: " ++ show (scanl1 (/) data_one))
    -- putStrLn ("Scanl / Array2: " ++ show (scanl1 (/) data_two))
    -- putStrLn ("Scanr / Array1: " ++ show (scanr1 (/) data_one))
    -- putStrLn ("Scanr / Array2: " ++ show (scanr1 (/) data_two) ++ "\n")
    -- putStrLn "Let's look at the result of a call of max" -- Reminder that max works with two input elements and returns the greater
    -- putStrLn ("Scanl + Array1: " ++ show (scanl max 0 data_one))
    -- putStrLn ("Scanr + Array2: " ++ show (scanr max 0 data_two))

    -- putStrLn "\n\nThe final function we will look at is zip and zipWith"
    -- putStrLn "Both functions involve creation of a new array based on two inputs"
    -- putStrLn "ZipWith requires a function as input, and computers the result of all pairs from the same index"
    -- putStrLn "Zip creates an ordered pair at each index"
    -- putStrLn ("Zip with Array1 and Array2: " ++ show (zip data_one data_two))
    -- putStrLn ("Zip with different sized arrays: " ++ show (zip data_one [11,12,13,14,15]))
    -- putStrLn ("ZipWith max Array1 Array2: " ++ show (zipWith max data_one data_two))
