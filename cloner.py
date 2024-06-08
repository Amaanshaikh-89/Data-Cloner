import os
import shutil
import time

def copy_files(src, dest):
    # Get the list of files and directories in the source directory
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        
        try:
            if os.path.isdir(src_path):
                # If the item is a directory, copy it recursively
                shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
                print(f"Copying directory: {src_path}")
            elif os.path.isfile(src_path):
                # If the item is a file, copy it
                shutil.copy2(src_path, dest_path)
                print(f"Copying file: {src_path}")
        except PermissionError:
            print(f"Permission denied: {src_path}")
        except Exception as e:
            print(f"Failed to copy {src_path}: {e}")

def main():
    # Define the source directory (the directory where the USB drive is mounted)
    source_directory = "F:\\"

    # Define the destination directory (where you want to copy the files on your PC)
    destination_directory = "D:\Delete this"

    # Ensure the destination directory exists
    os.makedirs(destination_directory, exist_ok=True)

    while True:
        # Check if the USB drive is connected
        if os.path.exists(source_directory):
            print("USB drive detected.")
            copy_files(source_directory, destination_directory)
            print("Files copied successfully.")
        else:
            print("USB drive not detected.")

        # Wait for some time before checking again
        time.sleep(10)  # Check every 10 seconds instead of 1 second

if __name__ == "__main__":
    main()
