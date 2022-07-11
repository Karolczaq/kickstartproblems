t = int(input())
for caseno in range(1,t+1):
    n = int(input())
    lista = list(map(int,input().split()))
    k = 1
    peaks = 0
    while k < len(lista)-1:
        if lista[k]>lista[k-1] and lista[k]>lista[k+1]:
            peaks+=1
        k+=1
    print("Case #{}: {}".format(caseno,peaks))