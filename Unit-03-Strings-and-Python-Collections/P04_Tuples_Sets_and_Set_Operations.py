
# Create a tuple
t = (101, 102, 103, 104)

print("Tuple:", t)
print("Indexing:", t[0])
print("Slicing:", t[1:3])
print("Concatenation:", t + (105,))

# Create two sets
a = {101, 102, 103}
b = {103, 104, 105}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric Difference:", a ^ b)

print("Subset:", {101, 102}.issubset(a))
print("Superset:", a.issuperset({101}))

# Add and remove elements
a.add(106)
a.remove(102)

print("Updated Set:", a)

# Set comprehension
squares = {n*n for n in range(1, 11) if n % 2 == 0}

print("Squares of Even Numbers:", squares)
