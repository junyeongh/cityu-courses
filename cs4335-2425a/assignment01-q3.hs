-- Function to find the maximum difference
findMaxDifference :: [Int] -> Int
findMaxDifference arr = maxDifferenceHelper arr 0 (length arr - 1)

-- Helper function to recursively find the maximum difference
maxDifferenceHelper :: [Int] -> Int -> Int -> Int
maxDifferenceHelper arr left right
  | right - left == 1 = arr !! right - arr !! left
  | otherwise = maximum [leftDiff, rightDiff, crossDiff]
  where
    mid = (left + right) `div` 2
    leftDiff = maxDifferenceHelper arr left mid
    rightDiff = maxDifferenceHelper arr (mid + 1) right
    minLeft = minimum (take (mid - left + 1) (drop left arr))
    maxRight = maximum (take (right - mid) (drop (mid + 1) arr))
    crossDiff = maxRight - minLeft

-- Example usage
main :: IO ()
main = do
  let x = [22, 5, 8, 10, -3, 1]
  print $ findMaxDifference x  -- Output: 5