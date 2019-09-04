numsum = []

for num in range(1000):
    if num % 5 == 0 or num % 3 == 0:
        numsum.append(num)
        
print(sum(numsum))