import os
import shutil


def copy_photos(source_dir, target_dir):
    copied_files = []
    for file in os.listdir(source_dir):
        if file.endswith(".jpg"):
            shutil.copy(os.path.join(source_dir, file), os.path.join(target_dir, file))
            copied_files.append(file)
    return copied_files
