"""
Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is better. For example, Kristen thinks that 13 is better than 12 and that 12 is better than 11 .

Given an integer, n, can you find the divisor of n that Kristin will consider to be the best?

Input Format

A single integer denoting .

Constraints
0<n <= 10^5
Output Format

Print an integer denoting the best divisor of n.

Sample Input 0

12
Sample Output 0

6
Explanation 0

The set of divisors of  12 can be expressed as {1,2,3,4,6,12} . The divisor whose digits sum to the largest number is 6 (which, having only one digit, sums to itself). Thus, we print 6 as our answer.
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    def digit_sum(num):
        return sum(int(digit) for digit in str (num))
    divisor = [i for i in range(1, n+1)if n%i ==0]
    result = max(divisor, key = digit_sum)
    print(result)
