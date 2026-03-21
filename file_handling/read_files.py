
with open("sample.txt", "r") as file:
    content = file.read()

print("File content:\n")
print(content)


with open("sample.txt", "a") as file:
    file.write("This line was appended.\n")

print("\nAfter appending:\n")
with open("sample.txt", "r") as file:
    print(file.read())
