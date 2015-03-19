![HackerRank]

#Solve me second

[HackerRank \ Algorithms \ Warmup \ Solve me second](https://www.hackerrank.com/challenges/solve-me-second)

Solve me second

##Problem Statement

You learnt about `STDIN` and `STDOUT` in [Solve me first](https://www.hackerrank.com/challenges/solve-me-first).

This is the second challenge in the introduction series. The purpose of this challenge is to give you a working I/O template in your preferred language. It includes scanning two space-separated integers from `STDIN` in a loop over ![$T$] lines, calling a function, returning a value, and printing it to `STDOUT`.

A pseudo code looks like the following:

    read T
    loop from 1 to T
        read A and B
        compute the sum
        print value in a newline
    end loop


The task is to scan two numbers from `STDIN`, and print the sum ![$A+B$] on `STDOUT`. The code has already been provided for most of the popular languages. This is primarily for you to read and inspect how the IO is handled.

**Note**: The code has been saved in a template, which you can submit if you want. Or, you may try rewriting it and building it up from scratch.

###Input Format

_(This section specifies the Input Format.)_

The first line contains ![$T$] (number of test cases) followed by ![$T$] lines

Each line contains ![$A$] and ![$B$], separated by a space.

As you can see that we have provided in advance the number of lines, we discourage the use of scanning till `EOF` as not every language has an easy way to handle that. In fact, every HackerRank challenge is designed in such a way that multitests begin with a ![$T$] line to indicate the number of lines.

###Output Format

_(This section specifies the Output Format.)_

An integer that denotes Sum ![$(A + B)$] printed on new line for every testcase.

###Constraints

_(This section tells what input you can expect. You can freely assume that the input will remain within the boundaries specified.)_

![$1 le T, A, B le 1000$]

###Sample Input

    2
    2 3
    3 7

###Sample Output

    5
    10

The above sample should be taken seriously. The input will be of _2_ lines and your test cases are _2_, _3_ and _3_, _7_ in two separate lines. Your output should be _5_ and _10_ printed on two separate lines. If you print extra lines or _"The answer is: 5"_, any such extra characters in output will result in a Wrong Answer, as the judging is done using diff checker.

[HackerRank]:https://www.hackerrank.com/assets/brand/typemark_60x200.png
[$A$]:../../../assets/53d147e7f3fe6e47ee05b88b166bd3f6.png
[$(A + B)$]:../../../assets/da8ce10f2d7dd5454fd614424dc2109d.png
[$B$]:../../../assets/61e84f854bc6258d4108d08d4c4a0852.png
[$T$]:../../../assets/2f118ee06d05f3c2d98361d9c30e38ce.png
[$A+B$]:../../../assets/a181ec999734dbca1a01f9781df15a09.png
[$1 le T, A, B le 1000$]:../../../assets/65dcf4faf0d42c57be40b0d6cba3abf1.png