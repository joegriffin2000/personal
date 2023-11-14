{--This converts an Int Array to a set--}
intArrayToSet :: [Int] -> [Int]
intArrayToSet [] = []
intArrayToSet (head:tail) 
 | elem head tail = (intArrayToSet tail)
 | otherwise = head : (intArrayToSet tail)

unionMain :: [Int] -> [Int] -> [Int]
unionMain arr1 arr2  = setUnion (intArrayToSet arr1) (intArrayToSet arr2) 

setUnion :: [Int] -> [Int] -> [Int]
setUnion arr1 []          = arr1
setUnion [] arr2          = arr2
setUnion arr1 (head2:tail2) 
 | elem head2 arr1 = (setUnion arr1 tail2)
 | otherwise = head2 : (setUnion arr1 tail2)

intersectionMain :: [Int] -> [Int] -> [Int]
intersectionMain arr1 arr2  = setIntersection (intArrayToSet arr1) (intArrayToSet arr2) 

setIntersection :: [Int] -> [Int] -> [Int]
setIntersection arr1 []          = []
setIntersection [] arr2          = []
setIntersection arr1 (head2:tail2) 
 | not (elem head2 arr1) = (setIntersection arr1 tail2)
 | otherwise = head2 : (setIntersection arr1 tail2)


{--FINISH THIS RN--}
addArrays2 :: (Integral a) => [[a]]  -> [a]
addArrays2 []          = []
addArrays2 (x:xs) = ((fromIntegral x) + (fromIntegral y)) : (addArrays2 xs ys)



main :: IO() = do
    let x = [1,1,1,2,6,55,155]
    print(intArrayToSet x)
    let y = [2,2,3,6,10]
    print(intArrayToSet y)

    print(unionMain x y)
    print(intersectionMain x y)