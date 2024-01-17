'''
sprawdzenie czy liczba dzieli się przez inną liczbę
'''
n, k = map(int, input().split())
if k == 0:
    print(f"k nie może być zerem")
elif n % k == 0:
    print(f"{k} dzieli {n}")
else:
    print(f"{k} nie dzieli {n}")
