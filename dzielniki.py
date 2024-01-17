n = int(input())

'''
Poznajemy pętlę for 
for i in range(n):
    print(i)

for i in range(n+1):
    print(i,end=" ")

print()

for i in range(1,n+1):
    print(i,end=",")

print()
for i in range(1,n+1,2):
    print(i,end=" ")

print()

for i in range(n,-1,-1):
    print(i, end=" ")
'''

for i in range(1,n+1):
    if n % i == 0:
        print(i,end=" ")
print()

root = int(n**(1/2))
for i in range(1,root+1):
    if n % i == 0:
        print(i, end=" ")
        if i != n//i:
            print(n//i, end=" ")
print()
divisors = []
root = int(n**(1/2))
for i in range(1,root+1):
    if n % i == 0:
        divisors.append(i)
        if i != n//i:
            divisors.append(n//i)
print(divisors)
print(sorted(divisors))

