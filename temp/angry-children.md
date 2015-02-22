![HackerRank][HackerRank]
#Angry Children
[HackerRank \ Algorithms \ Warmup \ Angry Children ](https://www.hackerrank.com/challenges/angry-children)

None

##Problem Statement

Given a list of $N$ integers, your task is to select $K$ integers from the list such that its *unfairness* is minimized.

if $(x_1, x_2, x_3, \ldots, x_k)$ are $K$ numbers selected from the list $N$, the unfairness is defined as

$$max(x_1,x_2,\ldots, x_k) - min(x_1,x_2,\ldots, x_k)$$

where _max_ denotes the largest integer among the elements of $K$, and _min_ denotes the smallest integer among the elements of $K$.


**Input Format**

The first line contains an integer $N$.
The second line contains an integer $K$.
$N$ lines follow. Each line contains an integer that belongs to the list $N$.

**Note**


Integers in the list $N$ may not be unique.

**Output Format**

An integer that denotes the minimum possible value of _unfairness_.<br>

**Constraints**

$2 \le N \le 10^5$
$2 \le K \le N$
$0 \le integer~in~N~ \le 10^9$

**Sample Input #00**


    7
    3
    10
    100
    300
    200
    1000
    20
    30

**Sample Output #00**


    20

**Explanation #00**

Here $K = 3$, selecting the $3$ integers such that $K$ = $10,20,30$ candies. The unfairness is

    max(10,20,30) - min(10,20,30) = 30 - 10 = 20

**Sample Input #01**


    10
    4
    1
    2
    3
    4
    10
    20
    30
    40
    100
    200

**Sample Output #01**


    3

**Explanation #01**

Here $K = 4$, selecting the $4$ integers $1,2,3,4$. The unfairness is

    max(1,2,3,4) - min(1,2,3,4) = 4 - 1 = 3

**Sample Input #02**


    6
    3
    10
    20
    30
    100
    101
    102

**Sample Output #02**


    2

**Explanation #02**


Here $K = 3$, $3$ integers such that the difference between the maximum and the minimum is smallest is $100, 101, 102$

    max(100, 101, 102) - min(100, 101, 102) = 102 - 100 = 2

[HackerRank]:https://www.hackerrank.com/assets/brand/typemark_60x200.png