# This solution exceeds the time limit for test set 2
t = int(input())
for i in range(1,t+1):
    wynik = 1 # a/a = 1 which is a palindrome
    a = int(input())
    if a == 1:
        wynik = 1
    else:
        if str(a) == str(a)[::-1]:
            wynik += 1
        k = 2
        while k <= a/2:
            if a%k == 0:
                if str(int(a/k)) == str(int(a/k))[::-1]:
                    wynik+=1
            k+=1
    print("Case #{}: {}".format(i,wynik))
