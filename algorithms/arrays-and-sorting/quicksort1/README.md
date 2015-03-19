![HackerRank]

#Quicksort 1 - Partition

[HackerRank \ Algorithms \ Sorting \ Quicksort 1 - Partition](https://www.hackerrank.com/challenges/quicksort1)

Simply partition an array, the first step of QuickSort.

##Problem Statement

The previous challenges covered _Insertion Sort_, which is a simple and intuitive sorting algorithm. Insertion Sort has a running time of ![$O(N$]<sup>![$2$]</sup>) which isn't fast enough for most purposes. Instead, sorting in the real world is done with faster algorithms like Quicksort, which will be covered in the challenges that follow.

The first step of Quicksort is to _partition_ an array into two smaller arrays.

###Challenge

You're given an array ![$ar$] and a number ![$p$]. Partition the array, so that all elements greater than ![$p$] are to its right, and all elements smaller than ![$p$] are to its left.

In the new sub-array, the relative positioning of elements should remain the same, i.e. if ![$n$]<sub>![$1$]</sub> was before ![$n$]<sub>![$2$]</sub> in the original array, it must remain so in the sub-array, as well. The only situation where this does not hold good is when ![$p$] lies between ![$n$]<sub>![$1$]</sub> and ![$n$]<sub>![$2$]</sub>.

I.e. ![$n$]<sub>![$1$]</sub> ![$gt p gt n$]<sub>![$2$]</sub>

*Guideline* - In this challenge, you do not need to move around the numbers 'in-place'. This means you can create two lists and combine them at the end.

###Input Format

 You will be given an array of integers. The number ![$p$] is the first element in ![$ar$].

 There are two lines of input:

- ![$n$] - the number of elements in the array ![$ar$]

- the ![$n$] elements of ![$ar$] (including ![$p$] at the beginning)

###Output Format

Print out the numbers of the partitioned array on one line.

###Constraints

- ![$1 le n le 1000$]

- ![$-1000 le x le 1000, x ∈ ar$]

- All elements will be unique.

###Sample Input

    5
    4 5 3 7 2

###Sample Output

    3 2 4 5 7

###Explanation

![$p$] equals _4_. _5_ is moved to the right of _4_, _2_ ix moved to the left of _4_, and _3_ is also moved to the left of _4_. The numbers otherwise remain in the same order.

###Task

Complete the method partition which takes an array ![$ar$]. The first element in ![$ar$] is the number ![$p$].

[HackerRank]:https://www.hackerrank.com/assets/brand/typemark_60x200.png
[$n$]:../../../assets/55a049b8f161ae7cfeb0197d75aff967.png
[$-1000 le x le 1000, x ∈ ar$]:../../../assets/0d33838ff42e329b55d13b0ebf003509.png
[$O(N$]:../../../assets/1649d8f73b71df7e4822e1462c517e8c.png
[$1$]:../../../assets/034d0a6be0424bffe9a6e7ac9236c0f5.png
[$p$]:../../../assets/2ec6e630f199f589a2402fdf3e0289d5.png
[$gt p gt n$]:../../../assets/252b21a78ca5a0565c6744b618d9770b.png
[$1 le n le 1000$]:../../../assets/a04ba05c8e489afc6d2bc03b751ad7ac.png
[$2$]:../../../assets/76c5792347bb90ef71cfbace628572cf.png
[$ar$]:../../../assets/9978ba2b8a2eb701a65496a8045523e2.png