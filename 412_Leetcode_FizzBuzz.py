"""
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for
the multiples of five output “Buzz”. For numbers which are multiples of both three
and five output “FizzBuzz”.
"""

def fizzBuzz(n):
    new_lst = []
    for elem in range(1, n+1):
        if elem % 3 == 0 and elem % 5 == 0:
            new_lst.append("FizzBuzz")
        elif elem % 3 == 0:
            new_lst.append("Fizz")
        elif elem % 5 == 0:
            new_lst.append("Buzz")
        else:
            new_lst.append(str(elem))
    return(new_lst)

n = int(input())
print(fizzBuzz(n))
