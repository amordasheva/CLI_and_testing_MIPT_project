import os

directory = r"C:\Users\Анастасия\Desktop\CLI_and_Testing_destination"

def get_size(directory):
    total_size = 0

    for root, folders, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size

def analyze_directory(directory):
    files = os.listdir(directory)
    directory_size = []

    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.isdir(file_path):
            size = get_size(file_path)
            directory_size.append((file, size))
        else:
            size = os.path.getsize(file_path)
            directory_size.append((file, size))
    
    return directory_size

directory_size = analyze_directory(directory)
total_size = get_size(directory)

for file, size in sorted(directory_size, key=lambda x: x[1], reverse=True):
    print(f"{file}: {size} bytes")

print(f"Total size of the directory: {total_size} bytes")
print(f"Number of files: {len(directory_size)}")