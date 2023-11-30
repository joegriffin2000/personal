{-
   Dr Michaels
   intro_fcs.hs
   This file contains several functions which are first class functions 
   This means that the functions are those which take one or more other functions
   in as input. We can tell in Haskell when a function is expected to be the input
   when we see two or more parameters together with parenthesis. 
-}

{- Create a function that will take as input 
   an array of Ints and a function that transforms
   an int, and directly applies that function to 
   all members of the input array
   NOTE: While a call to map will work here, that
   is not our goal.-}
transformInt :: (Int -> Int) -> [Int] -> [Int]
transformInt _ [] = []
transformInt f (x:xs) = f x : transformInt f xs

{- Create a function similar to the above,
   however this time it will take a generic type
   and return another generic type-}
transformArray :: (a -> b) -> [a] -> [b]
transformArray _ [] = []
transformArray f (x:xs) = f x : transformArray f xs


{- The above functions apply a single function 
   each item of the array, similar to a map.
   Let us now apply a function to an array
   that will condense it to a single value.
   This is similar to reduce in Python, and fold
   in Haskell.
   Go here: https://wiki.haskell.org/Fold for 
   more information on the fold function in Haskell-}
condenseInt :: (Int -> Int -> Int) -> [Int] -> Int
condenseInt _ [] = -9999999
condenseInt _ [x] = x
condenseInt f (x:y:xs) = condenseInt f (f x y:xs)

{- Genericizing the above follows a similar route
   to our map function. Consideration must be
   given to ensure that a proper function is
   generated and placed within. -}

{- Create a function that will take in an 
   generic function, two generic arrays, and 
   return a singular array of the type specified 
   by the function. Apply the function to each 
   pair A[i] B[i] to generate the return array-}
functionFour :: (a -> a -> b) -> [a] -> [a] -> [b]
functionFour _ [] _ = []
functionFour _ _ [] = []
functionFour f (x:xs) (y:ys) = f x y : functionFour f xs ys



test_data = [1,2,3,4,5]

main :: IO ()
main = do
  print "Time for the second inclass!"
  print (transformInt (+3) [1,2,3,4,5])
  print (transformArray (+3.5) test_data)
  print (transformArray (+3.5) [1.3,2.4,3.5,4,5])
  print (transformArray (3<) [1,2,3,4,5])
  print (condenseInt (+) [1,2,3,4,5])
  print (condenseInt (^) [2,3,4,5])
  print (functionFour (+) [1,2,3,4,5] [5,4,3,2,1])
