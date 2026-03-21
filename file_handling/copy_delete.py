import shutil
import os


shutil.copy("sample.txt", "sample_copy.txt")
print("File copied.")

# Create backup folder
os.makedirs("backup", exist_ok=True)

# Move file to backup
shutil.copy("sample.txt", "backup/sample_backup.txt")
print("Backup created.")


file_to_delete = "sample_copy.txt"

if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print("File deleted safely.")
else:
    print("File not found.")
