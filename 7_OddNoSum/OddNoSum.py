n = int(input("Enter the nth term: "))

sum = 0
for i in range(n):
  if i%2 == 1:
    sum = sum + i

print("Sum is",sum)
