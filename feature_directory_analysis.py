import os


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