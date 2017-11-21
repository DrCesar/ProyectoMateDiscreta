

div = []


def AgregarDiv(a):
    b = a[:]
    b.sort()
    if (not b in div and not 0 in b):
        div.append(b)


def Divisores(n,k,i=0,a=[]):
    if (i == k - 1):
        a[i] = n - (sum(a) - a[i])
        AgregarDiv(a)
        return a[-1]

    if (i == 0):
        a = [1] * k

    a[i] = 0
    b = 1
    while (b >= a[i]):
        a[i] = a[i] +1
        b = Divisores(n,k, i+1, a)

    return a[i]




Divisores(8,4)

print(div)





