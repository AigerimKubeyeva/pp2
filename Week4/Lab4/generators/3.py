def devisible(n):
    for i in range(n + 1):
        if(i%4 == 0 and i%3==0):
            yield i

n = int(input())
for i in devisible(n):
    print(i)