# Q1  https://www.hackerrank.com/challenges/compare-the-triplets/problem

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

# def compareTriplets(a, b):
    # Write your code here

#     ap=0
#     bp=0
#     for i in range(3):
#         if a[i]>b[i]:
#             ap=ap+1
#         elif a[i]<b[i]:
#             bp=bp+1
#     return [ap,bp]
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# result = compareTriplets(a, b)
# print(result[0],result[1])


#Q2 https://www.hackerrank.com/challenges/a-very-big-sum/problem

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

# def aVeryBigSum(ar):
#     sum=0
#     for i in range(len(ar)):
#         sum += ar[i]
#     return sum
    # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     ar_count = int(input().strip())

#     ar = list(map(int, input().rstrip().split()))

#     result = aVeryBigSum(ar)

#     fptr.write(str(result) + '\n')

#     fptr.close()

# Q3 https://www.hackerrank.com/challenges/diagonal-difference/problem

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

# def diagonalDifference(arr):
#     sum1=0
#     sum2=0
#     n=len(arr)
#     for i in range (n):
#         sum1=sum1+arr[i][i]
#         sum2=sum2+arr[i][n-1-i]
    # Write your code here
#     return abs(sum1-sum2)
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     arr = []

#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))

#     result = diagonalDifference(arr)

#     fptr.write(str(result) + '\n')

#     fptr.close()

#Q4 https://www.hackerrank.com/challenges/plus-minus/problem

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

# def plusMinus(arr):
    
#      n = len(arr)
    
#      positive = 0
#      negative = 0
#      zero = 0
     
#      for num in arr:
#         if num > 0:
#             positive += 1
#         elif num < 0:
#             negative += 1
#         else:
#             zero += 1
    
#      print(f"{positive/n:.6f}")
#      print(f"{negative/n:.6f}")
#      print(f"{zero/n:.6f}")
    # Write your code here

# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     plusMinus(arr)

# Q5  Array rotation

# ar=eval(input("Enter: "))
# n=int(input("enter n: "))

# len=len(ar)
# ar=ar[len-n:]+ar[:len-n]
# print(ar)
