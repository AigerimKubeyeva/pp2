n=-1
maxcnt=0
while n!=0:
    pred=n
    cnt=0
    while pred==n:
        cnt+=1
        n=int(input())
    if cnt>maxcnt:
        maxcnt=cnt
print(maxcnt)