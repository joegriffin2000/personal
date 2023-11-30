{--
Joe Griffin
Haskell_In_Class_Two_Joe_Griffin.hs

This is my haskell in-class 2

Note: There were two functions which I got varying levels of assistnace from Replit AI but other than that the code written is mine.
--}

import Data.Function
import Data.List

-- Arithmetic operators

data Op = Add | Sub | Mul | Div

-- Defines the show function for Op datatype
instance Show Op where
  show Add = "+"
  show Sub = "-"
  show Mul = "*"
  show Div = "/"

-- A method to determine if an Arithmetic operation is valid
-- All multiplication and addition are valid.
-- Subtraction is valid only if x > y
-- Division is only valid if it is a clean division
valid :: Op -> Int -> Int -> Bool
valid Add _ _ = True
valid Sub x y = x > y
valid Mul _ _ = True
valid Div x y = x `mod` y == 0

-- Applies the stated op to two input Ints
apply :: Op -> Int -> Int -> Int
apply Add x y = x + y
apply Sub x y = x - y
apply Mul x y = x * y
apply Div x y = x `div` y

-- Numeric expressions datatype

data Expr = Val Int | App Op Expr Expr

-- Properly places parentheses during Show using inline function definition for brak
instance Show Expr where
  show (Val n) = show n
  show (App o l r) = brak l ++ show o ++ brak r
    where
      brak (Val n) = show n
      brak e = "(" ++ show e ++ ")"

-- Extracts the individual numbers from the expression datapoint
values :: Expr -> [Int]
values (Val n) = [n]
values (App _ l r) = values l ++ values r

-- Compresses the expression to a single value
-- Does this have to be an [Int] array of size one? Or can we have it return an int?
eval :: Expr -> [Int]
eval (Val n) = [n | n > 0]
eval (App o l r) =
  [ apply o x y | x <- eval l, y <- eval r, valid o x y
  ]

x :: Expr
x = App Div (App Mul (Val 3) (Val 7)) (App Add (App Sub (Val 5) (Val 4)) (App Add (Val 2) (Val 4)))

y :: Expr
y = App Mul (App Add (Val 4) (Val 10)) (App Sub (App Div (Val 14) (Val 2)) (App Mul (Val 2) (Val 2)))

z :: Expr
z = App Sub (App Div (App Mul (Val 6) (App Add (Val 5) (App Sub (Val 9) (Val 4)))) (App Add (Val 3) (Val 2))) (App Mul (Val 3) (App Sub (App Div (Val 18) (Val 9)) (Val 1)))

a :: Expr
a = App Add (Val 1) (Val 2)

b :: Expr
b = App Add (Val 1) (Val 6)

d = [x, y, z, a, b]

{--
Add definitions for Eq and Ord to Expr. What should we use to compare different Expr datapoints?
Add a function that takes in two Expr datapoints and an Op, and returns a new Expr
Add a function that will invert an Expr. An inverted Expr will flip Add <-> Sub and Mul <-> Div, as well as the left and right hand sides (5+3 becomes 3-5). If an Expr is complex, such as (3*7) / ((5-4) + (4+2)), we will invert the nested Expr as well. The prior Expr will give us ((2-4) - (4+5)) * (7/3). (This may make an Expr datapoint invalid according to our rules in apply)
Add a function that will simplify an Expr down to two terms. The Expr  (3*7) / ((5-4) + (4+2)) will be condensed to 21/7.
Add a function that will take in an array of Expr datapoints, call the function defined in IV on all Expr within, and then return the most common number within the array. If we have a (simplified) array of [21/3. 14*3. 9/3, 7-4] the result returned back will be 3
--}

-- part 1: Eq and Ord

-- Replit AI helped me to construct this defintion specifically
instance Eq Expr where
  (Val x) == (Val y) = x == y
  (App op1 l1 r1) == (App op2 l2 r2) = (show op1 == show op2) && (l1 == l2) && (r1 == r2)
  _ == _ = False

instance Ord Expr where
  compare (Val x) (Val y) = compare x y
  compare (App op1 l1 r1) (App op2 l2 r2) = compare (eval (App op1 l1 r1)) (eval (App op2 l2 r2))
  compare (App op1 l1 r1) (Val y) = compare xhead y where xhead = head (eval (App op1 l1 r1))
  compare (Val x) (App op2 l2 r2) = compare x yhead where yhead = head (eval (App op2 l2 r2))

-- part 2: Create
create :: Expr -> Expr -> Op -> Expr
create l1 l2 op = (App op l1 l2)

-- part 3: Invert
invert :: Expr -> Expr
invert (Val i) = Val i
invert (App Add a b) = App Sub (invert b) (invert a)
invert (App Sub a b) = App Add (invert b) (invert a)
invert (App Mul a b) = App Div (invert b) (invert a)
invert (App Div a b) = App Mul (invert b) (invert a)

-- part 4: Simplify
simplify :: Expr -> Expr
simplify (Val i) = Val i
simplify (App Add a b) = App Add (Val (head (eval a))) (Val (head (eval b)))
simplify (App Sub a b) = App Sub (Val (head (eval a))) (Val (head (eval b)))
simplify (App Mul a b) = App Mul (Val (head (eval a))) (Val (head (eval b)))
simplify (App Div a b) = App Div (Val (head (eval a))) (Val (head (eval b)))

-- part 5: mostCommonEval
mostCommonEval :: [Expr] -> Int
mostCommonEval [] = 0
mostCommonEval (x) = mode (evalAll x)

evalAll :: [Expr] -> [Int]
evalAll [] = []
evalAll (x : xs) = head (eval x) : evalAll xs

-- Replit AI also helped me to construct this defintion specifically
-- Replit AI also helped me to construct this defintion specifically 
mode :: Ord a => [a] -> a
mode = head . maximumBy (compare `on` length) . group . sort

main = do
  print (x)
  print (y)
  print (z)
  print (a)
  print (eval x)
  print (eval y)
  print (eval z)
  print (eval a)
  {--My testing starts here--}
  putStrLn "______"
  print (simplify x)
  print (evalAll d)
  print (mostCommonEval d)