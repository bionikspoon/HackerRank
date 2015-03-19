![HackerRank]

#Insertion Sort - Part 2

[HackerRank \ Algorithms \ Sorting \ Insertion Sort - Part 2](https://www.hackerrank.com/challenges/insertionsort2)

Code Insertion Sort itself.

##Problem Statement

In _Insertion Sort Part 1_, you sorted one element into an array. Using the same approach repeatedly, can you sort an entire unsorted array?

_Guideline:_ You already can place an element into a sorted array. How can you use that code to build up a sorted array, one element at a time? Note that in the first step, when you consider an element with just the first element - that is already "sorted" since there's nothing to its left that is smaller.

In this challenge, don't print every time you move an element. Instead, print the array every time an element is "inserted" into the array in (what is currently) its correct place. Since the array composed of just the first element is already "sorted", begin printing from the second element and on.

###Input Format

There will be two lines of input:

 - ![$s$] - the size of the array

 - ![$ar$] - a list of numbers that makes up the array

###Output Format

On each line, output the entire array at every iteration.

###Constraints

![$1 le s le 1000$]

![$-10000 le x le 10000,  x ∈ ar$]

###Sample Input

    6
    1 4 3 5 6 2


###Sample Output

    1 4 3 5 6 2
    1 3 4 5 6 2
    1 3 4 5 6 2
    1 3 4 5 6 2
    1 2 3 4 5 6


###Explanation

Insertion Sort checks ![$4$] first and doesn't need to move it, so it just prints out the array. Next, ![$3$] is inserted next to ![$1$], and the array is printed out. This continues one element at a time until the entire array is sorted.

###Task

The method **insertionSort** takes in one parameter: ![$ar$], an unsorted array. Use an Insertion Sort Algorithm to sort the entire array.

[HackerRank]:https://www.hackerrank.com/assets/brand/typemark_60x200.png
[$1 le s le 1000$]:../../../assets/2070d7a074f73f92fb797f0d3170afb7.png
[$4$]:../../../assets/ecf4fe2774fd9244b4fd56f7e76dc882.png
[$1$]:../../../assets/034d0a6be0424bffe9a6e7ac9236c0f5.png
[$-10000 le x le 10000,  x ∈ ar$]:../../../assets/e9474fcc2ead3ad8bff3d3092637b986.png
[$s$]:../../../assets/6f9bad7347b91ceebebd3ad7e6f6f2d1.png
[$3$]:../../../assets/5dc642f297e291cfdde8982599601d7e.png
[$ar$]:../../../assets/9978ba2b8a2eb701a65496a8045523e2.png