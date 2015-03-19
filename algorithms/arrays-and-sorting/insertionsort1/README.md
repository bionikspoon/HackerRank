![HackerRank]

#Insertion Sort - Part 1

[HackerRank \ Algorithms \ Sorting \ Insertion Sort - Part 1](https://www.hackerrank.com/challenges/insertionsort1)

Insert an element into a sorted array.

##Problem Statement

###Sorting

One common task for computers is to sort data. For example, people might want to see all their files on a computer sorted by size. Since sorting is a simple problem with many different possible solutions, it is often used to introduce the study of algorithms.

###Insertion Sort

These challenges will cover _Insertion Sort_, a simple and intuitive sorting algorithm. We will first start with an already sorted list.

###Insert element into sorted list

Given a sorted list with an unsorted number ![$V$] in the rightmost cell, can you write some simple code to _insert_ ![$V$] into the array so that it remains sorted?

Print the array every time a value is shifted in the array until the array is fully sorted. The goal of this challenge is to follow the correct order of insertion sort.

_Guideline:_ You can copy the value of ![$V$] to a variable and consider its cell "empty". Since this leaves an extra cell empty on the right, you can shift everything over until ![$V$] can be inserted. This will create a duplicate of each value, but when you reach the right spot, you can replace it with ![$V$].

###Input Format

There will be two lines of input:

 - ![$s$] - the size of the array

 - ![$ar$] - the sorted array of integers

###Output Format

On each line, output the entire array every time an item is shifted in it.

###Constraints

![$1 le s  le 1000$]

![$-10000 le V le 10000, V ∈ ar$]

###Sample Input

    5
    2 4 6 8 3

###Sample Output

    2 4 6 8 8
    2 4 6 6 8
    2 4 4 6 8
    2 3 4 6 8

###Explanation

![$3$] is removed from the end of the array.<br/>

In the ![$1$]<sup>st</sup> line ![$8 > 3$], so ![$8$] is shifted one cell to the right. <br/>

In the ![$2$]<sup>nd</sup> line ![$6 > 3$], so ![$6$] is shifted one cell to the right. <br/>

In the ![$3$]<sup>rd</sup> line ![$4 > 3$], so ![$4$] is shifted one cell to the right. <br/>

In the ![$4$]<sup>th</sup> line ![$2 < 3$], so ![$3$] is placed at position ![$2$].

###Task

Complete the method <i>insertionSort</i> which takes in one parameter:

- ![$ar$] - an array with the value ![$V$] in the right-most cell.


###Next Challenge

In the [next Challenge](https://www.hackerrank.com/challenges/insertionsort2), we will complete the insertion sort itself!

[HackerRank]:https://www.hackerrank.com/assets/brand/typemark_60x200.png
[$2 < 3$]:../../../assets/31b7da964c9a032096e56f6bc31a3056.png
[$4$]:../../../assets/ecf4fe2774fd9244b4fd56f7e76dc882.png
[$1 le s  le 1000$]:../../../assets/f96a07606d21bb781ea7c745f14bb330.png
[$V$]:../../../assets/a9a3a4a202d80326bda413b5562d5cd1.png
[$4 > 3$]:../../../assets/fd373c293836a8cbf209b84031859ffe.png
[$2$]:../../../assets/76c5792347bb90ef71cfbace628572cf.png
[$1$]:../../../assets/034d0a6be0424bffe9a6e7ac9236c0f5.png
[$6 > 3$]:../../../assets/68c65047570bb09c4ff6899653a93e80.png
[$6$]:../../../assets/327c36301dc71617dc7032f8ce30b236.png
[$8 > 3$]:../../../assets/e343096361c18d2989f000ad0a1d1fe6.png
[$-10000 le V le 10000, V ∈ ar$]:../../../assets/5ab6a23b4dbac71bee6df5895d88a91e.png
[$s$]:../../../assets/6f9bad7347b91ceebebd3ad7e6f6f2d1.png
[$8$]:../../../assets/005c128d6e551735fa5d938e44e7a613.png
[$3$]:../../../assets/5dc642f297e291cfdde8982599601d7e.png
[$ar$]:../../../assets/9978ba2b8a2eb701a65496a8045523e2.png