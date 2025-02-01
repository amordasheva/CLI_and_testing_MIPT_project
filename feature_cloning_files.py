import os
import shutil

source_dir = r"C:\Users\Анастасия\Desktop\CLI_and_Testing_source"
target_dir = r"C:\Users\Анастасия\Desktop\CLI_and_Testing_destination"

for file in os.listdir(source_dir):
    if file.endswith(".jpg"):
        shutil.copy(os.path.join(source_dir, file), os.path.join(target_dir, file))

print("Photos copied successfully.")
