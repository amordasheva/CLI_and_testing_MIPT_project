import os
from datetime import datetime

directory = r"C:\Users\Анастасия\Desktop\CLI_and_Testing_destination"

for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    creation_time = os.path.getctime(file_path)
    creation_date = datetime.fromtimestamp(creation_time).strftime("%d_%m_%Y")
    file_size_kb = round(os.path.getsize(file_path) / 1024, 2)

    new_filename = f"Photo_date_{creation_date}_size_{file_size_kb}{os.path.splitext(file)[1]}"
    new_file_path = os.path.join(directory, new_filename)
    os.rename(file_path, new_file_path)

print("Renaming completed")