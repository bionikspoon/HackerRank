![HackerRank]

#Correctness and the Loop Invariant

[HackerRank \ Algorithms \ Sorting \ Correctness and the Loop Invariant](https://www.hackerrank.com/challenges/correctness-invariant)

How do you demonstrate the correctness of an algorithm? You can use the loop invariant.

##Problem Statement

In the previous challenge, you wrote code to perform an _Insertion Sort_ on an unsorted array. But how would you prove that the code is correct? I.e. how do you show that for any input your code will provide the right output?

###Loop Invariant

In computer science, you could prove it formally with a _loop invariant_, where you state that a desired property is maintained in your loop. Such a proof is broken down into the following parts:

 - _Initialization_: It is true (in a limited sense) before the loop runs.

 - _Maintenance_: If it's true before an iteration of a loop, it remains true before the next iteration.

 - _Termination_: It will terminate in a useful way once it is finished.

**Insertion Sort's Invariant**

Say, you have some InsertionSort code, where the outer loop goes through the whole array ![$A$]:

    for(int i = 1; i < A.length; i++){
    //insertion sort code

You could then state the following loop invariant:

> At the start of every iteration of the outer loop (indexed with ![$i$]), the subarray until ![$ari$] consists of the original elements that were there, but in sorted order.

To prove Insertion Sort is correct, you will then demonstrate it for the three stages:

- _Initialization_ - The subarray starts with the first element of the array, and it is (obviously) sorted to begin with.

- _Maintenance_ - Each iteration of the loop expands the subarray, but keeps the sorted property. An element ![$V$]  gets inserted into the array only when it is greater than the element to its left. Since the elements to its left have already been sorted, it means ![$V$] is greater than all the elements to its left, so the array remains sorted. (In _Insertion Sort 2_ we saw this by printingthe array each time an element was properly inserted.)

- _Termination_ - The code will terminate after ![$i$] has reached the last element in the array, which means the sorted subarray has expanded to encompass the entire array. The array is now fully sorted.

![Loop Invariant Chart](https://s3.amazonaws.com/hr-challenge-images/insertion-sort/InsertionSortCorrect-small.png)

You can often use a similar process to demonstrate the correctness of many algorithms. You can see [these notes](http://www.cs.uofs.edu/~mccloske/courses/cmps144/invariants_lec.html) for more information.

###Challenge

In the InsertionSort code below, there is an error. Can you fix it? Print the array only once, when it is fully sorted.

###Details

The Input format and the constraints are the same as in the previous challenges and are presented below.

<hr>

###Input Format

There will be two lines of input:

 - ![$s$] - the size of the array

 - ![$ar$] - the list of numbers that makes up the array

###Output Format

Output the numbers in order, space-separated.

###Constraints

![$1 le s le 1000$]

![$-1500 le V le 1500, V ∈ ar$]

###Sample Input

<pre>

6

1 4 3 5 6 2

</pre>

###Sample Output

<pre>

1 2 3 4 5 6

</pre>

[HackerRank]:https://www.hackerrank.com/assets/brand/typemark_60x200.png
[$A$]:../../../assets/53d147e7f3fe6e47ee05b88b166bd3f6.png
[$ari$]:../../../assets/6fc9da1442be04032d5171209f031c7b.png
[$i$]:../../../assets/77a3b857d53fb44e33b53e4c8b68351a.png
[$V$]:../../../assets/a9a3a4a202d80326bda413b5562d5cd1.png
[$1 le s le 1000$]:../../../assets/2070d7a074f73f92fb797f0d3170afb7.png
[$s$]:../../../assets/6f9bad7347b91ceebebd3ad7e6f6f2d1.png
[$-1500 le V le 1500, V ∈ ar$]:../../../assets/428ac3008c2166c082d5a4127b3ac8dd.png
[$ar$]:../../../assets/9978ba2b8a2eb701a65496a8045523e2.png