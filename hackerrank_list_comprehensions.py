#List Comprehensions
#Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . You have to print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here,
#Example: You are given two integers x and y . yYou need to find out the ordered pairs ( i , j ) , such that ( i + j ) is not equal to n and print them in lexicographic order.( 0 <= i <= x ) and ( 0 <= j <= y) This is the code if we dont use list comprehensions in Python.

x = int ( input())
y = int ( input())
n = int ( input())
ar = []
p = 0
for i in range ( x + 1 ) :
     for j in range( y + 1):
         if i+j != n:
             ar.append([])
             ar[p] = [ i , j ]
             p+=1
print(ar)
#Other smaller codes may also exist, but using list comprehensions is always a good option. Code using list comprehensions:


x = int ( input())
y = int ( input())
n = int ( input())
print( [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n ))
