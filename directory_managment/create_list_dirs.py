import os

# Create nested directories
os.makedirs("test_dir/sub_dir1/sub_dir2", exist_ok=True)
print("Directories created.")

# List files and folders
print("\nDirectory contents:")
for item in os.listdir("."):
    print(item)

# Find files by extension
print("\nFinding .txt files:")
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".txt"):
            print(os.path.join(root, file))
