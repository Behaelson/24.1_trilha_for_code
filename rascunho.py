i = 0
j = 1
while i <= 9:
    i += 3
    j += 2
    if i == j:
        print("-")
    else:
        print(".")

while j < 15:
    j += 1.5
    if j == i:
        print(".")
    else:
        print("-")

print(".")

