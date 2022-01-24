"""
Task
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.
"""

#Solution 1:

if __name__ == '__main__':
    n = int(raw_input().strip())
    if n%2 !=0:
        print("Weird")
    else:
        if n in range(2,6):
            print("Not Weird")
        elif n in range(6,21):
            print("Weird")
        else:
            print("Not Weird")
            
#Solution 2:

n = int(input().strip())
check = {True: "Not Weird", False: "Weird"}

print(check[
        n%2==0 and (
            n in range(2,6) or 
            n > 20)
    ])

#Solution 3:

n = int(input())
print ("Not Weird" if not n%2 and (n in range(2,6) or n>20) else "Weird")

""" 

"""
