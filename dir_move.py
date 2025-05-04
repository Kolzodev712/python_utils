# Script used to extract all fiels from inner directories to the parent one.
# Useful if one wants to extract movies to a singler folder or a similar case.

import os
import shutil

def flatten_directory(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # Skip the root directory itself
        if dirpath == root_dir:
            continue

        for file in filenames:
            src_path = os.path.join(dirpath, file)
            dest_path = os.path.join(root_dir, file)

            # Ensure no name collision
            if os.path.exists(dest_path):
                base, ext = os.path.splitext(file)
                counter = 1
                while True:
                    new_name = f"{base}_{counter}{ext}"
                    dest_path = os.path.join(root_dir, new_name)
                    if not os.path.exists(dest_path):
                        break
                    counter += 1

            shutil.move(src_path, dest_path)

        # Remove the now-empty directory
        if not os.listdir(dirpath):
            os.rmdir(dirpath)

if __name__ == "__main__":
    current_dir = os.getcwd()
    flatten_directory(current_dir)
