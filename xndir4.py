#xndir4 (present, return -1.)
def search_index(n:list,m):
    for i in range(len(n)):
        if n[i] == m:
            return i
    return -1
x = [1,2,3,4,5,6,7,8,9,]
y = search_index(x,5)
print(y)