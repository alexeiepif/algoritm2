import timeit
import matplotlib.pyplot as plt


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonaccibest(n):
    a = [0, 1]
    for i in range(2, n+1):
        a.append(a[i-1]+a[i-2])
    return a[n]


N = 10
b = []
c = []
d = []
print("Fibonacci:")
for i in range(1, N):
    b.append(i)
    time = sum(timeit.timeit(lambda: fibonacci(i), number=1) for j in range(10000))
    k = time/10000
    c.append(k)
    print("При i = ", i, "время = ", k)
print("Fibonaccibest:")
for i in range(1, N):
    time = sum(timeit.timeit(lambda: fibonaccibest(i), number=1) for j in range(10000))
    l = time/10000
    d.append(l)
    print("При i = ", i, "время = ", l)

plt.plot(b, c)
plt.plot(b, d)
plt.title("График")
plt.xlabel("X-ось")
plt.ylabel("Y-ось")
plt.xticks(b)
plt.yticks([0, 5e-6, 1e-5, 5e-5])
plt.show()
