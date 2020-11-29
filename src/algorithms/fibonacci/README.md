# Fibonacci Numbers

Fibonacci numbers are a mathematical sequence defined by the simple formula:

<!-- $$F_n = F_{n-1} + F_{n-2}$$ -->
![fib-1](https://latex.codecogs.com/svg.latex?F_n&space;=&space;F_{n-1}&space;&plus;&space;F_{n-2})

So, each number is the sum of the previous two. This makes Fibonacci numbers recursive.

In this section a few problems related to Fibonacci numbers are presented.

- [Compute a small Fibonacci number](fibonacci_number)
- [Compute the last digit of a large Fibonacci number](last_digit_of_fibonacci_number)
- [Compute a huge Fibonacci number modulo m](fibonacci_number_huge)
- [Compute the last digit of the sum of Fibonacci numbers](last_digit_of_the_partial_sum_of_fibonacci_numbers)
- [Compute the last digit of a partial sum of Fibonacci numbers](last_digit_of_the_partial_sum_of_fibonacci_numbers)

## Mathematical Preliminaries

### Last Digit of a Large Fibonacci Number

The last digit of a large Fibonacci number can be calculated via:

<!-- $$F_n \equiv (F_{n-1} + F_{n-2}) \mod 10$$ -->
![fib-2](https://latex.codecogs.com/svg.latex?F_n&space;\equiv&space;(F_{n-1}&space;&plus;&space;F_{n-2})&space;\mod&space;10)

In general, to find the last digit of any number $\mod 10$ can be used.

### Compute a Huge Fibonacci Number Modulo m

To compute a huge Fibonacci number modulo `m` the Pisano period is used. The Pisano period defines the period with which the sequence of Fibonacci numbers taken modulo `m` repeats. The period always starts with `01`.

### Compute the Last Digit of the Sum of Fibonacci Numbers

To find the last digit of the sum, we first find the formula to calculate the sum itself. It turns out the following formula can be used:

<!-- $$\sum_{n=0}^{m} F_n = F_{n+2} - 1$$ -->
![fib-3](https://latex.codecogs.com/svg.latex?\sum_{n=0}^{m}&space;F_n&space;=&space;F_{n&plus;2}&space;-&space;1) 


This means the sum of the Fibonacci numbers starting from `0` till `m` is given by the nth plus term minus `1`. Now that we are able to calculate the sum, to find the last digit all we need is to find the value of the sum modulo `10`.

### Compute the Last Digit of the Partial Sum of Fibonacci Numbers

This is a slight alternative to the previous one. Here, we are interested in finding the last digit of a partial sum fo Fibonacci Numbers. A partial sum is simply defined as the following:

<!-- $$F_m + F_{m+1} + ... + F_n \\ \textrm{for any} \quad 0 \leq m \leq n$$ -->
![fib-4](https://latex.codecogs.com/svg.latex?%5C%5CF_m%20&plus;%20F_%7Bm&plus;1%7D%20&plus;%20...%20&plus;%20F_n%20%5C%5C%20%5Ctextrm%7Bfor%20any%7D%20%5Cquad%200%20%5Cleq%20m%20%5Cleq%20n)

To find the last digit of such a sum, we first find the sum at the end point that is $F_n$ and subtract from it the sum of the $F_{m-1}$ term and finally take modulo 10 to get the last digit.