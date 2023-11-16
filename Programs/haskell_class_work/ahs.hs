import Data.Bits (toIntegralSized)
import Data.Fixed (div')
import Distribution.Simple.Utils (xargs)

{--This converts an Int Array to a set--}
{--____________________________________________________--}
intArrayToSet :: [Int] -> [Int]
intArrayToSet [] = []
intArrayToSet (head:tail) 
 | elem head tail = (intArrayToSet tail)
 | otherwise = head : (intArrayToSet tail)
{--____________________________________________________--}

{--This does set union--}
{--____________________________________________________--}
unionMain :: [Int] -> [Int] -> [Int]
unionMain arr1 arr2  = setUnion (intArrayToSet arr1) (intArrayToSet arr2) 

setUnion :: [Int] -> [Int] -> [Int]
setUnion arr1 []          = arr1
setUnion [] arr2          = arr2
setUnion arr1 (head2:tail2) 
 | elem head2 arr1 = (setUnion arr1 tail2)
 | otherwise = head2 : (setUnion arr1 tail2)
{--____________________________________________________--}

{--This does set intersection--}
{--____________________________________________________--}
intersectionMain :: [Int] -> [Int] -> [Int]
intersectionMain arr1 arr2  = setIntersection (intArrayToSet arr1) (intArrayToSet arr2) 

setIntersection :: [Int] -> [Int] -> [Int]
setIntersection arr1 []          = []
setIntersection [] arr2          = []
setIntersection arr1 (head2:tail2) 
 | not (elem head2 arr1) = (setIntersection arr1 tail2)
 | otherwise = head2 : (setIntersection arr1 tail2)
{--____________________________________________________--}


{--This takes the average of many different arrays and then returns the largest--}
{--____________________________________________________--}
chooseMaxAvg :: (Integral a) => [[a]] -> a
chooseMaxAvg [] = 0
chooseMaxAvg x = maximum (avgArrays x)

avgArrays :: (Integral a) => [[a]]  -> [a]
avgArrays []          = []
avgArrays (x:xs) = div (sumArray x) (fromIntegral (length x)) : (avgArrays xs)

sumArray :: (Integral a) => [a] -> a
sumArray [head] = head
sumArray (head:tail) = head + (sumArray tail)

{--____________________________________________________--}

main :: IO() = do
    let x = [1,1,1,2,6,55,155]
    print(intArrayToSet x)
    let y = [2,2,3,6,10]
    print(intArrayToSet y)

    print(unionMain x y)
    print(intersectionMain x y)

    let w = [[1,2,3],[4,5,6],[7,8,9]]

    putStrLn("")
    print(chooseMaxAvg w)