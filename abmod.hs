import Data.Maybe as Maybe
import Data.List as List

f n a b= take n li
        where li = [a,b] ++ [let x = li !! (i-1)
                                 y = li !! (i-2) 
                                 in (x*y) `mod` (x+y+1) | i <-[2..]]
                                 
f200 = f 200
myf a= f200 a a

cycled li = foldl1 (||) [cycleLength n li| n <- [2..length li]]
    where cycleLength n li = foldl (||) (False) [li!!m == li!!(m+n)| m <- [0..length li-n-1]]

l2 = filter (not . cycled) [f 100 a b | a <- [1..200], b <- [1..200]]
          
fmax a= if cycled l then Just (maximum l) else Nothing
    where l = f 1000 a a

maxlist = [(a,fmax a) | a <- [1..1000]]

sortWithNothing a b
  | snd a == Nothing && snd b == Nothing = EQ
  | snd a == Nothing = GT
  | snd b == Nothing = LT
  | otherwise = compare x y
      where x = (fromIntegral(Maybe.fromJust(snd a))) / (fromIntegral(fst a))
            y = (fromIntegral(Maybe.fromJust(snd b))) / (fromIntegral(fst b))
  
sortedMaxList = List.sortBy sortWithNothing maxlist