n = int(input("Number 1: "))
if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")
        
a = int(input("Number 2: "))
if a > n:
    print("Number 2>Number 1")
elif a == n:
    print("Number 1=Number 2")
else:
    print("Number 2<Number 1")