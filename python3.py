liste = []
num = int(input("Liste uzunlu�unu giriniz: "))
zeroCounter = 0
for i in range(0, num):
    n = int(input())
    liste.append(n)
    if n == 0:
        zeroCounter += 1

for k in range(0, zeroCounter):
    liste.remove(0)
    
for a in range(0, zeroCounter):
    liste.insert(a, 0)
    
print(liste)