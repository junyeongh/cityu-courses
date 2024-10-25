-- quicksort
quickSort :: (Ord a) => [a] -> [a]
quickSort [] = []
quickSort (x : xs) = quickSort ys ++ [x] ++ quickSort zs
  where
    ys = [a | a <- xs, a <= x]
    zs = [b | b <- xs, b > x]

-- merge two sorted lists
merge :: (Ord a) => [a] -> [a] -> [a]
merge [] ys = ys
merge xs [] = xs
merge (x : xs) (y : ys)
  | x <= y = x : merge xs (y : ys)
  | otherwise = y : merge (x : xs) ys

-- merge sort
mergeSort :: (Ord a) => [a] -> [a]
mergeSort [] = []
mergeSort [x] = [x]
mergeSort xs = merge (mergeSort left) (mergeSort right) -- partition
  where
    (left, right) = splitAt (length xs `div` 2) xs

main = do
  print $ quickSort [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
  print $ mergeSort [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
