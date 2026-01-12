number_repetitions = int(input("Enter the number of Fibonacci numbers to generate: "))
a, b = 0, 1
for _ in range(number_repetitions):
    print(a)
    a, b = b, a + b
    