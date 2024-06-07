#xndir3 (Write a function that calculates the average of a list of numbers)
def average(n:list[int]):
    x = 0
    for i in n:
        x+=i
    return x / len(n)
t = [1,2,3,4,5,6,7,8,9,10,11]   
y = average(t)
print(y) 