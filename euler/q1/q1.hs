divisible_by_3_or_5 :: Int -> Bool
divisible_by_3_or_5 x = x `mod` 3 == 0 || x `mod` 5 == 0

sum_divisible_by_3_or_5 :: Int -> Int
sum_divisible_by_3_or_5 n = sum [x | x <- [1..n-1], divisible_by_3_or_5 x]

main :: IO ()
main = putStrLn ("The sum of numbers from 0 to 1000: " ++ show (sum_divisible_by_3_or_5 1000))