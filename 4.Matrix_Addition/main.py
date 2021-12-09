m, n = map(int, input().split())
a = [[int(c) for c in input().split()] for i in range(m)]
b = [[int(c) for c in input().split()] for i in range(m)]
c = [[str(a[i][j] + b[i][j]) for j in range(n)] for i in range(m)]
print("\n".join(" ".join(i) for i in c))
