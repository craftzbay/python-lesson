n = int(input()) # 5    15
m = int(input()) # 10   5
niilber = 0
ih = max(n,m)
while ih >= min(n,m) : # 5 >= 10
    niilber = niilber + ih
    ih = ih - 1
print(niilber)