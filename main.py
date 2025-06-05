import os
import shutil

# Set the target directory
target_dir = "C:/Users/Arvie/Desktop/Python Projects/File_Organizer/test" # Change this to your target directory

# Get all items in the directory
def get_items(directory):
    return os.listdir(directory)

# Separate files and folders
def separate_items(directory):
    folders = []
    files = []
    for item in get_items(directory):
        full_path = os.path.join(directory, item)
        if os.path.isdir(full_path):
            folders.append(item)
        else:
            files.append(item)
    return {"folders": folders, "files": files}

# Get a list of unique file extensions
def get_extensions(directory):
    files = separate_items(directory)["files"]
    extensions = [f.split('.')[-1] for f in files if '.' in f]
    return list(set(extensions))

# Create folders for each file extension
def create_folders(directory):
    for ext in get_extensions(directory):
        folder_path = os.path.join(directory, ext)
        try:
            os.mkdir(folder_path)
            print(f"Created folder: {ext}")
        except FileExistsError:
            print(f"Folder already exists: {ext}")

# Move files to their corresponding extension folders
def move_files(directory):
    files = separate_items(directory)["files"]
    if not files:
        print("No files to organize.")
        return
    for file in files:
        ext = file.split('.')[-1]
        source = os.path.join(directory, file)
        destination = os.path.join(directory, ext, file)
        try:
            shutil.move(source, destination)
            print(f"Moved: {file} -> {ext}/")
        except Exception as e:
            print(f"Error moving {file}: {e}")
    print("Files organized successfully.")

# Run the organizer
def main():
    create_folders(target_dir)
    move_files(target_dir)

if __name__ == "__main__":
    main()
