![HackerRank](https://www.hackerrank.com/assets/brand/typemark_60x200.png)
#Sherlock and Queries#
[HackerRank \ Algorithms \ Implementation \ Sherlock and Queries](https://www.hackerrank.com/challenges/sherlock-and-queries)

Help Sherlock in answering Queries

##Problem Statement##

Watson gives to Sherlock an array: ![$A_1, A_2, \cdots, A_N$](https://raw.githubusercontent.com/bionikspoon/HackerRank/master/assets/c3f4413a12dd68a3f0999d8c67f58f0e.png). He also gives to Sherlock two other arrays: ![$B_1, B_2, \cdots, B_M$](https://raw.githubusercontent.com/bionikspoon/HackerRank/master/assets/931a66e3d5b402ced398785c46df78e4.png) and ![$C_1, C_2, \cdots, C_M$](https://raw.githubusercontent.com/bionikspoon/HackerRank/master/assets/8a695951a4f2c018cdea907c2aef0ee3.png).
Then Watson asks Sherlock to perform the following program:

    for i = 1 to M do
        for j = 1 to N do
            if j % B[i] == 0 then
                A[j] = A[j] * C[i]
            endif
        end do
    end do

Can you help Sherlock and tell him the resulting array ![$A$](https://raw.githubusercontent.com/bionikspoon/HackerRank/master/assets/53d147e7f3fe6e47ee05b88b166bd3f6.png)? You should print all the array elements modulo ![$(10^9 + 7)$](https://raw.githubusercontent.com/bionikspoon/HackerRank/master/assets/c4e61dbf8b36a31aa53c4e418152f3d2.png).

###Input Format###

The first line contains two integer numbers ![$N$](https://raw.githubusercontent.com/bionikspoon/HackerRank/master/assets/f9c4988898e7f532b9f826a75014ed3c.png) and ![$M$](https://raw.githubusercontent.com/bionikspoon/HackerRank/master/assets/fb97d38bcc19230b0acd442e17db879c.png). The next line contains ![$N$](https://raw.githubusercontent.com/bionikspoon/HackerRank/master/assets/f9c4988898e7f532b9f826a75014ed3c.png) integers, the elements of array ![$A$](https://raw.githubusercontent.com/bionikspoon/HackerRank/master/assets/53d147e7f3fe6e47ee05b88b166bd3f6.png). The next two lines contains ![$M$](https://raw.githubusercontent.com/bionikspoon/HackerRank/master/assets/fb97d38bcc19230b0acd442e17db879c.png) integers each, the elements of array ![$B$](https://raw.githubusercontent.com/bionikspoon/HackerRank/master/assets/61e84f854bc6258d4108d08d4c4a0852.png) and ![$C$](https://raw.githubusercontent.com/bionikspoon/HackerRank/master/assets/9b325b9e31e85137d1de765f43c0f8bc.png).

###Output Format###

Print ![$N$](https://raw.githubusercontent.com/bionikspoon/HackerRank/master/assets/f9c4988898e7f532b9f826a75014ed3c.png) integers, the elements of array ![$A$](https://raw.githubusercontent.com/bionikspoon/HackerRank/master/assets/53d147e7f3fe6e47ee05b88b166bd3f6.png) after performing the program modulo ![$(10^9 + 7)$](https://raw.githubusercontent.com/bionikspoon/HackerRank/master/assets/c4e61dbf8b36a31aa53c4e418152f3d2.png).

###Constraints###

![$1 \le N, M \le 10^5$](https://raw.githubusercontent.com/bionikspoon/HackerRank/master/assets/404294123ec13c62c8a0b390d4e8f6ee.png)

![$1 \le B[i] \le N$](https://raw.githubusercontent.com/bionikspoon/HackerRank/master/assets/ef9ba375db3112e1c88aa798dd3522c4.png)

![$1 \le A[i], C[i] \le 10^5$](https://raw.githubusercontent.com/bionikspoon/HackerRank/master/assets/d133006232caf463e513a0ef1f36103c.png)

###Sample Input###


	4 3
	1 2 3 4
	1 2 3
	13 29 71

###Sample Output###


	13 754 2769 1508	
