names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

# enumerate()
print("Using enumerate:")
for index, name in enumerate(names):
    print(index, name)

# zip()
print("\nUsing zip:")
for name, score in zip(names, scores):
    print(name, score)

# Type checking and conversions
value = "123"

print("\nType conversion:")
num = int(value)
print(type(value), "->", type(num))

# Type checking
print("\nType checking:")
print(isinstance(num, int))
