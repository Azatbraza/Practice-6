import shutil
import os

# Ensure directories exist
os.makedirs("source", exist_ok=True)
os.makedirs("destination", exist_ok=True)

# Create sample file
with open("source/example.txt", "w") as f:
    f.write("Sample file for moving.")

# Move file
shutil.move("source/example.txt", "destination/example.txt")
print("File moved.")

# Copy file back
shutil.copy("destination/example.txt", "source/example_copy.txt")
print("File copied back.")
