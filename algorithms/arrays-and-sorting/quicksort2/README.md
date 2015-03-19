![HackerRank]

#Quicksort 2 - Sorting

[HackerRank \ Algorithms \ Sorting \ Quicksort 2 - Sorting](https://www.hackerrank.com/challenges/quicksort2)

Write Quicksort itself.

##Problem Statement

In the previous challenge, you wrote a _partition_ method to split an array into two sub-arrays, one containing smaller elements and one containing larger elements than a given number. This means you 'sorted' half the array with respect to the other half. Can you repeatedly use _partition_ to sort an entire array?

###Guideline

In Insertion Sort, you simply went through each element in order and inserted it into a sorted sub-array. In this challenge, you cannot focus on one element at a time, but instead must deal with whole sub-arrays, with a strategy known as "divide and conquer".

When _partition_ is called on an array, two parts of the array get 'sorted' with respect to each other. If _partition_ is then called on each sub-array, the array will now be split into four parts. This process can be repeated until the sub-arrays are small. Notice that when  partition is called on just two numbers, they end up being sorted.

Can you repeatedly call partition so that the entire array ends up sorted?

**Print Sub-Arrays**

In this challenge, print your array every time your partitioning method finishes, i.e. whenever two subarrays, along with the pivot, is merged together.

- The first element in a sub-array should be used as a pivot.

- Partition the left side before partitioning the right side.

- The pivot should be placed between sub-arrays while merging them.

- Array of length ![$1$] or less will be considered sorted, and there is no need to sort or to print them.

###Input Format

There will be two lines of input:

 - ![$n$] - the size of the array

 - ![$ar$] - the *n* numbers of the array

###Output Format

Print every partitioned sub-array on a new line.

###Constraints

![$1 le n le 1000$]

![$-1000 le x le 1000, x ∈ ar$]

Each number is unique.

###Sample Input

    7
    5 8 1 3 7 9 2

###Sample Output

    2 3
    1 2 3
    7 8 9
    1 2 3 5 7 8 9

###Explanation

This is a diagram of Quicksort operating on the sample array:

![quick-sort diagram](https://s3.amazonaws.com/hr-challenge-images/quick-sort/QuickSort.png)

###Task

The method **quickSort** takes in a parameter, ![$ar$], an unsorted array. Use the Quicksort algorithm to sort the entire array.

[HackerRank]:https://www.hackerrank.com/assets/brand/typemark_60x200.png
[$1$]:../../../assets/034d0a6be0424bffe9a6e7ac9236c0f5.png
[$n$]:../../../assets/55a049b8f161ae7cfeb0197d75aff967.png
[$-1000 le x le 1000, x ∈ ar$]:../../../assets/0d33838ff42e329b55d13b0ebf003509.png
[$1 le n le 1000$]:../../../assets/a04ba05c8e489afc6d2bc03b751ad7ac.png
[$ar$]:../../../assets/9978ba2b8a2eb701a65496a8045523e2.png