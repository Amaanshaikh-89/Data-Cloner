import os
import shutil
import time

def main():
    # Define the source directory (the directory where the USB drive is mounted)
    source_directory = "F:\\"
    
    # Define the destination directory (where you want to copy the files on your PC)
    destination_directory = "C:\\Users\\User\\Documents\\delete this"
    
    # Ensure the destination directory exists
    os.makedirs(destination_directory, exist_ok=True)
    
    while True:
        # Check if the USB drive is connected
        if os.path.exists(source_directory):
            print("USB drive detected.")
            # Get the list of files in the USB drive
            files = os.listdir(source_directory)
            
            # Copy each file from the USB drive to the destination directory
            for file in files:
                try:
                    source_file = os.path.join(source_directory, file)
                    if os.path.isfile(source_file):  # Check if it's a file
                        shutil.copy(source_file, destination_directory)
                        print(f"Copying {file}...")
                except PermissionError:
                    print(f"Permission denied: {file}")
            
            print("Files copied successfully.")
        else:
            print("USB drive not detected.")
        
        # Wait for 1 second before checking again
        time.sleep(10)

if __name__ == "__main__":
    main()
