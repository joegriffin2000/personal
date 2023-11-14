addArrays :: [Int] -> [Int] -> [Int]
addArrays [] _          = []
addArrays _ []          = []
addArrays (x:xs) (y:ys) = (x + y) : (addArrays xs ys)

addArrays2 :: (Integral a, Integral b) => [a] -> [b] -> [a]
addArrays2 [] _          = []
addArrays2 _ []          = []
addArrays2 (x:xs) (y:ys) = ((fromIntegral x) + (fromIntegral y)) : (addArrays2 xs ys)

compareArrays :: Ord a => [a] -> [a] -> [Bool]
compareArrays [] [] = []
compareArrays (x:xs) (y:ys) = (x < y) : (compareArrays xs ys)

mapAdd :: [Int] -> [Int] -> [[Int]]
mapAdd [] _     = []
mapAdd (x:xs) y = (map (+x) y) : (mapAdd xs y)

testArray :: [Int] -> [Int]
testArray [] = []
testArray (x:xs) 
 | x < 0     = x^2 : testArray xs
 | x == 0    = (-1) : testArray xs
 | x > 0     = (x * 2) : testArray xs


quicksort :: Ord a => [a] -> [a]
quicksort []     = []
quicksort (p:xs) = (quicksort lesser) ++ [p] ++ (quicksort greater)
    where
        lesser  = filter (< p) xs
        greater = filter (>= p) xs

showArray :: [[Int]] -> [Char] -> IO()
showArray [] to_print = putStrLn to_print
showArray (x:xs) to_print = showArray (xs) (to_print ++ (show x) ++ "\n")

w :: [Int]
w = [6,3,2,5,8,6,1,2,8,4,3,2,9]
x = [1,6,3,1,7,0,6,3,1,2,4,3,8,4,2,5,10]
y :: [Int]
y = [7,2,7,3,1,4,6,9,7,5,3,10]
z = [7,4,2,5,4,1,3,5,7,9,0,10,2,1,8,3,4]
test :: [Int]
test = [(-2), 1, 3, 5, 0, (-9), 5, 7, (-7), 0, 14]


main = do
  print("In this program we will perform a variety of array functions!")
  --print(quicksort x)
  --print(quicksort y)
  print(addArrays x y)
  --print(addArrays2 x y)
  --print(compareArrays x y)
  --print(compareArrays x z)
  --print(mapAdd w y)
  --showArray (mapAdd w y) "The generated array is:\n"

