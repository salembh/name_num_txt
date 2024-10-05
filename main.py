from numpy import array
t = array([str]*20)
r = array([str]*20)

def saisie():
    n = int(input("n: "))
    while not(3<=n<=20):
        n = int(input("n: "))
    return n

def remplir(n,t):
    for i in range(n):
        t[i] = input("username "+str(i+1)+": ")
        while not(t[i].isalpha()):
            t[i] = input("username "+str(i+1)+": ")
    return 1

def phone(n,t,r):
    for i in range(n):
        r[i] = input("phone number of user "+t[i]+": ")
        while not(len(r[i])==8):
            r[i] = input("phone number of user "+t[i]+": ")
    return 1

def fileadd(n,t,r):
    f = open("users.txt","w")
    for i in range(n):
        f.write(t[i]+", "+r[i]+"\n")
    f.close()
    return 1

def show(n,t,r):
    for i in range(n):
        print(t[i]+"'s number is "+r[i]+)

n = saisie()
remplir(n,t)
phone(n,t,r)
fileadd(n,t,r)
show(n,t,r)
print("done")