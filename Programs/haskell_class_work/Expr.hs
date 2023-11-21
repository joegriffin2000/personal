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
   show (Val n)     = show n
   show (App o l r) = brak l ++ show o ++ brak r
                      where
                         brak (Val n) = show n
                         brak e       = "(" ++ show e ++ ")"

-- Extracts the individual numbers from the expression datapoint
values :: Expr -> [Int]
values (Val n)     = [n]
values (App _ l r) = values l ++ values r

-- Compresses the expression to a single value 
-- Does this have to be an [Int] array of size one? Or can we have it return an int?
eval :: Expr -> [Int]
eval (Val n)     = [n | n > 0]
eval (App o l r) = [apply o x y | x <- eval l,
                                  y <- eval r,
                                  valid o x y]


x :: Expr 
x = App Div (App Mul (Val 3) (Val 7)) (App Add (App Sub (Val 5) (Val 4)) (App Add (Val 2) (Val 4)))
y :: Expr
y = App Mul (App Add (Val 4) (Val 10)) (App Sub (App Div (Val 14) (Val 2)) (App Mul (Val 2) (Val 2)))
z :: Expr
z = App Sub (App Div (App Mul (Val 6) (App Add (Val 5) (App Sub (Val 9) (Val 4)))) (App Add (Val 3) (Val 2))) (App Mul (Val 3) (App Sub (App Div (Val 18) (Val 9)) (Val 1)))
a :: Expr 
a = App Add (Val 1) (Val 2) 

main = do 
 print(x)
 print(y)
 print(z)
 print(a)
 print(eval x)
 print(eval y)
 print(eval z)
 print(eval a)