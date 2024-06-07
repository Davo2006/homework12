#xndir5 (Write a function that calculates the sum of squares of numbers from 1 to n.)
def calculates_squares_of_nambers(n:int):
    x=0
    for i in range(1,n+1):
        i = i**2
        x+=i
    return x
c = calculates_squares_of_nambers(5)
print(c)