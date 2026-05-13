# Pattern Compression Program

numbers = [1,1,1,2,2,3,3,3]

compressed = []

count = 1

for i in range(len(numbers) - 1):

    if numbers[i] == numbers[i + 1]:
        count += 1

    else:
        compressed.append((numbers[i], count))
        count = 1

# Add last element
compressed.append((numbers[-1], count))

print("Compressed Output:", compressed)