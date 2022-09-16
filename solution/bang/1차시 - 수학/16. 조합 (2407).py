n, m = map(int, input().split())

val1 = 1
val2 = 1
for i in range(n, n-m, -1) :
  val1 *= i

for i in range(2, m + 1) :
  val2 *= i

print(val1 // val2)