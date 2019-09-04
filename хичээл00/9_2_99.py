a=int(input())
b=int(input())
k=int(input())
c=max(a,b)
while c >= min(a,b): # 123 = 1 2 3
    i = sum(int(j) for j in str(c))
    if i==k:
        print(c)
    c-=1
