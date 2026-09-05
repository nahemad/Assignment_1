# CMPS 2200 Assignment 01
## Answers

**Name:** Nahema Dumontei


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation** #on paper/separate pdf

  - 1b (2 pts): 
 on separate paper/pdf
  - 1c (2 pts): 
//
  - 1d (2 pts):
//
  - 1e (2 pts):
//
  - 1f (2 pts):
//
  - 1g (2 pts):
//
2. **SPARC to Python**

  - 2b (3 pts): 

  This function calculates the Fibonacci sequence. The input x represents the index f(x). It calculates the number at index x by adding the two previous numbers. However, to get those previous numbers, it has to go all the way back to the base cases where x=1 or x=0 working its way back up to the inputted x by calculating the values. 

3. **Parallelism and recursion**

  - 3b (4 pts):

  Since the longest_run is a iterative and sequential function using a single for loop, there is no parallelism. Because of this, its Work and Span are mathematically the same. 

  Work would be $\Theta$(n) because it iterates throught the whole list exaclty once, that has n items in it. 

  Span would be the execution time if we had infinite processors. In this function, since every iteration of the loop depends on the previous one (because it accumulates current_sequence and max) then these iterations can't run at the same time. Since operations happen one after the other, the Span is still the lenght of the list $\Theta$(n) 

  - 3d (4 pts): 
  
  The work would be $\Theta$(n) again, because there are still n elements in the list that are being checked. Even though it is being splitted, at the end each split contains 1 number and performs 1 operation, so for n elements, it is $\Theta$(n)

  The Span would be the execution time if we had infinite processors, so once its split in half, these halves can run in parallel at the same time, and the halfs of the halfs can also run in parallel. The span tracks the height of the binary recursion tree (the longest single path). If we visualize the tree, and determine the cost of each level (something like S(n) = S(n/2) +c) we can derive the Span which turns out to be $\Theta$(log(n))
  If the Span is ran sequentially then it would be $\Theta$(n) because one half would have to wait for the other hald to go. 

  - 3e (5 pts):

  The work would still be $\Theta$(n), because the work calculates the total number of operartions that happen across all threads combined, and that stays the same as before (3d)
  Now, the Span, if it does run in parallel then we would get the $\Theta$(log(n)) because we would only be calculating the longest "one way/ single path" from top to bottom of the tree, since all the divisions would be running in their own thread at the same time. 