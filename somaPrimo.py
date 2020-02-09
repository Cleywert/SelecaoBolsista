import operator
def separaPrimo(num):
    flag = 0
    i = 2
    while i<=num/2:
        if num%i==0:
            flag = 1
        i += 1
    if flag==0:
        return num
    else:
        return -1

n = int(input("Digite um número: "))
primos = [None]*n
c = 0
j = 2 
while c<n:
    num = separaPrimo(j)
    if num != -1:
        primos[c] = num
        c+=1
    j+=1
soma =  sum(primos)
print(soma)
