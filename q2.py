arr = [-4, 3, -9, 0, 4, 1]
n = len(arr)

pos = neg = zero = 0

for i in range(len(arr)):
    if arr[i] > 0:
        pos += 1
    elif arr[i] < 0:
        neg += 1
    else:
        zero += 1

a = pos/n
b = neg/n
c = zero/n

result = [a, b, c]

print(result)
print(f"The ratio of positive number is {a} ")
print(f"The ratio of negative number is {b} ")
print(f"The ratio of zero number is {c} ")
