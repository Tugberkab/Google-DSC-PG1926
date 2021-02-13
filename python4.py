liste = []
maximum = -100
num = int(input("Liste uzunluğunu giriniz: "))
for i in range(0, num):
    n = int(input())
    liste.append(n)
    if n > maximum and n % 2 != 0:
        maximum = n
        
print(maximum)