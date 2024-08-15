import re
def domainChecker(a,b):
    if a<2 or b<2:
        raise Exception ("bases should be more than 1")
    if a>16 or b>16:
        raise Exception ("bases should be less than 16")
def baseChecker(n,a):
    if a<=10:
        if not n.isnumeric(): raise Exception (f"{n} is not in base {a}") 
        for i in n:
            if int(i)>(a-1):
                raise Exception (f"number {n} is not suited to base {a}")
    else:
        listN = []
        for i in range(0,len(n)):
            listN.append(n[i])
        for j in listN:
            if j in alpha:
                if alpha[j]>(a-1):
                    raise Exception (f"number {n} is not suited to base {a}") 
    return
def Deci2_10(n,a):
    n = int(n)
    s = 0
    i = 0 
    while n>0:
        r = n%10 
        n //= 10 
        s = s + r*(a**i)
        i += 1
    return s
def bRadix2_10(n,b):
    s = 0
    i = 0
    while n>=b:
        r = n%b 
        n //= b 
        s = s + r*(10**i)
        i += 1
    s = s + n*(10**i)
    return s
def Deci11_16(n,a):
    global alpha
    s = 0
    listN = []
    for i in range(0,len(n)):
        listN.append(n[i])
    listN = listN[::-1]
    k = 0
    for j in listN:
        if j in alpha:
            s += alpha[j] * (a**k)
        else:
            s += int(j) * (a**k)
        k += 1
    return s
def bRadix11_16(n,b):
    s = ''
    i = 0
    listN = []
    while n>=b:
        r = n%b
        n //= b
        listN.append(r)
    else: listN.append(n)
    listN = listN[::-1]
    for j in range(0,len(listN)):
        if listN[j]>9: s += rAlpha[listN[j]]
        else: s += str(listN[j])
    return s
def main():
    while True:
        try:
            a = int(input("enter radix a (integer): "))
            b = int(input("enter radix b (integer): "))
            domainChecker(a,b)
        except Exception as e:
            print(e)
            continue
        else: break
    while True:
        n = input("enter a number (base 2-16): ")
        e = re.findall("^[1-9A-F][0-9A-F]*|[0]+$",n) 
        if len(e) != 1 or e[0] != n: 
            print("wrong input. Try again...")
        else: break
    try:
        baseChecker(n,a)
    except Exception as e:
        print(e)
    else:
        if a<=10 and b<=10:
            n2 = Deci2_10(n,a)
            n2 = bRadix2_10(n2,b)
        elif a>10 and b>10:
            n2 = Deci11_16(n,a)
            n2 = Deci11_16(n2,b)
        elif a<=10 and b>10:
            n2 = Deci2_10(n,a)
            n2 = bRadix11_16(n2,b)
        else:
            n2 = Deci11_16(n,a)
            n2 = bRadix2_10(n2,b)
        print(f"{n} in base {a}\n{n} in base {b}: {n2}")
alpha = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
rAlpha = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
main()